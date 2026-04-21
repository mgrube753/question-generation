from api_config import init_clients
from question_generation import run_exp1, run_exp2
from prompt_utils import get_bloom
import constants
import sys

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)


def main():
    print("=" * 60)
    print("Question Generation Experiments")
    print("=" * 60)
    print(f"LLMs: {', '.join(constants.LLM_NAMES)}")
    print(f"Layers: {len(constants.LAYERS)} OSI layers")
    print(f"Question Types: MCQ (3-step), Open-Ended")
    print("=" * 60)
    print("Experiment 1: 4 × 7 × 2 = 56 questions (sample 24)")
    print("Experiment 2: 4 × (6 MCQ + 6 OE) = 48 questions (sample 24)")
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

    run_exp1(clients)
    run_exp2(clients)

    print("\n" + "=" * 60)
    print("[INFO] All experiments completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
