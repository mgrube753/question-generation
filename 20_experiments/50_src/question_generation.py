import os
import csv
import random
import constants
import shutil
from file_utils import load_txt, save_result
from prompt_utils import load_prompt, format_prompt, get_bloom, get_learning_objective
from api_calls import llm_generation
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from tqdm import tqdm
from collections import defaultdict


random.seed(constants.RANDOM_SEED)
llm_counters = defaultdict(int)
counter_lock = threading.Lock()


def clean_questions(exp_path):
    questions_dir = os.path.join(exp_path, "questions")
    if os.path.exists(questions_dir):
        try:
            shutil.rmtree(questions_dir)
            print(f"[INFO] Cleaned old questions: {os.path.relpath(questions_dir)}")
        except Exception as e:
            print(f"[ERROR] Could not clean questions directory: {e}")


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
        desc_parts = []
        for llm_name in sorted(llm_counters.keys()):
            count = llm_counters[llm_name]
            desc_parts.append(f"{llm_name}:{count}")
        return f"Progress [{' | '.join(desc_parts)}]"


def create_csvs(exp_name, headers, rows):
    try:
        initial_csv_dir = os.path.join(constants.ANALYSES_PATH, "csv", "initial")
        file_path = os.path.join(initial_csv_dir, f"{exp_name}.csv")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            if rows:
                writer.writerows(rows)
        print(f"[INFO] Initial CSV created: {os.path.relpath(file_path)}")
    except IOError as e:
        print(f"[ERROR] Could not write to CSV file {file_path}: {e}")


def load_layer_content(layer_num):
    layer_path = os.path.join(constants.INPUT_SOURCES_PATH, f"layer{layer_num}.txt")
    return load_txt(layer_path)


def load_concatenated_content():
    concat_path = os.path.join(constants.INPUT_SOURCES_PATH, "concatenated_common.txt")
    content = load_txt(concat_path)

    if content:
        return content

    # Fallback: concatenate all layers
    print("[INFO] Concatenating all layer files...")
    concatenated = []
    for layer_num in constants.LAYERS:
        layer_content = load_layer_content(layer_num)
        if layer_content:
            concatenated.append(f"--- Layer {layer_num} ---\n{layer_content.strip()}")

    return "\n\n".join(concatenated)


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

    # Step 1: Generate MCQ Stem
    stem_template = load_prompt(constants.PROMPT_MCQ_STEM)
    if not stem_template:
        print(f"[WARNING] MCQ stem prompt not found")
        return None

    stem_prompt = format_prompt(
        stem_template,
        text=source_text,
        bloom_level=bloom_level,
        bloom_level_description=level_data.get("description", ""),
        bloom_level_verbs=level_data.get("verbs", ""),
        learning_objective=learning_objective,
    )

    stem_result = llm_generation(
        llm_name, clients, stem_prompt, max_tokens=max_tokens // 2
    )
    if not stem_result:
        return None

    # Step 2: Generate Keys (correct answers)
    keys_template = load_prompt(constants.PROMPT_MCQ_KEYS)
    if not keys_template:
        print(f"[WARNING] MCQ keys prompt not found")
        return None

    keys_prompt = format_prompt(
        keys_template,
        text=source_text,
        stem=stem_result,
        bloom_level=bloom_level,
        bloom_level_description=level_data.get("description", ""),
        learning_objective=learning_objective,
    )

    keys_result = llm_generation(
        llm_name, clients, keys_prompt, max_tokens=max_tokens // 2
    )
    if not keys_result:
        return None

    # Step 3: Generate Distractors (incorrect answers)
    distractors_template = load_prompt(constants.PROMPT_MCQ_DISTRACTORS)
    if not distractors_template:
        print(f"[WARNING] MCQ distractors prompt not found")
        return None

    distractors_prompt = format_prompt(
        distractors_template,
        text=source_text,
        stem=stem_result,
        keys=keys_result,
        bloom_level=bloom_level,
        bloom_level_description=level_data.get("description", ""),
        learning_objective=learning_objective,
    )

    distractors_result = llm_generation(
        llm_name, clients, distractors_prompt, max_tokens=max_tokens // 2
    )
    if not distractors_result:
        return None

    # Combine into complete MCQ
    complete_mcq = f"""## Multiple-Choice Question

### Bloom Level: {bloom_level}

### Learning Objective: {learning_objective}

### Stem Generation:

{stem_result}

### Key Generation:

{keys_result}

### Distractor Generation + Union of all:

{distractors_result}

### Source Text:

{source_text}
"""
    return complete_mcq


