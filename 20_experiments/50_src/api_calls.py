import time
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
    after_log,
)
import logging
from tqdm import tqdm
from constants import REQUEST_DELAY_SECONDS, LLM_MODEL_IDS, DRY_RUN


class TqdmLoggingHandler(logging.Handler):
    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
        except Exception:
            self.handleError(record)


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[TqdmLoggingHandler()],
)

RETRYABLE_EXCEPTIONS = (
    ConnectionError,
    TimeoutError,
    Exception,
)

api_retry = retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    retry=retry_if_exception_type(RETRYABLE_EXCEPTIONS),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    after=after_log(logger, logging.INFO),
)


@api_retry
def gen_with_anthropic(client, prompt_text, model_id, max_tokens):
    try:
        response = client.messages.create(
            model=model_id,
            thinking={"type": "enabled", "budget_tokens": 1800},
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=max_tokens,
        )

        # https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
        if response.stop_reason == "max_tokens":
            logger.warning(f"{model_id} ran out of tokens")
            for block in response.content:
                if block.type == "text":
                    logger.info(f"Partial output available for {model_id}")
                    return block.text
            logger.warning(f"No output available for {model_id}")
            return None

        for block in response.content:
            if block.type == "text":
                return block.text

    # https://platform.claude.com/docs/en/api/errors
    except Exception as e:
        logger.error(f"Claude API ({model_id}): {e}")
        if hasattr(e, "status_code") and e.status_code == 429:
            logger.warning(f"Rate limit hit for {model_id}, will retry...")
            raise  # Retry
        if hasattr(e, "status_code") and e.status_code in [500, 502, 503, 504]:
            logger.warning(
                f"Server error {e.status_code} for {model_id}, will retry..."
            )
            raise  # Retry
        return None


@api_retry
def gen_with_openai(client, prompt_text, model_id, max_tokens):
    try:
        response = client.responses.create(
            model=model_id,
            reasoning={"effort": "high"},
            input=[{"role": "user", "content": prompt_text}],
            max_output_tokens=max_tokens,
        )

        # Might be outdated, new website:
        # https://developers.openai.com/api/reference/resources/responses
        if (
            response.status == "incomplete"
            and response.incomplete_details.reason == "max_output_tokens"
        ):
            logger.warning(f"{model_id} ran out of tokens")
            if response.output_text:
                logger.info(f"Partial output available for {model_id}")
                return response.output_text
            else:
                logger.warning(f"{model_id} ran out of tokens during reasoning")
                return None

        return response.output_text

    # Might be outdated, new website:
    # https://developers.openai.com/api/docs/guides/error-codes
    except Exception as e:
        logger.error(f"OpenAI API ({model_id}): {e}")
        # Check for retryable errors
        if hasattr(e, "status_code") and e.status_code in [429, 500, 502, 503, 504]:
            logger.warning(
                f"Retryable error {e.status_code} for {model_id}, will retry..."
            )
            raise  # Retry
        return None


@api_retry
def gen_with_deepseek(client, prompt_text, model_id, max_tokens):
    # https://api-docs.deepseek.com/guides/thinking_mode
    # https://api-docs.deepseek.com/guides/reasoning_model
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=max_tokens,
            extra_body={"thinking": {"type": "enabled"}},
        )

        if response.choices and response.choices[0].finish_reason == "length":
            logger.warning(f"{model_id} ran out of tokens")
            if response.choices[0].message.content:
                logger.info(f"Partial output available for {model_id}")
                return response.choices[0].message.content
            else:
                logger.warning(f"{model_id} returned no content")
                return None

        if response.choices and response.choices[0].message.content:
            return response.choices[0].message.content

        logger.warning(f"{model_id} returned empty content")
        return None

    except Exception as e:
        logger.error(f"DeepSeek API ({model_id}): {e}")
        # Check for retryable errors
        if hasattr(e, "status_code") and e.status_code in [429, 500, 502, 503, 504]:
            logger.warning(
                f"Retryable error {e.status_code} for {model_id}, will retry..."
            )
            raise  # Retry
        return None


@api_retry
def gen_with_xai(client, prompt_text, model_id, max_tokens):
    try:
        response = client.responses.create(
            model=model_id,
            input=[{"role": "user", "content": prompt_text}],
            max_output_tokens=max_tokens,
        )

        # https://docs.x.ai/developers/rest-api-reference/inference/chat#chat-completions
        if (
            response.status == "incomplete"
            and response.incomplete_details.reason == "max_output_tokens"
        ):
            logger.warning(f"{model_id} ran out of tokens")
            if response.output_text:
                logger.info(f"Partial output available for {model_id}")
                return response.output_text
            else:
                logger.warning(f"{model_id} ran out of tokens during reasoning")
                return None

        return response.output_text

    # https://docs.x.ai/llms.txt
    except Exception as e:
        logger.error(f"xAI/Grok API ({model_id}): {e}")
        if hasattr(e, "status_code") and e.status_code in [429, 500, 502, 503, 504]:
            logger.warning(
                f"Retryable error {e.status_code} for {model_id}, will retry..."
            )
            raise  # Retry
        return None


def llm_generation(llm_name, clients, prompt_text, max_tokens):
    if DRY_RUN:
        logger.info(
            f"[DRY-RUN] Skipping API call for {llm_name}, returning empty content"
        )
        return " "

    client = clients.get(llm_name)
    model_id = LLM_MODEL_IDS.get(llm_name)

    if not client or not model_id:
        logger.error(f"Client or model_id not found for LLM: {llm_name}")
        return None

    result = None
    try:
        if llm_name == "anthropic":
            result = gen_with_anthropic(client, prompt_text, model_id, max_tokens)
        elif llm_name == "openai":
            result = gen_with_openai(client, prompt_text, model_id, max_tokens)
        elif llm_name == "deepseek":
            result = gen_with_deepseek(client, prompt_text, model_id, max_tokens)
        elif llm_name == "xai":
            result = gen_with_xai(client, prompt_text, model_id, max_tokens)
        else:
            logger.error(f"Unknown LLM name '{llm_name}'")
            return None

    except Exception as e:
        logger.error(f"All retry attempts failed for {llm_name}: {e}")
        return None

    time.sleep(REQUEST_DELAY_SECONDS)
    return result
