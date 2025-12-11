"""
Question Generation Module

Implements the unified question generation pipeline for two experiments:

Experiment 1 (Content Fidelity):
- 4 LLMs × 1 Script × 7 Layers × 2 Question Types × 3 Random Bloom Levels = 168 questions
- Sample 24 questions (1/7 of layers)

Experiment 2 (Bloom Alignment):
- 4 LLMs × 1 Script × 2 Question Types × 6 Bloom Levels = 48 questions
- Sample 24 questions (1/2)
- 12 Open-Ended: 2 per Bloom level (all 6 levels)
- 12 MCQ: 4 per Bloom level (levels 1-3 only)

Question Types:
- MCQ: 3-step process (stem → keys → distractors)
- Open-Ended: 1 prompt
"""

import os
import csv
import random
import constants
from file_utils import load_txt, save_result, slugify
from prompt_utils import load_prompt, format_prompt, get_bloom
from api_calls import llm_generation
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from tqdm import tqdm
from collections import defaultdict


# Thread-safe counters for progress tracking
llm_counters = defaultdict(int)
counter_lock = threading.Lock()


def increment_counter(llm_name):
    """Increment the question counter for an LLM."""
    with counter_lock:
        llm_counters[llm_name] += 1


def reset_counters():
    """Reset all LLM counters."""
    with counter_lock:
        llm_counters.clear()
        for llm_name in constants.LLM_NAMES:
            llm_counters[llm_name] = 0


def get_progress():
    """Get formatted progress string for all LLMs."""
    with counter_lock:
        if not llm_counters:
            return "Progress"
        desc_parts = []
        for llm_name in sorted(llm_counters.keys()):
            count = llm_counters[llm_name]
            desc_parts.append(f"{llm_name}:{count}")
        return f"Progress [{' | '.join(desc_parts)}]"


def create_csvs(exp_name, headers, rows):
    """Create initial CSV file for an experiment."""
    try:
        initial_csv_dir = os.path.join(constants.ANALYSES_PATH, "csv", "initial")

        if exp_name.startswith("exp1"):
            exp_subdir = os.path.join(initial_csv_dir, "exp1")
        elif exp_name.startswith("exp2"):
            exp_subdir = os.path.join(initial_csv_dir, "exp2")
        else:
            exp_subdir = initial_csv_dir

        file_path = os.path.join(exp_subdir, f"{exp_name}.csv")
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
    """Load content for a specific OSI layer."""
    layer_path = os.path.join(constants.INPUT_SOURCES_PATH, f"layer{layer_num}.txt")
    return load_txt(layer_path)


def load_concatenated_content():
    """Load concatenated content of all layers for Exp2."""
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
    llm_name, clients, source_text, bloom_level, bloom_data, max_tokens=2400
):
    """
    Generate a Multiple-Choice question using the 3-step MCQ pipeline:
    1. Generate stem (question text)
    2. Generate keys (correct answers)
    3. Generate distractors (incorrect answers)

    Returns the complete MCQ or None if any step fails.
    """
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
    )

    stem_result = llm_generation(
        llm_name, clients, stem_prompt, max_tokens=max_tokens // 3
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
    )

    keys_result = llm_generation(
        llm_name, clients, keys_prompt, max_tokens=max_tokens // 3
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
    )

    distractors_result = llm_generation(
        llm_name, clients, distractors_prompt, max_tokens=max_tokens // 3
    )
    if not distractors_result:
        return None

    # Combine into complete MCQ
    complete_mcq = f"""## Multiple-Choice Question
### Bloom Level: {bloom_level}

### Stem (Question):
{stem_result}

### Correct Answer(s):
{keys_result}

### Distractors (Incorrect Answers):
{distractors_result}
"""
    return complete_mcq


def generate_open_ended_question(
    llm_name, clients, source_text, bloom_level, bloom_data, max_tokens=2400
):
    """
    Generate an Open-Ended question.

    Returns the complete question or None if generation fails.
    """
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
    )

    result = llm_generation(llm_name, clients, formatted_prompt, max_tokens=max_tokens)
    if not result:
        return None

    complete_question = f"""## Open-Ended Question
### Bloom Level: {bloom_level}

{result}
"""
    return complete_question


def generate_task(task_params):
    """
    Execute a single question generation task.

    task_params is a tuple containing:
    - llm_name: Name of the LLM
    - clients: Dictionary of LLM clients
    - question_type: 'mcq' or 'open_ended'
    - source_text: Input text for question generation
    - bloom_level: Bloom's taxonomy level
    - bloom_data: Bloom level descriptions and verbs
    - output_path: Path to save the generated question
    - description: Task description for logging
    - max_tokens: Maximum tokens for generation
    """
    (
        llm_name,
        clients,
        question_type,
        source_text,
        bloom_level,
        bloom_data,
        output_path,
        description,
        max_tokens,
    ) = task_params

    try:
        if question_type == "mcq":
            result = generate_mcq_question(
                llm_name, clients, source_text, bloom_level, bloom_data, max_tokens
            )
        else:
            result = generate_open_ended_question(
                llm_name, clients, source_text, bloom_level, bloom_data, max_tokens
            )

        if result:
            save_result(output_path, result)
            increment_counter(llm_name)
            return True
    except Exception as e:
        print(f"[ERROR] {llm_name}: {description} - {e}")
    return False


def run_tasks(tasks, exp_desc):
    """Run all tasks with progress tracking."""
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(generate_task, task): task for task in tasks}

        with tqdm(
            total=len(tasks), desc=f"{exp_desc} {get_progress()}", unit="task"
        ) as pbar:
            for future in as_completed(futures):
                future.result()
                pbar.set_description(f"{exp_desc} {get_progress()}")
                pbar.update(1)


