import os
import csv
import random
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from tqdm import tqdm
from collections import defaultdict

import constants
from file_utils import load_txt, save_result
from prompt_utils import load_prompt, format_prompt, get_bloom, get_learning_objective
from api_calls import llm_generation


random.seed(constants.RANDOM_SEED)
llm_counters = defaultdict(int)
counter_lock = threading.Lock()


def increment_counter(llm_name):
    with counter_lock:
        llm_counters[llm_name] += 1


def reset_counters():
    with counter_lock:
        llm_counters.clear()
        for llm_name in constants.LLM_NAMES:
            llm_counters[llm_name] = 0


def get_progress():
    with counter_lock:
        if not llm_counters:
            return "Progress"
        parts = [f"{llm}:{cnt}" for llm, cnt in sorted(llm_counters.items())]
        return f"Progress [{' | '.join(parts)}]"


def get_max_tokens(bloom_level):
    return constants.MAX_TOKENS_BY_BLOOM.get(bloom_level, 6000)


def clean_questions(exp_path):
    questions_dir = os.path.join(exp_path, "questions")
    if os.path.exists(questions_dir):
        try:
            shutil.rmtree(questions_dir)
            print(f"[INFO] Cleaned old questions: {os.path.relpath(questions_dir)}")
        except Exception as e:
            print(f"[ERROR] Could not clean questions directory: {e}")


def create_csvs(exp_name, headers, rows):
    file_path = os.path.join(
        constants.ANALYSES_PATH, "csv", "initial", f"{exp_name}.csv"
    )
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            if rows:
                writer.writerows(rows)
        print(f"[INFO] Initial CSV created: {os.path.relpath(file_path)}")
    except IOError as e:
        print(f"[ERROR] Could not write to CSV file {file_path}: {e}")


def load_layer_content(layer_num):
    return load_txt(os.path.join(constants.INPUT_SOURCES_PATH, f"layer{layer_num}.txt"))


def load_concatenated_content():
    return load_txt(
        os.path.join(constants.INPUT_SOURCES_PATH, "concatenated_common.txt")
    )


def generate_mcq_question(
    llm_name,
    clients,
    source_text,
    bloom_level,
    bloom_data,
    learning_objective="",
    max_tokens=4000,
):
    level_data = bloom_data.get(bloom_level, {})

    # Step 1: Stem
    stem_result = llm_generation(
        llm_name,
        clients,
        format_prompt(
            load_prompt(constants.PROMPT_MCQ_STEM),
            text=source_text,
            bloom_level=bloom_level,
            bloom_level_description=level_data.get("description", ""),
            bloom_level_verbs=level_data.get("verbs", ""),
            learning_objective=learning_objective,
        ),
        max_tokens=max_tokens // 2,
    )

    # Step 2: Keys
    keys_result = llm_generation(
        llm_name,
        clients,
        format_prompt(
            load_prompt(constants.PROMPT_MCQ_KEYS),
            text=source_text,
            stem=stem_result,
            bloom_level=bloom_level,
            bloom_level_description=level_data.get("description", ""),
            learning_objective=learning_objective,
        ),
        max_tokens=max_tokens // 2,
    )

    # Step 3: Distractors
    distractors_result = llm_generation(
        llm_name,
        clients,
        format_prompt(
            load_prompt(constants.PROMPT_MCQ_DISTRACTORS),
            text=source_text,
            stem=stem_result,
            keys=keys_result,
            bloom_level=bloom_level,
            bloom_level_description=level_data.get("description", ""),
            learning_objective=learning_objective,
        ),
        max_tokens=max_tokens // 2,
    )

    return f"""## Multiple-Choice Question

### Bloom Level: {bloom_level}

### Learning Objective 

{learning_objective}

### Stem Generation

{stem_result}

### Key Generation

{keys_result}

### Distractor Generation + Union of all

{distractors_result}

### Source Text

{source_text}
"""


