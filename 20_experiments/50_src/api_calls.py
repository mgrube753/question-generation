import time
from constants import REQUEST_DELAY_SECONDS, LLM_MODEL_IDS


def gen_with_anthropic(client, prompt_text, model_id, max_tokens):
    """Generate content using Anthropic's Claude API."""
    try:
        response = client.messages.create(
            model=model_id,
            thinking={"type": "enabled", "budget_tokens": 1100},
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=max_tokens,
        )

        if response.stop_reason == "max_tokens":
            print(f"\n[WARNING] {model_id} ran out of tokens")
            for block in response.content:
                if block.type == "text":
                    print(f"[INFO] Partial output available for {model_id}")
                    return block.text
            print(f"[WARNING] No output available for {model_id}")
            return None

        for block in response.content:
            if block.type == "text":
                return block.text
    except Exception as e:
        print(f"[ERROR] Claude API ({model_id}): {e}")
        return None


def gen_with_openai(client, prompt_text, model_id, max_tokens):
    """Generate content using OpenAI's API (gpt-5.2)."""
    try:
        response = client.responses.create(
            model=model_id,
            reasoning={"effort": "high"},
            input=[{"role": "user", "content": prompt_text}],
            max_tokens=max_tokens,
        )
        if (
            response.status == "incomplete"
            and response.incomplete_details.reason == "max_output_tokens"
        ):
            print(f"\n[WARNING] {model_id} ran out of tokens")
            if response.output_text:
                print(f"[INFO] Partial output available for {model_id}")
                return response.output_text
            else:
                print(f"[WARNING] {model_id} ran out of tokens during reasoning")
                return None

        return response.output_text

    except Exception as e:
        print(f"[ERROR] OpenAI API ({model_id}): {e}")
        return None


def gen_with_deepseek(client, prompt_text, model_id, max_tokens):
    """Generate content using DeepSeek's API (deepseek-v3.2)."""
    try:
        response = client.responses.create(
            model=model_id,
            input=[{"role": "user", "content": prompt_text}],
            max_tokens=max_tokens,
        )

        if (
            response.status == "incomplete"
            and response.incomplete_details.reason == "max_output_tokens"
        ):
            print(f"\n[WARNING] {model_id} ran out of tokens")
            if response.output_text:
                print(f"[INFO] Partial output available for {model_id}")
                return response.output_text
            else:
                print(f"[WARNING] {model_id} ran out of tokens during reasoning")
                return None

        return response.output_text
    except Exception as e:
        print(f"[ERROR] OpenAI API ({model_id}): {e}")
        return None


def gen_with_xai(client, prompt_text, model_id, max_tokens):
    """Generate content using xAI's Grok API (grok-4)."""
    try:
        response = client.responses.create(
            model=model_id,
            input=[{"role": "user", "content": prompt_text}],
            max_tokens=max_tokens,
        )

        if (
            response.status == "incomplete"
            and response.incomplete_details.reason == "max_output_tokens"
        ):
            print(f"\n[WARNING] {model_id} ran out of tokens")
            if response.output_text:
                print(f"[INFO] Partial output available for {model_id}")
                return response.output_text
            else:
                print(f"[WARNING] {model_id} ran out of tokens during reasoning")
                return None

        return response.output_text

    except Exception as e:
        print(f"[ERROR] xAI/Grok API ({model_id}): {e}")
        return None


def llm_generation(llm_name, clients, prompt_text, max_tokens):
    """
    Unified LLM generation function for all 4 providers:
    - anthropic: claude-opus-4.5
    - openai: gpt-5.2
    - deepseek: deepseek-v3.2
    - xai: grok-4
    """
    client = clients.get(llm_name)
    model_id = LLM_MODEL_IDS.get(llm_name)

    if not client or not model_id:
        print(f"[ERROR] Client or model_id not found for LLM: {llm_name}")
        return None

    result = None
    if llm_name == "anthropic":
        result = gen_with_anthropic(client, prompt_text, model_id, max_tokens)
    elif llm_name == "openai":
        result = gen_with_openai(client, prompt_text, model_id, max_tokens)
    elif llm_name == "deepseek":
        result = gen_with_deepseek(client, prompt_text, model_id, max_tokens)
    elif llm_name == "xai":
        result = gen_with_xai(client, prompt_text, model_id, max_tokens)
    else:
        print(f"[ERROR] Unknown LLM name '{llm_name}'")
        return None

    time.sleep(REQUEST_DELAY_SECONDS)
    return result