def generate_open_ended_question(
    llm_name,
    clients,
    source_text,
    bloom_level,
    bloom_data,
    learning_objective="",
    max_tokens=4000,
):
    level_data = bloom_data.get(bloom_level, {})

    prompt_template = load_prompt(constants.PROMPT_OPEN_ENDED)
    if not prompt_template:
        print(f"[WARNING] Open-ended prompt not found")
        return None

    formatted_prompt = format_prompt(
        prompt_template,
        text=source_text,
        bloom_level=bloom_level,
        bloom_level_description=level_data.get("description", ""),
        bloom_level_verbs=level_data.get("verbs", ""),
        learning_objective=learning_objective,
    )

    result = llm_generation(llm_name, clients, formatted_prompt, max_tokens=max_tokens)
    if not result:
        return None

    complete_question = f"""## Open-Ended Question

### Bloom Level: {bloom_level}

### Learning Objective: {learning_objective}

### Question

{result}

### Source Text

{source_text}
"""
    return complete_question


def generate_task(task_params):
    (
        llm_name,
        clients,
        question_type,
        source_text,
        bloom_level,
        bloom_data,
        learning_objective,
        output_path,
        description,
        max_tokens,
    ) = task_params

    try:
        if question_type == "mcq":
            result = generate_mcq_question(
                llm_name,
                clients,
                source_text,
                bloom_level,
                bloom_data,
                learning_objective,
                max_tokens,
            )
        else:
            result = generate_open_ended_question(
                llm_name,
                clients,
                source_text,
                bloom_level,
                bloom_data,
                learning_objective,
                max_tokens,
            )

        if result:
            save_result(output_path, result)
            increment_counter(llm_name)
            return True
    except Exception as e:
        print(f"[ERROR] {llm_name}: {description} - {e}")
    return False


def run_tasks(tasks, exp_desc):
    print(f"\n[INFO] Running {len(tasks)} tasks for {exp_desc}...")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(generate_task, task): task for task in tasks}

        with tqdm(total=len(tasks), desc=get_progress()) as pbar:
            for future in as_completed(futures):
                future.result()
                pbar.set_description(get_progress())
                pbar.update(1)


def run_exp1(clients):
    print("\n[INFO] Experiment 1: Content Fidelity")
    print(
        "       4 LLMs × 7 Layers × 2 Question Types × 1 Random Bloom Level = 56 questions"
    )
    print("     MCQ: 1 per LLM per Layer (Bloom 1-3 random)")
    print("     Open-Ended: 1 per LLM per Layer (Bloom 1-6 random)")

    clean_questions(constants.EXP1_PATH)
    reset_counters()

    tasks = []
    csv_rows = []
    bloom_data = get_bloom()

    for layer_num in constants.LAYERS:
        source_text = load_layer_content(layer_num)
        if not source_text:
            print(f"[WARNING] Could not load layer{layer_num}.txt")
            continue

        learning_objective = get_learning_objective("exp1", layer=layer_num)

        # need halfway randomized bloom level setup
        for llm_name in constants.LLM_NAMES:
            # MCQ: Sample 1 random Bloom level from levels 1-3
            if constants.GENERATE_MCQ:
                bloom_level = random.choice(constants.BLOOM_LEVELS_MCQ)
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                output_path = os.path.join(
                    constants.EXP1_PATH,
                    "questions",
                    llm_name,
                    "mcq",
                    f"bloom{bloom_idx}_layer{layer_num}.txt",
                )

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "mcq",
                        source_text,
                        bloom_level,
                        bloom_data,
                        learning_objective,
                        output_path,
                        f"L{layer_num} MCQ {bloom_level}",
                        4000,
                    )
                )
                csv_rows.append([llm_name, layer_num, "mcq", bloom_idx])

            # Open-Ended: Sample 1 random Bloom levels from all 6
            if constants.GENERATE_OPEN_ENDED:
                bloom_level = random.choice(constants.BLOOM_LEVELS_OPEN_ENDED)
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                output_path = os.path.join(
                    constants.EXP1_PATH,
                    "questions",
                    llm_name,
                    "open_ended",
                    f"bloom{bloom_idx}_layer{layer_num}.txt",
                )

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "open_ended",
                        source_text,
                        bloom_level,
                        bloom_data,
                        learning_objective,
                        output_path,
                        f"L{layer_num} OE {bloom_level}",
                        4000,
                    )
                )
                csv_rows.append([llm_name, layer_num, "open_ended", bloom_idx])

    csv_rows.sort(key=lambda row: (row[0], int(row[1]), row[2], row[3]))
    headers = ["llm", "layer", "question_type", "bloom_idx"]
    create_csvs("exp1", headers, csv_rows)

    run_tasks(tasks, "Exp 1")
    print(f"[INFO] Experiment 1 completed: {len(tasks)} questions generated")