def generate_open_ended_question(
    llm_name,
    clients,
    source_text,
    bloom_level,
    bloom_data,
    learning_objective,
    max_tokens,
):
    level_data = bloom_data.get(bloom_level, {})

    # Question
    question_result = llm_generation(
        llm_name,
        clients,
        format_prompt(
            load_prompt(constants.PROMPT_OPEN_ENDED_QUESTION),
            text=source_text,
            bloom_level=bloom_level,
            bloom_level_description=level_data.get("description", ""),
            bloom_level_verbs=level_data.get("verbs", ""),
            learning_objective=learning_objective,
        ),
        max_tokens=max_tokens // 2,
    )

    # Answer
    answer_result = llm_generation(
        llm_name,
        clients,
        format_prompt(
            load_prompt(constants.PROMPT_OPEN_ENDED_ANSWER),
            text=source_text,
            question=question_result,
            bloom_level=bloom_level,
            bloom_level_description=level_data.get("description", ""),
            bloom_level_verbs=level_data.get("verbs", ""),
            learning_objective=learning_objective,
        ),
        max_tokens=max_tokens,
    )

    return f"""## Open-Ended Question

### Bloom Level: {bloom_level}

### Learning Objective

{learning_objective}

### Question Generation

{question_result}

### Answer Generation + Union of all

{answer_result}

### Source Text

{source_text}
"""


def generate_task(task_params):
    (
        llm_name,
        clients,
        q_type,
        source_text,
        bloom_level,
        bloom_data,
        learning_obj,
        output_path,
        desc,
        max_tokens,
    ) = task_params

    try:
        result = (
            generate_mcq_question if q_type == "mcq" else generate_open_ended_question
        )(
            llm_name,
            clients,
            source_text,
            bloom_level,
            bloom_data,
            learning_obj,
            max_tokens,
        )

        if result:
            save_result(output_path, result)
            increment_counter(llm_name)
            return True
    except Exception as e:
        tqdm.write(f"[ERROR] {llm_name}: {desc} - {e}")
    return False


def run_tasks(tasks, exp_desc):
    tqdm.write(f"\n[INFO] Running {len(tasks)} tasks for {exp_desc}...")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(generate_task, task): task for task in tasks}

        with tqdm(total=len(tasks), desc=get_progress()) as pbar:
            for future in as_completed(futures):
                future.result()
                pbar.set_description(get_progress())
                pbar.update(1)


def run_exp1(clients):
    tqdm.write("\n[INFO] Experiment 1: Content Fidelity")
    tqdm.write(
        "       4 LLMs × 7 Layers × 2 Question Types × 1 Random Bloom Level = 56 questions"
    )
    tqdm.write("     MCQ: 1 per LLM per Layer (Bloom 1-3 random)")
    tqdm.write("     Open-Ended: 1 per LLM per Layer (Bloom 1-6 random)")

    clean_questions(constants.EXP1_PATH)
    reset_counters()

    tasks, csv_rows = [], []
    bloom_data = get_bloom()

    for layer_num in constants.LAYERS:
        source_text = load_layer_content(layer_num)
        if not source_text:
            print(f"[WARNING] Could not load layer{layer_num}.txt")
            continue

        learning_obj = get_learning_objective("exp1", layer=layer_num)

        for llm_name in constants.LLM_NAMES:
            # MCQ: Random Bloom 1-3
            if constants.GENERATE_MCQ:
                bloom_level = random.choice(constants.BLOOM_LEVELS_MCQ)
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "mcq",
                        source_text,
                        bloom_level,
                        bloom_data,
                        learning_obj,
                        os.path.join(
                            constants.EXP1_PATH,
                            "questions",
                            llm_name,
                            "mcq",
                            f"bloom{bloom_idx}_layer{layer_num}.txt",
                        ),
                        f"L{layer_num} MCQ {bloom_level}",
                        get_max_tokens(bloom_level),
                    )
                )
                csv_rows.append([llm_name, layer_num, "mcq", bloom_idx])

            # Open-Ended: Random Bloom 1-6
            if constants.GENERATE_OPEN_ENDED:
                bloom_level = random.choice(constants.BLOOM_LEVELS_OPEN_ENDED)
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "open_ended",
                        source_text,
                        bloom_level,
                        bloom_data,
                        learning_obj,
                        os.path.join(
                            constants.EXP1_PATH,
                            "questions",
                            llm_name,
                            "open_ended",
                            f"bloom{bloom_idx}_layer{layer_num}.txt",
                        ),
                        f"L{layer_num} OE {bloom_level}",
                        get_max_tokens(bloom_level),
                    )
                )
                csv_rows.append([llm_name, layer_num, "open_ended", bloom_idx])

    csv_rows.sort(key=lambda row: (row[0], row[2], int(row[3]), row[1]))
    create_csvs("exp1", ["llm", "layer", "question_type", "bloom_idx"], csv_rows)

    run_tasks(tasks, "Exp 1")
    tqdm.write(f"[INFO] Experiment 1 completed: {len(tasks)} questions generated")