def run_exp1(clients):
    """
    Experiment 1: Content Fidelity

    4 LLMs × 1 Script × 7 Layers × 2 Question Types × 3 Random Bloom Levels = 168 questions

    For each layer, we randomly select 3 Bloom levels.
    MCQ uses only Bloom 1-3, Open-Ended uses all 6.
    """
    print("\n[INFO] Experiment 1: Content Fidelity")
    print(
        "       4 LLMs × 7 Layers × 2 Question Types × 3 Bloom Levels = 168 questions"
    )
    reset_counters()

    tasks = []
    csv_rows = []
    bloom_data = get_bloom()

    for layer_num in constants.LAYERS:
        source_text = load_layer_content(layer_num)
        if not source_text:
            print(f"[WARNING] Could not load layer{layer_num}.txt")
            continue

        for llm_name in constants.LLM_NAMES:
            # MCQ: Sample 3 random Bloom levels from levels 1-3
            mcq_bloom_levels = random.sample(constants.BLOOM_LEVELS_MCQ, 3)

            for bloom_level in mcq_bloom_levels:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                output_path = os.path.join(
                    constants.EXP1_PATH,
                    "questions",
                    llm_name,
                    f"layer{layer_num}",
                    "mcq",
                    f"bloom{bloom_idx}_{slugify(bloom_level)}.txt",
                )

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "mcq",
                        source_text,
                        bloom_level,
                        bloom_data,
                        output_path,
                        f"L{layer_num} MCQ {bloom_level}",
                        2400,
                    )
                )
                csv_rows.append([llm_name, layer_num, "mcq", bloom_level, bloom_idx])

            # Open-Ended: Sample 3 random Bloom levels from all 6
            oe_bloom_levels = random.sample(constants.BLOOM_LEVELS_OPEN_ENDED, 3)

            for bloom_level in oe_bloom_levels:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                output_path = os.path.join(
                    constants.EXP1_PATH,
                    "questions",
                    llm_name,
                    f"layer{layer_num}",
                    "open_ended",
                    f"bloom{bloom_idx}_{slugify(bloom_level)}.txt",
                )

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "open_ended",
                        source_text,
                        bloom_level,
                        bloom_data,
                        output_path,
                        f"L{layer_num} OE {bloom_level}",
                        2400,
                    )
                )
                csv_rows.append(
                    [llm_name, layer_num, "open_ended", bloom_level, bloom_idx]
                )

    # Sort CSV rows and create file
    csv_rows.sort(key=lambda row: (row[0], int(row[1]), row[2], row[4]))
    headers = ["llm", "layer", "question_type", "bloom_level", "bloom_idx"]
    create_csvs("exp1", headers, csv_rows)

    run_tasks(tasks, "Exp 1")
    print(f"[INFO] Experiment 1 completed: {len(tasks)} questions generated")


def run_exp2(clients):
    """
    Experiment 2: Bloom Alignment

    4 LLMs × 1 Script (concatenated) × 2 Question Types × 6 Bloom Levels = 48 questions

    - 12 MCQ: 4 questions per Bloom level (levels 1-3 only)
    - 12 Open-Ended: 2 questions per Bloom level (all 6 levels)

    Uses concatenated script content for full OSI model coverage.
    """
    print("\n[INFO] Experiment 2: Bloom Alignment")
    print("       4 LLMs × 2 Question Types × varying Bloom Levels = 48 questions")
    reset_counters()

    tasks = []
    csv_rows = []
    bloom_data = get_bloom()
    source_text = load_concatenated_content()

    if not source_text:
        print("[ERROR] Could not load concatenated content for Exp2")
        return

    for llm_name in constants.LLM_NAMES:
        # MCQ: 4 questions per Bloom level (levels 1-3)
        for bloom_level in constants.BLOOM_LEVELS_MCQ:
            bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1

            for q_num in range(1, constants.EXP2_MCQ_PER_BLOOM + 1):
                output_path = os.path.join(
                    constants.EXP2_PATH,
                    "questions",
                    llm_name,
                    "mcq",
                    f"bloom{bloom_idx}_{slugify(bloom_level)}_q{q_num}.txt",
                )

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "mcq",
                        source_text,
                        bloom_level,
                        bloom_data,
                        output_path,
                        f"MCQ B{bloom_idx} Q{q_num}",
                        2400,
                    )
                )
                csv_rows.append([llm_name, "mcq", bloom_level, bloom_idx, q_num])

        # Open-Ended: 2 questions per Bloom level (all 6 levels)
        for bloom_level in constants.BLOOM_LEVELS_OPEN_ENDED:
            bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1

            for q_num in range(1, constants.EXP2_OPEN_ENDED_PER_BLOOM + 1):
                output_path = os.path.join(
                    constants.EXP2_PATH,
                    "questions",
                    llm_name,
                    "open_ended",
                    f"bloom{bloom_idx}_{slugify(bloom_level)}_q{q_num}.txt",
                )

                tasks.append(
                    (
                        llm_name,
                        clients,
                        "open_ended",
                        source_text,
                        bloom_level,
                        bloom_data,
                        output_path,
                        f"OE B{bloom_idx} Q{q_num}",
                        2400,
                    )
                )
                csv_rows.append([llm_name, "open_ended", bloom_level, bloom_idx, q_num])

    # Sort CSV rows and create file
    csv_rows.sort(key=lambda row: (row[0], row[1], row[3], row[4]))
    headers = ["llm", "question_type", "bloom_level", "bloom_idx", "question_num"]
    create_csvs("exp2", headers, csv_rows)

    run_tasks(tasks, "Exp 2")
    print(f"[INFO] Experiment 2 completed: {len(tasks)} questions generated")
