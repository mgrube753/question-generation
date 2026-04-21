import os
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from tqdm import tqdm
from constants import (
    EXP1_PATH,
    INPUT_SOURCES_PATH,
    ANALYSES_PATH,
    PROMPT_TEMPLATES_PATH,
)
from file_utils import load_txt
from api_calls import llm_generation
from api_config import init_clients


def get_adherence_score(clients, question, source_text, evaluator):
    prompt = load_txt(
        os.path.join(PROMPT_TEMPLATES_PATH, "evaluation", "exp1_adherence_eval.md")
    )
    prompt = prompt.replace("{question_text}", question).replace(
        "{context_text}", source_text
    )

    response = llm_generation(evaluator, clients, prompt, max_tokens=1200)
    try:
        score = float(response.strip())
        return score if 0 <= score <= 1 else None
    except (ValueError, AttributeError):
        return None


def process_adherence_scores(
    clients, question_source_pairs, df, valid_indices, csv_path, max_workers=2
):
    lock = Lock()

    def evaluate_pair(idx_pair):
        idx, (question, source) = idx_pair
        scores = {
            "openai": get_adherence_score(clients, question, source, "openai"),
            "anthropic": get_adherence_score(clients, question, source, "anthropic"),
        }

        with lock:
            df_idx = valid_indices[idx]
            df.at[df_idx, "adherence_score_openai"] = scores["openai"]
            df.at[df_idx, "adherence_score_anthropic"] = scores["anthropic"]
            df.to_csv(csv_path, index=False)

        return scores

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(evaluate_pair, (i, pair)): i
            for i, pair in enumerate(question_source_pairs)
        }

        results = []
        for future in tqdm(
            as_completed(futures), total=len(futures), desc="Adherence Scores"
        ):
            try:
                results.append(future.result())
            except Exception as e:
                print(f"Error: {e}")
                results.append({"openai": None, "anthropic": None})

    return results


def parse_filename(filename):
    try:
        parts = filename.replace(".txt", "").split("_")
        return int(parts[0].replace("bloom", "")), int(parts[1].replace("layer", ""))
    except:
        return None, None


def filter_question_text(content):
    return "\n".join(
        line
        for line in content.splitlines()
        if not line.strip().endswith(("(Falsch)", "(Richtig)"))
    )


def process_experiment():
    print("[INFO] Processing Experiment 1 - OSI Layer-based Questions")
    print("=" * 80)

    clients = init_clients()

    # Setup output
    csv_path = os.path.join(
        ANALYSES_PATH, "csv", "quantitative", "exp1", "exp1_adherence.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    # Collect question-source pairs
    questions_dir = os.path.join(EXP1_PATH, "questions")
    rows, questions, sources, valid_indices = [], [], [], []
    idx = 0

    print("[INFO] Loading questions and sources...")

    for llm in os.listdir(questions_dir):
        llm_path = os.path.join(questions_dir, llm)
        if not os.path.isdir(llm_path):
            continue

        for q_type in ["mcq", "open_ended"]:
            type_path = os.path.join(llm_path, q_type)
            if not os.path.exists(type_path):
                continue

            for filename in os.listdir(type_path):
                if not filename.endswith(".txt"):
                    continue

                bloom_idx, layer = parse_filename(filename)
                if bloom_idx is None:
                    print(f"[WARNING] Could not parse filename: {filename}")
                    continue

                # Load and filter question
                question_path = os.path.join(type_path, filename)
                question_content = load_txt(question_path)
                if not question_content:
                    continue

                question = filter_question_text(question_content)
                if not question.strip():
                    print(f"[WARNING] Empty question after filtering: {question_path}")
                    continue

                # Load source
                source_path = os.path.join(INPUT_SOURCES_PATH, f"layer{layer}.txt")
                source_text = load_txt(source_path)
                if not source_text:
                    print(f"[WARNING] No source found: {source_path}")
                    continue

                # Store data
                print(
                    f"[MATCH {len(questions)+1:3d}] {os.path.relpath(question_path, EXP1_PATH)}"
                )
                print(
                    f"             Source: layer{layer}.txt | LLM: {llm} | Type: {q_type} | Bloom: {bloom_idx}"
                )
                print("-" * 80)

                questions.append(question)
                sources.append(source_text)
                valid_indices.append(idx)
                rows.append(
                    {
                        "llm": llm,
                        "question_type": q_type,
                        "layer": layer,
                        "bloom_idx": bloom_idx,
                        "adherence_score_openai": np.nan,
                        "adherence_score_anthropic": np.nan,
                    }
                )
                idx += 1

    if not questions:
        print("[ERROR] No valid question-source pairs found!")
        return

    print(f"\n[INFO] Total valid pairs: {len(questions)}")
    print("=" * 80)

    # Initialize DataFrame
    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)

    # Calculate adherence scores
    print("[INFO] Processing adherence scores with OpenAI and Anthropic...")
    results = process_adherence_scores(
        clients, list(zip(questions, sources)), df, valid_indices, csv_path
    )

    # Print results
    for i, idx in enumerate(valid_indices):
        row = rows[i]
        scores = results[i]
        print(
            f"[ADHERENCE OpenAI   ] Layer {row['layer']} -> {row['llm']} "
            f"({row['question_type']}, Bloom {row['bloom_idx']}): {scores['openai']}"
        )
        print(
            f"[ADHERENCE Anthropic] Layer {row['layer']} -> {row['llm']} "
            f"({row['question_type']}, Bloom {row['bloom_idx']}): {scores['anthropic']}"
        )

    print(f"\n[INFO] Results saved to {csv_path}")
    print("=" * 80)


if __name__ == "__main__":
    process_experiment()
