import os
import pandas as pd
import numpy as np
import concurrent.futures
import threading

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


def get_adherence_scores(clients, question, source_text, evaluator):
    prompt_path = os.path.join(
        PROMPT_TEMPLATES_PATH, "evaluation", "exp1_adherence_eval.md"
    )
    prompt_template = load_txt(prompt_path)

    prompt = prompt_template.replace("{question_text}", question).replace(
        "{context_text}", source_text
    )

    response = llm_generation(evaluator, clients, prompt, max_tokens=1200)
    if response:
        try:
            score = float(response.strip())
            if 0 <= score <= 1:
                return score
            else:
                return None
        except ValueError:
            return None
    else:
        return None


def get_adherence_scores_parallel(
    clients,
    questions_sources_pairs,
    max_workers=2,
    df=None,
    valid_indices=None,
    csv_path=None,
):
    results = []
    lock = threading.Lock()

    def process_pair(idx_pair):
        idx, (question, source) = idx_pair
        openai_score = get_adherence_scores(clients, question, source, "openai")
        anthropic_score = get_adherence_scores(clients, question, source, "anthropic")

        with lock:
            if df is not None and valid_indices is not None and csv_path is not None:
                df_idx = valid_indices[idx]
                df.at[df_idx, "adherence_score_openai"] = openai_score
                df.at[df_idx, "adherence_score_anthropic"] = anthropic_score
                df.to_csv(csv_path, index=False)

        return (openai_score, anthropic_score)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_pair, (i, pair)): i
            for i, pair in enumerate(questions_sources_pairs)
        }

        for future in tqdm(
            concurrent.futures.as_completed(futures),
            total=len(futures),
            desc="Adherence Scores",
        ):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"Error processing question: {e}")
                results.append((None, None))

    return results


def get_question_path(llm, layer):
    """Get path to a question file based on LLM and layer."""
    # Check both mcq and open_ended directories
    mcq_path = os.path.join(EXP1_PATH, "questions", llm, "mcq")
    oe_path = os.path.join(EXP1_PATH, "questions", llm, "open_ended")

    for base_path in [mcq_path, oe_path]:
        if os.path.exists(base_path):
            # Find any file that matches the layer
            for filename in os.listdir(base_path):
                if f"_layer{layer}.txt" in filename:
                    return os.path.join(base_path, filename)

    return None


def get_source_file_path(layer):
    """Get path to source file (OSI layer)."""
    source_path = os.path.join(INPUT_SOURCES_PATH, f"layer{layer}.txt")
    return source_path


def process_experiment():
    """Process all generated questions in Experiment 1."""
    print(f"[INFO] Processing Experiment 1 - OSI Layer-based Questions")
    print("=" * 80)

    clients = init_clients()

    # Create output directory
    csv_output_path = os.path.join(
        ANALYSES_PATH, "csv", "quantitative", "exp1", "exp1_adherence.csv"
    )
    os.makedirs(os.path.dirname(csv_output_path), exist_ok=True)

    # Collect all question files
    questions_dir = os.path.join(EXP1_PATH, "questions")

    rows = []
    questions = []
    sources = []
    valid_indices = []
    comparison_info = []

    print("[INFO] Loading questions and sources...")

    idx = 0
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

                # Extract bloom level and layer from filename
                # Format: bloom{X}_layer{Y}.txt
                try:
                    parts = filename.replace(".txt", "").split("_")
                    bloom_idx = int(parts[0].replace("bloom", ""))
                    layer = int(parts[1].replace("layer", ""))
                except:
                    print(f"[WARNING] Could not parse filename: {filename}")
                    continue

                question_path = os.path.join(type_path, filename)
                question_content = load_txt(question_path)

                if not question_content:
                    print(f"[WARNING] Could not load: {question_path}")
                    continue

                # Filter out answer options (Falsch/Richtig markers)
                question = "\n".join(
                    line
                    for line in question_content.splitlines()
                    if not line.strip().endswith("(Falsch)")
                    and not line.strip().endswith("(Richtig)")
                )

                if not question.strip():
                    print(
                        f"[WARNING] Question is empty after filtering: {question_path}"
                    )
                    continue

                # Get source file
                source_path = get_source_file_path(layer)
                source_text = load_txt(source_path)

                if not source_text:
                    print(f"[WARNING] No source found: {source_path}")
                    continue

                print(
                    f"[MATCH {len(questions)+1:3d}] Question: {os.path.relpath(question_path, EXP1_PATH)}"
                )
                print(f"             Source:   layer{layer}.txt")
                print(
                    f"             LLM:      {llm} | Type: {q_type} | Bloom: {bloom_idx}"
                )
                print("-" * 80)

                questions.append(question)
                sources.append(source_text)
                valid_indices.append(idx)
                comparison_info.append(
                    {
                        "question_path": question_path,
                        "source_path": source_path,
                        "llm": llm,
                        "question_type": q_type,
                        "layer": layer,
                        "bloom_idx": bloom_idx,
                    }
                )

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

    print(f"\n[INFO] Total valid pairs found: {len(questions)}")
    print("=" * 80)

    # Create DataFrame and save initial version
    df = pd.DataFrame(rows)
    df.to_csv(csv_output_path, index=False)
    print("=" * 80)

    # Calculate adherence scores
    questions_sources_pairs = list(zip(questions, sources))

    print("[INFO] Processing adherence scores with OpenAI and Anthropic...")
    adherence_results = get_adherence_scores_parallel(
        clients,
        questions_sources_pairs,
        max_workers=2,
        df=df,
        valid_indices=valid_indices,
        csv_path=csv_output_path,
    )

    # Print results
    for i, idx in enumerate(valid_indices):
        openai_score, anthropic_score = adherence_results[i]
        info = comparison_info[i]
        print(
            f"[ADHERENCE OpenAI] Layer {info['layer']} -> {info['llm']} ({info['question_type']}, Bloom {info['bloom_idx']}): {openai_score}"
        )
        print(
            f"[ADHERENCE Anthropic] Layer {info['layer']} -> {info['llm']} ({info['question_type']}, Bloom {info['bloom_idx']}): {anthropic_score}"
        )

    print(f"\n[INFO] Final results saved to {csv_output_path}")
    print("=" * 80)


if __name__ == "__main__":
    process_experiment()