def run_exp2(clients):
    tqdm.write("\n[INFO] Experiment 2: Bloom Alignment")
    tqdm.write("       4 LLMs × 2 Question Types = 48 questions")
    tqdm.write("       MCQ: 6 per LLM (Bloom 1-3, each 2×)")
    tqdm.write("       Open-ended: 6 per LLM (Bloom 1-6, each 1×)")

    clean_questions(constants.EXP2_PATH)
    reset_counters()

    tasks, csv_rows = [], []
    bloom_data = get_bloom()
    source_text = load_concatenated_content()

    if not source_text:
        print("[ERROR] Could not load concatenated content for Exp2")
        return

    for llm_name in constants.LLM_NAMES:
        # MCQ: 2 questions per Bloom level (1-3)
        if constants.GENERATE_MCQ:
            for bloom_level in constants.BLOOM_LEVELS_MCQ:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                learning_obj = get_learning_objective("exp2", bloom_level=bloom_level)

                for q_num in range(1, constants.EXP2_MCQ_PER_BLOOM + 1):
                    tasks.append(
                        (
                            llm_name,
                            clients,
                            "mcq",
                            source_text,
                            bloom_level,
                            bloom_data,
                            learning_obj,
                            os.path.join(
                                constants.EXP2_PATH,
                                "questions",
                                llm_name,
                                "mcq",
                                f"bloom{bloom_idx}_q{q_num}.txt",
                            ),
                            f"MCQ B{bloom_idx} Q{q_num}",
                            get_max_tokens(bloom_level),
                        )
                    )
                    csv_rows.append([llm_name, "mcq", bloom_idx, q_num])

        # Open-Ended: 1 question per Bloom level (1-6)
        if constants.GENERATE_OPEN_ENDED:
            for bloom_level in constants.BLOOM_LEVELS_OPEN_ENDED:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                learning_obj = get_learning_objective("exp2", bloom_level=bloom_level)

                for q_num in range(1, constants.EXP2_OPEN_ENDED_PER_BLOOM + 1):
                    tasks.append(
                        (
                            llm_name,
                            clients,
                            "open_ended",
                            source_text,
                            bloom_level,
                            bloom_data,
                            learning_obj,
                            os.path.join(
                                constants.EXP2_PATH,
                                "questions",
                                llm_name,
                                "open_ended",
                                f"bloom{bloom_idx}_q{q_num}.txt",
                            ),
                            f"OE B{bloom_idx} Q{q_num}",
                            get_max_tokens(bloom_level),
                        )
                    )
                    csv_rows.append([llm_name, "open_ended", bloom_idx, q_num])

    csv_rows.sort(key=lambda row: (row[0], row[1], row[2], row[3]))
    create_csvs("exp2", ["llm", "question_type", "bloom_idx", "question_num"], csv_rows)

    run_tasks(tasks, "Exp 2")
    tqdm.write(f"[INFO] Experiment 2 completed: {len(tasks)} questions generated")
