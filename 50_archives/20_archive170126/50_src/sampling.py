import os
import random
import shutil
import pandas as pd
import constants


def clean_directory(path, description):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"[INFO] Cleaned old {description}: {os.path.relpath(path)}")


def clean_samples(exp_path):
    clean_directory(os.path.join(exp_path, "sampled"), "samples")


def clean_renamed_samples():
    clean_directory(
        os.path.join(constants.EXPERIMENTS_BASE_PATH, "70_sampled_questions"),
        "renamed samples",
    )


def parse_question_filename(filename):
    try:
        parts = filename.replace(".txt", "").split("_")
        return int(parts[0].replace("bloom", "")), int(parts[1].replace("layer", ""))
    except (ValueError, IndexError):
        return None, None


def collect_exp1_questions():
    questions_path = os.path.join(constants.EXP1_PATH, "questions")
    questions_by_llm_type = {
        llm: {"mcq": [], "open_ended": []} for llm in constants.LLM_NAMES
    }

    for llm_name in constants.LLM_NAMES:
        for q_type in constants.QUESTION_TYPES:
            type_dir = os.path.join(questions_path, llm_name, q_type)
            if not os.path.exists(type_dir):
                continue

            for filename in os.listdir(type_dir):
                if not filename.endswith(".txt") or not filename.startswith("bloom"):
                    continue

                bloom_idx, layer_num = parse_question_filename(filename)
                if bloom_idx is None:
                    continue

                questions_by_llm_type[llm_name][q_type].append(
                    {
                        "path": os.path.join(type_dir, filename),
                        "llm": llm_name,
                        "layer": layer_num,
                        "question_type": q_type,
                        "bloom_idx": bloom_idx,
                    }
                )

    return questions_by_llm_type


def sample_questions_per_llm(questions_by_llm_type, n_per_type=3):
    sampled = []
    for llm_name in constants.LLM_NAMES:
        for q_type in ["mcq", "open_ended"]:
            questions = questions_by_llm_type[llm_name][q_type]
            n_sample = min(n_per_type, len(questions))
            if n_sample < n_per_type:
                print(
                    f"[WARNING] {llm_name} has only {len(questions)} {q_type} questions"
                )
            sampled.extend(random.sample(questions, n_sample))
    return sampled


def copy_sampled_questions(sampled_questions, sample_path):
    csv_rows = []
    for q in sampled_questions:
        dest_dir = os.path.join(sample_path, q["llm"], q["question_type"])
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copy2(q["path"], os.path.join(dest_dir, os.path.basename(q["path"])))
        csv_rows.append([q["llm"], q["layer"], q["question_type"], q["bloom_idx"]])
    return csv_rows


def print_exp1_statistics(sampled_questions):
    print("\n       Distribution per LLM:")
    for llm_name in constants.LLM_NAMES:
        llm_q = [q for q in sampled_questions if q["llm"] == llm_name]
        mcq = sum(1 for q in llm_q if q["question_type"] == "mcq")
        oe = sum(1 for q in llm_q if q["question_type"] == "open_ended")
        print(f"       {llm_name}: {len(llm_q)} total ({mcq} MCQ, {oe} OE)")

    layer_dist = {}
    for q in sampled_questions:
        layer_dist[q["layer"]] = layer_dist.get(q["layer"], 0) + 1
    print(f"\n       Layer distribution: {dict(sorted(layer_dist.items()))}")


def sample_exp1():
    print("\n[INFO] Sampling Experiment 1 questions...")
    print("       Target: 24 questions (6 per LLM: 3 MCQ + 3 Open-Ended)")

    clean_samples(constants.EXP1_PATH)

    questions_by_llm_type = collect_exp1_questions()
    sampled_questions = sample_questions_per_llm(questions_by_llm_type)

    print(f"       Sampled: {len(sampled_questions)} questions")
    if not sampled_questions:
        print("[ERROR] No questions were sampled! Check file paths and structure.")
        return []

    sample_path = os.path.join(constants.EXP1_PATH, "sampled")
    csv_rows = copy_sampled_questions(sampled_questions, sample_path)
    print_exp1_statistics(sampled_questions)

    # Save CSV
    csv_path = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp1_sampled.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    df = pd.DataFrame(csv_rows, columns=["llm", "layer", "question_type", "bloom_idx"])
    df.sort_values(["llm", "question_type", "bloom_idx", "layer"], inplace=True)
    df.to_csv(csv_path, index=False)
    print(f"\n       CSV saved: {csv_path} ({len(df)} rows)")

    return sampled_questions