def run_exp2(clients):
    print("\n[INFO] Experiment 2: Bloom Alignment")
    print("       4 LLMs × 2 Question Types = 48 questions")
    print("       MCQ: 6 per LLM (Bloom 1-3, each 2×)")
    print("       Open-ended: 6 per LLM (Bloom 1-6, each 1×)")

    clean_questions(constants.EXP2_PATH)
    reset_counters()

    tasks = []
    csv_rows = []
    bloom_data = get_bloom()
    source_text = load_concatenated_content()

    if not source_text:
        print("[ERROR] Could not load concatenated content for Exp2")
        return

    for llm_name in constants.LLM_NAMES:
        # MCQ: 2 questions per Bloom level (levels 1-3) = 6 MCQ per LLM
        if constants.GENERATE_MCQ:
            for bloom_level in constants.BLOOM_LEVELS_MCQ:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1

                learning_objective = get_learning_objective(
                    "exp2", bloom_level=bloom_level
                )

                for q_num in range(1, constants.EXP2_MCQ_PER_BLOOM + 1):
                    output_path = os.path.join(
                        constants.EXP2_PATH,
                        "questions",
                        llm_name,
                        "mcq",
                        f"bloom{bloom_idx}_q{q_num}.txt",
                    )

                    tasks.append(
                        (
                            llm_name,
                            clients,
                            "mcq",
                            source_text,
                            bloom_level,
                            bloom_data,
                            learning_objective,
                            output_path,
                            f"MCQ B{bloom_idx} Q{q_num}",
                            4000,
                        )
                    )
                    csv_rows.append([llm_name, "mcq", bloom_idx, q_num])

        # Open-Ended: 1 question per Bloom level (all 6 levels) = 6 OE per LLM
        if constants.GENERATE_OPEN_ENDED:
            for bloom_level in constants.BLOOM_LEVELS_OPEN_ENDED:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1

                learning_objective = get_learning_objective(
                    "exp2", bloom_level=bloom_level
                )

                for q_num in range(1, constants.EXP2_OPEN_ENDED_PER_BLOOM + 1):
                    output_path = os.path.join(
                        constants.EXP2_PATH,
                        "questions",
                        llm_name,
                        "open_ended",
                        f"bloom{bloom_idx}_q{q_num}.txt",
                    )

                    tasks.append(
                        (
                            llm_name,
                            clients,
                            "open_ended",
                            source_text,
                            bloom_level,
                            bloom_data,
                            learning_objective,
                            output_path,
                            f"OE B{bloom_idx} Q{q_num}",
                            4000,
                        )
                    )
                    csv_rows.append([llm_name, "open_ended", bloom_idx, q_num])

    csv_rows.sort(key=lambda row: (row[0], row[1], row[2], row[3]))
    headers = ["llm", "question_type", "bloom_idx", "question_num"]
    create_csvs("exp2", headers, csv_rows)

    run_tasks(tasks, "Exp 2")
    print(f"[INFO] Experiment 2 completed: {len(tasks)} questions generated")
