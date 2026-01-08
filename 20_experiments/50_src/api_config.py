import os
from dotenv import load_dotenv
import anthropic
import openai  # for OpenAI, DeepSeek and xAI


def load_api_keys():
    load_dotenv()
    keys = {
        # "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        # "openai": os.getenv("OPENAI_API_KEY"),
        # "deepseek": os.getenv("DEEPSEEK_API_KEY"),
        # "xai": os.getenv("XAI_API_KEY"),
    }
    if not all(keys.values()):
        missing = [k for k, v in keys.items() if not v]
        raise ValueError(
            f"[ERROR] Missing API keys for: {', '.join(missing)} in .env file"
        )
    return keys


def init_clients():
    api_keys = load_api_keys()

    print("[INFO] Initializing API clients...")

    # anthropic_client = anthropic.Anthropic(api_key=api_keys["anthropic"])
    # openai_client = openai.OpenAI(api_key=api_keys["openai"])
    # deepseek_client = openai.OpenAI(
    #     api_key=api_keys["deepseek"], base_url="https://api.deepseek.com"
    # )
    # xai_client = openai.OpenAI(api_key=api_keys["xai"], base_url="https://api.x.ai/v1")

    print("[INFO] API clients initialized successfully")
    print("       - Anthropic (claude-opus-4.5)")
    print("       - OpenAI (gpt-5.2)")
    print("       - DeepSeek (deepseek-v3.2)")
    print("       - xAI (grok-4)")

    return {
        # "anthropic": anthropic_client,
        # "openai": openai_client,
        # "deepseek": deepseek_client,
        # "xai": xai_client,
    }
