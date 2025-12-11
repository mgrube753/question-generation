"""
Main Entry Point for Question Generation Experiments

Experiment 1 (Content Fidelity):
- 4 LLMs × 1 Script × 7 Layers × 2 Question Types × 3 Random Bloom Levels = 168 questions
- Sample 24 questions (1/7 of layers)

Experiment 2 (Bloom Alignment):
- 4 LLMs × 1 Script × 2 Question Types × 6 Bloom Levels = 48 questions
- Sample 24 questions (1/2)

LLMs: grok-4, gpt-5.2, claude-opus-4.5, deepseek-v3.2
"""

from api_config import init_clients
from question_generation import run_exp1, run_exp2
from sampling import sample_exp1, sample_exp2
from prompt_utils import get_bloom
import constants


def main():
    print("=" * 60)
    print("Question Generation Experiments")
    print("=" * 60)
    print(f"LLMs: {', '.join(constants.LLM_NAMES)}")
    print(f"Layers: {len(constants.LAYERS)} OSI layers")
    print(f"Question Types: MCQ (3-step), Open-Ended")
    print("=" * 60)

    print("\n[INFO] Initializing LLM clients...")
    try:
        clients = init_clients()
    except ValueError as e:
        print(f"[ERROR] Failed to initialize clients: {e}")
        print("[ERROR] Please ensure your .env file contains:")
        print(
            "        ANTHROPIC_API_KEY, OPENAI_API_KEY, DEEPSEEK_API_KEY, XAI_API_KEY"
        )
        return

    print("\n[INFO] Pre-loading Bloom's Taxonomy data...")
    get_bloom()

    print("\n[INFO] Starting question generation experiments...")

    # Experiment 1: Content Fidelity
    # 4 LLMs × 7 Layers × 2 Question Types × 3 Bloom Levels = 168 questions
    run_exp1(clients)

    # Experiment 2: Bloom Alignment
    # 4 LLMs × 2 Question Types × varying Bloom Levels = 48 questions
    run_exp2(clients)

    print("\n" + "=" * 60)
    print("[INFO] All experiments completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
