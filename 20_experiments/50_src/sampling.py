"""
Sampling Module for Question Generation Experiments

Implements stratified sampling for both experiments:

Experiment 1: Sample 24 questions from 168 (1/7 = sample 1 layer worth)
- Stratified by LLM, Question Type

Experiment 2: Sample 24 questions from 48 (1/2)
- 12 MCQ: 4 per Bloom level (levels 1-3)
- 12 Open-Ended: 2 per Bloom level (all 6 levels)
"""

import os
import random
import shutil
import pandas as pd
import constants


def collect_question_files(base_path, pattern=".txt"):
    """Collect all question files from a directory tree."""
    files = []
    for root, _, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.endswith(pattern):
                files.append(os.path.join(root, filename))
    return sorted(files)


def sample_files(files, sample_size, dest_base):
    """Sample files and copy to destination."""
    if len(files) < sample_size:
        print(f"[WARNING] Only {len(files)} files available, requested {sample_size}")
        sample_size = len(files)

    if sample_size == 0:
        return []

    sampled = random.sample(files, sample_size)

    for src_path in sampled:
        # Preserve relative structure
        rel_path = os.path.relpath(src_path, os.path.dirname(src_path))
        dest_path = os.path.join(dest_base, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(src_path, dest_path)

    return sampled


def sample_exp1():
    """
    Sample 24 questions from Experiment 1 (168 total).

    Strategy: Sample 1 complete layer (all LLMs, both question types, 3 Bloom levels)
    1/7 of layers = ~24 questions

    Per sampled layer: 4 LLMs × 2 types × 3 Bloom = 24 questions
    """
    print("\n[INFO] Sampling Experiment 1 questions...")
    print("       Target: 24 questions (1 layer)")

    questions_path = os.path.join(constants.EXP1_PATH, "questions")
    sample_path = os.path.join(constants.EXP1_PATH, "sampled")

    # Randomly select 1 layer to sample completely
    sampled_layer = random.choice(constants.LAYERS)
    print(f"       Selected layer: {sampled_layer}")

    sampled_files = []
    csv_rows = []

    for llm_name in constants.LLM_NAMES:
        for q_type in constants.QUESTION_TYPES:
            src_dir = os.path.join(
                questions_path, llm_name, f"layer{sampled_layer}", q_type
            )
            dest_dir = os.path.join(
                sample_path, llm_name, f"layer{sampled_layer}", q_type
            )

            if not os.path.exists(src_dir):
                print(f"[WARNING] Directory not found: {src_dir}")
                continue

            files = [f for f in os.listdir(src_dir) if f.endswith(".txt")]

            for filename in files:
                src_file = os.path.join(src_dir, filename)
                dest_file = os.path.join(dest_dir, filename)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy2(src_file, dest_file)
                sampled_files.append(dest_file)

                # Parse Bloom level from filename
                bloom_idx = int(filename.split("_")[0].replace("bloom", ""))
                csv_rows.append([llm_name, sampled_layer, q_type, bloom_idx])

    print(f"       Sampled: {len(sampled_files)} questions")

    # Create sample CSV
    csv_path = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp1_sampled.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    df = pd.DataFrame(csv_rows, columns=["llm", "layer", "question_type", "bloom_idx"])
    df.to_csv(csv_path, index=False)
    print(f"       CSV saved: {csv_path}")

    return sampled_files


def sample_exp2():
    """
    Sample 24 questions from Experiment 2 (48 total).

    Strategy: Sample 1/2 of questions
    - 12 MCQ: Sample 2 per Bloom level (from 4 per level × 3 levels = 12)
    - 12 Open-Ended: Sample 1 per Bloom level (from 2 per level × 6 levels = 12)

    Total per LLM: 3 MCQ + 3 Open-Ended = 6
    4 LLMs × 6 = 24 questions
    """
    print("\n[INFO] Sampling Experiment 2 questions...")
    print("       Target: 24 questions (6 per LLM)")

    questions_path = os.path.join(constants.EXP2_PATH, "questions")
    sample_path = os.path.join(constants.EXP2_PATH, "sampled")

    sampled_files = []
    csv_rows = []

    for llm_name in constants.LLM_NAMES:
        # Sample MCQ: 2 questions from each of 3 Bloom levels (6 total, sample 3)
        mcq_dir = os.path.join(questions_path, llm_name, "mcq")
        mcq_dest = os.path.join(sample_path, llm_name, "mcq")

        if os.path.exists(mcq_dir):
            mcq_files = [f for f in os.listdir(mcq_dir) if f.endswith(".txt")]
            # Sample 1 question per Bloom level (3 total)
            for bloom_level in constants.BLOOM_LEVELS_MCQ:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                level_files = [
                    f for f in mcq_files if f.startswith(f"bloom{bloom_idx}_")
                ]
                if level_files:
                    selected = random.choice(level_files)
                    src_file = os.path.join(mcq_dir, selected)
                    dest_file = os.path.join(mcq_dest, selected)
                    os.makedirs(mcq_dest, exist_ok=True)
                    shutil.copy2(src_file, dest_file)
                    sampled_files.append(dest_file)
                    csv_rows.append([llm_name, "mcq", bloom_level, bloom_idx])

        # Sample Open-Ended: 1 question from each of 6 Bloom levels (sample 3)
        oe_dir = os.path.join(questions_path, llm_name, "open_ended")
        oe_dest = os.path.join(sample_path, llm_name, "open_ended")

        if os.path.exists(oe_dir):
            # Sample 3 random Bloom levels
            sampled_blooms = random.sample(constants.BLOOM_LEVELS_OPEN_ENDED, 3)
            oe_files = [f for f in os.listdir(oe_dir) if f.endswith(".txt")]

            for bloom_level in sampled_blooms:
                bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
                level_files = [
                    f for f in oe_files if f.startswith(f"bloom{bloom_idx}_")
                ]
                if level_files:
                    selected = random.choice(level_files)
                    src_file = os.path.join(oe_dir, selected)
                    dest_file = os.path.join(oe_dest, selected)
                    os.makedirs(oe_dest, exist_ok=True)
                    shutil.copy2(src_file, dest_file)
                    sampled_files.append(dest_file)
                    csv_rows.append([llm_name, "open_ended", bloom_level, bloom_idx])

    print(f"       Sampled: {len(sampled_files)} questions")

    # Create sample CSV
    csv_path = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp2_sampled.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    df = pd.DataFrame(
        csv_rows, columns=["llm", "question_type", "bloom_level", "bloom_idx"]
    )
    df.to_csv(csv_path, index=False)
    print(f"       CSV saved: {csv_path}")

    return sampled_files


def generate_expert_evaluation_csvs():
    """Generate CSV templates for expert evaluation."""
    print("\n[INFO] Generating expert evaluation CSV templates...")

    # Exp1 expert CSVs
    exp1_csv = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp1_sampled.csv"
    )
    if os.path.exists(exp1_csv):
        df = pd.read_csv(exp1_csv)

        # Add evaluation columns
        eval_columns = [
            "relevance",  # 1-5 scale
            "clarity",  # 1-5 scale
            "answerability",  # 1-5 scale
            "challenging",  # 1-5 scale
            "value",  # 1-5 scale
            "language",  # 1-5 scale
            "correctness",  # 1-5 scale
            "comments",  # Free text
        ]

        for col in eval_columns:
            df[col] = ""

        # Save to expert folders
        for i in range(1, 6):
            expert_dir = os.path.join(
                constants.ANALYSES_PATH,
                "csv",
                "qualitative",
                "exp1",
                "experts",
                f"expert_{i}",
            )
            os.makedirs(expert_dir, exist_ok=True)
            df.to_csv(os.path.join(expert_dir, "exp1_eval.csv"), index=False)

        print("       Exp1 expert CSVs created (5 experts)")

    # Exp2 student CSVs
    exp2_csv = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp2_sampled.csv"
    )
    if os.path.exists(exp2_csv):
        df = pd.read_csv(exp2_csv)

        # Add evaluation columns for Bloom alignment
        eval_columns = [
            "perceived_difficulty",  # 1-6 scale (matching Bloom levels)
            "actual_answer_quality",  # 1-5 scale
            "bloom_alignment",  # 1-5 scale
            "comments",  # Free text
        ]

        for col in eval_columns:
            df[col] = ""

        # Save to student folders
        for i in range(1, 4):
            student_dir = os.path.join(
                constants.ANALYSES_PATH,
                "csv",
                "qualitative",
                "exp2",
                "students",
                f"student_{i}",
            )
            os.makedirs(student_dir, exist_ok=True)
            df.to_csv(os.path.join(student_dir, "exp2_eval.csv"), index=False)

        print("       Exp2 student CSVs created (3 students)")


def run_sampling():
    """Run the complete sampling pipeline."""
    print("\n" + "=" * 60)
    print("Question Sampling")
    print("=" * 60)

    sample_exp1()
    sample_exp2()
    generate_expert_evaluation_csvs()

    print("\n[INFO] Sampling completed.")


if __name__ == "__main__":
    run_sampling()
