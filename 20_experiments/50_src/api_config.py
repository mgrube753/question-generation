import os
from dotenv import load_dotenv
from google import genai
import anthropic
import openai  # for OpenAI, DeepSeek and xAI


def load_api_keys():
    load_dotenv()
    keys = {
        "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "openai": os.getenv("OPENAI_API_KEY"),
        "deepseek": os.getenv("DEEPSEEK_API_KEY"),
        "xai": os.getenv("XAI_API_KEY"),
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

    anthropic_client = anthropic.Anthropic(api_key=api_keys["anthropic"])
    openai_client = openai.OpenAI(api_key=api_keys["openai"])
    deepseek_client = openai.OpenAI(api_key=api_keys["deepseek"])
    xai_client = openai.OpenAI(api_key=api_keys["xai"])

    print("[INFO] API clients initialized successfully")

    return {
        "anthropic": anthropic_client,
        "openai": openai_client,
        "deepseek": deepseek_client,
        "xai": xai_client,
    }


# def load_api_keys():
#     load_dotenv()
#     keys = {
#         "google": os.getenv("GOOGLE_API_KEY"),
#         "anthropic": os.getenv("ANTHROPIC_API_KEY"),
#         "openai": os.getenv("OPENAI_API_KEY"),
#     }
#     if not all(keys.values()):
#         missing = [k for k, v in keys.items() if not v]
#         raise ValueError(
#             f"[ERROR] Missing API keys for: {', '.join(missing)} in .env file"
#         )
#     return keys


# def init_clients():
#     api_keys = load_api_keys()

#     print("[INFO] Initializing API clients...")

#     google_client = genai.Client(api_key=api_keys["google"])
#     anthropic_client = anthropic.Anthropic(api_key=api_keys["anthropic"])
#     openai_client = openai.OpenAI(api_key=api_keys["openai"])

#     print("[INFO] API clients initialized successfully")

#     return {
#         "google": google_client,
#         "anthropic": anthropic_client,
#         "openai": openai_client,
#     }