def sample_bloom_files(src_dir, dest_dir, bloom_levels, llm_name, q_type):
    if not os.path.exists(src_dir):
        return []

    files = [f for f in os.listdir(src_dir) if f.endswith(".txt")]
    csv_rows = []

    for bloom_level in bloom_levels:
        bloom_idx = constants.BLOOM_LEVELS_ORDERED.index(bloom_level) + 1
        level_files = [f for f in files if f.startswith(f"bloom{bloom_idx}_")]

        if level_files:
            selected = random.choice(level_files)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(
                os.path.join(src_dir, selected), os.path.join(dest_dir, selected)
            )
            csv_rows.append([llm_name, q_type, bloom_idx])

    return csv_rows


def sample_exp2():
    print("\n[INFO] Sampling Experiment 2 questions...")
    print("       Target: 24 questions (6 per LLM)")

    questions_path = os.path.join(constants.EXP2_PATH, "questions")
    sample_path = os.path.join(constants.EXP2_PATH, "sampled")
    csv_rows = []

    for llm_name in constants.LLM_NAMES:
        # MCQ: all 3 Bloom levels (1-3)
        mcq_rows = sample_bloom_files(
            os.path.join(questions_path, llm_name, "mcq"),
            os.path.join(sample_path, llm_name, "mcq"),
            constants.BLOOM_LEVELS_MCQ,
            llm_name,
            "mcq",
        )
        csv_rows.extend(mcq_rows)

        # Open-ended: 3 random Bloom levels (1-6)
        oe_rows = sample_bloom_files(
            os.path.join(questions_path, llm_name, "open_ended"),
            os.path.join(sample_path, llm_name, "open_ended"),
            random.sample(constants.BLOOM_LEVELS_OPEN_ENDED, 3),
            llm_name,
            "open_ended",
        )
        csv_rows.extend(oe_rows)

    print(f"       Sampled: {len(csv_rows)} questions")

    # Save CSV
    csv_path = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp2_sampled.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    df = pd.DataFrame(csv_rows, columns=["llm", "question_type", "bloom_idx"])
    df.sort_values(["llm", "question_type", "bloom_idx"], inplace=True)
    df.to_csv(csv_path, index=False)
    print(f"       CSV saved: {csv_path}")

    return csv_rows


def filter_question_content(content):
    lines = content.split("\n")

    # Determine question type
    if "## Multiple-Choice Question" in content:
        header = "## Multiple-Choice-Question"
    else:
        header = "## Offene Frage"

    learning_obj = ""
    in_learning_obj = False
    for i, line in enumerate(lines):
        if (
            line.strip() == "### Learning Objective"
            or line.strip() == "### Learning Objective "
        ):
            in_learning_obj = True
            continue
        if in_learning_obj:
            if line.startswith("###"):
                break
            if line.strip():
                learning_obj = line.strip()
                break

    final_question = ""
    in_final = False
    for _, line in enumerate(lines):
        if (
            "### Distractor Generation + Union" in line
            or "### Answer Generation + Union" in line
        ):
            in_final = True
            continue
        if in_final:
            if line.startswith("### Source Text"):
                break
            final_question += line + "\n"
    final_question = final_question.strip()

    source_text = ""
    in_source = False
    for line in lines:
        if line.startswith("### Source Text"):
            in_source = True
            continue
        if in_source:
            source_text += line + "\n"
    source_text = source_text.strip()

    output = f"""{header}

### Lernziel

{learning_obj}

### Formulierte Frage

{final_question}

### Quelltext

{source_text}
"""
    return output


def rename_and_copy_exp1(df, renamed_base):
    exp1_dest = os.path.join(renamed_base, "10_exp1")
    os.makedirs(exp1_dest, exist_ok=True)
    sample_path = os.path.join(constants.EXP1_PATH, "sampled")

    for idx, row in df.iterrows():
        sample_id = f"{idx + 1:03d}"
        src_file = os.path.join(
            sample_path,
            row["llm"],
            row["question_type"],
            f"bloom{row['bloom_idx']}_layer{row['layer']}.txt",
        )
        if os.path.exists(src_file):
            with open(src_file, "r", encoding="utf-8") as f:
                content = f.read()
            filtered_content = filter_question_content(content)

            dest_file = os.path.join(
                exp1_dest, f"{sample_id}_{row['question_type']}_layer{row['layer']}.txt"
            )
            with open(dest_file, "w", encoding="utf-8") as f:
                f.write(filtered_content)
        else:
            print(f"[WARNING] Source file not found: {src_file}")

    print(f"       Exp1: {len(df)} files created in 70_sampled_questions/10_exp1")


