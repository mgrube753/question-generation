"""
Sampling Module for Question Generation Experiments
"""

import os
import random
import shutil
import pandas as pd
import constants


def clean_samples(exp_path):
    sample_dir = os.path.join(exp_path, "sampled")
    if os.path.exists(sample_dir):
        try:
            shutil.rmtree(sample_dir)
            print(f"[INFO] Cleaned old samples: {os.path.relpath(sample_dir)}")
        except Exception as e:
            print(f"[ERROR] Could not clean samples directory: {e}")


def collect_question_files(base_path, pattern=".txt"):
    files = []
    for root, _, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.endswith(pattern):
                files.append(os.path.join(root, filename))
    return files


def sample_files(files, sample_size, dest_base):
    sampled = random.sample(files, min(sample_size, len(files)))
    for src in sampled:
        rel_path = os.path.relpath(src, os.path.dirname(src))
        dest = os.path.join(dest_base, rel_path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(src, dest)
    return sampled


def sample_exp1():
    print("\n[INFO] Sampling Experiment 1 questions...")
    print("       Target: 24 questions (6 per LLM: 3 MCQ + 3 Open-Ended)")

    # Clean old samples before starting
    clean_samples(constants.EXP1_PATH)

    questions_path = os.path.join(constants.EXP1_PATH, "questions")
    sample_path = os.path.join(constants.EXP1_PATH, "sampled")

    # Collect questions organized by LLM and question type
    questions_by_llm_type = {
        llm: {"mcq": [], "open_ended": []} for llm in constants.LLM_NAMES
    }

    for llm_name in constants.LLM_NAMES:
        llm_dir = os.path.join(questions_path, llm_name)
        if not os.path.exists(llm_dir):
            print(f"[WARNING] Directory not found: {llm_dir}")
            continue

        # Check both question types
        for q_type in constants.QUESTION_TYPES:
            type_dir = os.path.join(llm_dir, q_type)
            if not os.path.exists(type_dir):
                print(f"[WARNING] Directory not found: {type_dir}")
                continue

            # Scan files in this type directory
            for filename in os.listdir(type_dir):
                if not filename.endswith(".txt"):
                    continue

                # Expected format: bloom{idx}_layer{num}.txt
                if filename.startswith("bloom") and "_layer" in filename:
                    try:
                        parts = filename.replace(".txt", "").split("_")
                        bloom_idx = int(parts[0].replace("bloom", ""))
                        layer_num = int(parts[1].replace("layer", ""))

                        file_path = os.path.join(type_dir, filename)

                        questions_by_llm_type[llm_name][q_type].append(
                            {
                                "path": file_path,
                                "llm": llm_name,
                                "layer": layer_num,
                                "question_type": q_type,
                                "bloom_idx": bloom_idx,
                            }
                        )
                    except (ValueError, IndexError) as e:
                        print(f"[WARNING] Could not parse filename {filename}: {e}")

    # Stratified sampling: 3 MCQ + 3 Open-Ended per LLM
    sampled_questions = []
    for llm_name in constants.LLM_NAMES:
        # Sample 3 MCQ questions
        mcq_questions = questions_by_llm_type[llm_name]["mcq"]
        if len(mcq_questions) >= 3:
            sampled_questions.extend(random.sample(mcq_questions, 3))
        else:
            print(f"[WARNING] {llm_name} has only {len(mcq_questions)} MCQ questions")
            sampled_questions.extend(mcq_questions)

        # Sample 3 Open-Ended questions
        oe_questions = questions_by_llm_type[llm_name]["open_ended"]
        if len(oe_questions) >= 3:
            sampled_questions.extend(random.sample(oe_questions, 3))
        else:
            print(
                f"[WARNING] {llm_name} has only {len(oe_questions)} Open-Ended questions"
            )
            sampled_questions.extend(oe_questions)

    print(f"       Sampled: {len(sampled_questions)} questions")

    if len(sampled_questions) == 0:
        print("[ERROR] No questions were sampled! Check file paths and structure.")
        return []

    # Copy sampled files and create CSV rows
    csv_rows = []
    for q in sampled_questions:
        # Create destination path matching source structure: {llm}/{question_type}/
        dest_dir = os.path.join(sample_path, q["llm"], q["question_type"])
        os.makedirs(dest_dir, exist_ok=True)

        # Copy file
        dest_file = os.path.join(dest_dir, os.path.basename(q["path"]))
        shutil.copy2(q["path"], dest_file)

        # Add to CSV
        csv_rows.append([q["llm"], q["layer"], q["question_type"], q["bloom_idx"]])

    # Show distribution per LLM
    print("\n       Distribution per LLM:")
    for llm_name in constants.LLM_NAMES:
        llm_questions = [q for q in sampled_questions if q["llm"] == llm_name]
        mcq_count = len([q for q in llm_questions if q["question_type"] == "mcq"])
        oe_count = len([q for q in llm_questions if q["question_type"] == "open_ended"])
        print(
            f"       {llm_name}: {len(llm_questions)} total ({mcq_count} MCQ, {oe_count} OE)"
        )

    # Show layer distribution
    layer_dist = {}
    for q in sampled_questions:
        layer_dist[q["layer"]] = layer_dist.get(q["layer"], 0) + 1
    print(f"\n       Layer distribution: {dict(sorted(layer_dist.items()))}")

    # Create sample CSV
    csv_path = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp1_sampled.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    df = pd.DataFrame(csv_rows, columns=["llm", "layer", "question_type", "bloom_idx"])
    df = df.sort_values(["llm", "question_type", "bloom_idx", "layer"])
    df.to_csv(csv_path, index=False)
    print(f"\n       CSV saved: {csv_path} ({len(df)} rows)")

    return sampled_questions


def sample_exp2():
    print("\n[INFO] Sampling Experiment 2 questions...")
    print("       Target: 24 questions (6 per LLM)")

    questions_path = os.path.join(constants.EXP2_PATH, "questions")
    sample_path = os.path.join(constants.EXP2_PATH, "sampled")

    sampled_files = []
    csv_rows = []

    for llm_name in constants.LLM_NAMES:
        # Sample MCQ: 1 question from each of 3 Bloom levels (3 total per LLM)
        mcq_dir = os.path.join(questions_path, llm_name, "mcq")
        mcq_dest = os.path.join(sample_path, llm_name, "mcq")

        if os.path.exists(mcq_dir):
            mcq_files = [f for f in os.listdir(mcq_dir) if f.endswith(".txt")]
            # Sample 1 question per Bloom level (from 2 available per level)
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
                    csv_rows.append([llm_name, "mcq", bloom_idx])

        # Sample Open-Ended: 3 random Bloom levels from 6 (3 total per LLM)
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
                    csv_rows.append([llm_name, "open_ended", bloom_idx])

    print(f"       Sampled: {len(sampled_files)} questions")

    # Create sample CSV
    csv_path = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp2_sampled.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    df = pd.DataFrame(csv_rows, columns=["llm", "question_type", "bloom_idx"])
    df = df.sort_values(["llm", "question_type", "bloom_idx"])
    df.to_csv(csv_path, index=False)
    print(f"       CSV saved: {csv_path}")

    return sampled_files


def generate_expert_evaluation_csvs():
    print("\n[INFO] Generating expert evaluation CSV templates...")

    # Exp1 expert CSVs
    exp1_csv = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp1_sampled.csv"
    )
    if os.path.exists(exp1_csv):
        df = pd.read_csv(exp1_csv)

        # Add sample_id as first column (001, 002, ...)
        df.insert(0, "sample_id", [f"{i+1:03d}" for i in range(len(df))])

        # Remove llm and bloom_idx columns for blind evaluation
        df = df.drop(columns=["llm", "bloom_idx"])

        # Add evaluation columns
        eval_columns = [
            "relevance",  # 0-10 scale
            "clarity",  # 0-10 scale
            "answerability",  # 0-10 scale
            "challenging",  # 0-10 scale
            "value",  # 0-10 scale
            "language",  # 0-10 scale
            "correctness",  # 0-10 scale
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
            )
            os.makedirs(expert_dir, exist_ok=True)

            for i in range(1, 6):
                df.to_csv(os.path.join(expert_dir, f"exp1_eval_e{i}.csv"), index=False)

        print("       Exp1 expert CSVs created (5 experts)")

    # Exp2 student CSVs
    exp2_csv = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp2_sampled.csv"
    )
    if os.path.exists(exp2_csv):
        df = pd.read_csv(exp2_csv)

        # Add sample_id as first column (001, 002, ...)
        df.insert(0, "sample_id", [f"{i+1:03d}" for i in range(len(df))])

        # Remove llm and bloom_idx columns for blind evaluation
        df = df.drop(columns=["llm", "bloom_idx"])

        # Add evaluation columns for Bloom alignment
        eval_columns = [
            "relevance",  # 0-10 scale
            "clarity",  # 0-10 scale
            "answerability",  # 0-10 scale
            "challenging",  # 0-10 scale
            "value",  # 0-10 scale
            "language",  # 0-10 scale
            "bloom_rating",  # 1-6 scale (Bloom level)
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
            )
            os.makedirs(student_dir, exist_ok=True)
            for i in range(1, 4):
                df.to_csv(os.path.join(student_dir, f"exp2_eval_s{i}.csv"), index=False)

        print("       Exp2 student CSVs created (3 students)")


def run_sampling():
    print("\n" + "=" * 60)
    print("Question Sampling")
    print("=" * 60)

    random.seed(constants.RANDOM_SEED)

    clean_samples(constants.EXP1_PATH)
    clean_samples(constants.EXP2_PATH)

    sample_exp1()
    sample_exp2()
    generate_expert_evaluation_csvs()

    print("\n[INFO] Sampling completed.")


if __name__ == "__main__":
    run_sampling()