def rename_and_copy_exp2(df, renamed_base):
    exp2_dest = os.path.join(renamed_base, "20_exp2")
    os.makedirs(exp2_dest, exist_ok=True)
    sample_path = os.path.join(constants.EXP2_PATH, "sampled")

    for idx, row in df.iterrows():
        sample_id = f"{idx + 1:03d}"
        src_dir = os.path.join(sample_path, row["llm"], row["question_type"])

        if os.path.exists(src_dir):
            matching_files = [
                f
                for f in os.listdir(src_dir)
                if f.startswith(f"bloom{row['bloom_idx']}_") and f.endswith(".txt")
            ]
            if matching_files:
                src_file = os.path.join(src_dir, matching_files[0])
                # Read and filter content
                with open(src_file, "r", encoding="utf-8") as f:
                    content = f.read()
                filtered_content = filter_question_content(content)

                dest_file = os.path.join(
                    exp2_dest, f"{sample_id}_{row['question_type']}_concatenated.txt"
                )
                with open(dest_file, "w", encoding="utf-8") as f:
                    f.write(filtered_content)
            else:
                print(
                    f"[WARNING] No matching file for bloom{row['bloom_idx']} in {src_dir}"
                )
        else:
            print(f"[WARNING] Directory not found: {src_dir}")

    print(f"       Exp2: {len(df)} files created in 70_sampled_questions/20_exp2")


def create_renamed_samples():
    print("\n[INFO] Creating renamed sample collections...")
    renamed_base = os.path.join(constants.EXPERIMENTS_BASE_PATH, "70_sampled_questions")

    # Exp1
    exp1_csv = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp1_sampled.csv"
    )
    if os.path.exists(exp1_csv):
        rename_and_copy_exp1(pd.read_csv(exp1_csv), renamed_base)

    # Exp2
    exp2_csv = os.path.join(
        constants.ANALYSES_PATH, "csv", "sampled", "exp2_sampled.csv"
    )
    if os.path.exists(exp2_csv):
        rename_and_copy_exp2(pd.read_csv(exp2_csv), renamed_base)


def create_evaluation_csv(
    csv_path, eval_columns, n_evaluators, evaluator_prefix, exp_label
):
    if not os.path.exists(csv_path):
        return

    df = pd.read_csv(csv_path)
    df.insert(0, "sample_id", [f"{i+1:03d}" for i in range(len(df))])
    df = df.drop(columns=["llm", "bloom_idx"])

    for col in eval_columns:
        df[col] = ""

    output_dir = os.path.join(constants.ANALYSES_PATH, "csv", "qualitative", exp_label)
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, n_evaluators + 1):
        df.to_csv(
            os.path.join(output_dir, f"{exp_label}_eval_{evaluator_prefix}{i}.csv"),
            index=False,
        )

    print(
        f"       {exp_label.capitalize()} {evaluator_prefix.upper()} CSVs created ({n_evaluators} evaluators)"
    )


def generate_expert_evaluation_csvs():
    print("\n[INFO] Generating expert evaluation CSV templates...")

    # Exp1: 5 experts
    create_evaluation_csv(
        os.path.join(constants.ANALYSES_PATH, "csv", "sampled", "exp1_sampled.csv"),
        [
            "relevance",
            "clarity",
            "answerability",
            "challenging",
            "value",
            "language",
            "correctness",
            "comments",
        ],
        5,
        "e",
        "exp1",
    )

    # Exp2: 3 students
    create_evaluation_csv(
        os.path.join(constants.ANALYSES_PATH, "csv", "sampled", "exp2_sampled.csv"),
        [
            "relevance",
            "clarity",
            "answerability",
            "challenging",
            "value",
            "language",
            "bloom_rating",
            "comments",
        ],
        3,
        "s",
        "exp2",
    )


def run_sampling():
    print("\n" + "=" * 60)
    print("Question Sampling")
    print("=" * 60)

    random.seed(constants.RANDOM_SEED)

    clean_samples(constants.EXP1_PATH)
    clean_samples(constants.EXP2_PATH)
    clean_renamed_samples()

    sample_exp1()
    sample_exp2()
    create_renamed_samples()
    generate_expert_evaluation_csvs()

    print("\n[INFO] Sampling completed.")


if __name__ == "__main__":
    run_sampling()
