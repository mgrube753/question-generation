# [`api_calls.py`](../20_experiments/50_src/api_calls.py)

Abstraction layer sending customized prompts to multiple LLM APIs. The file manages retry and parsing logic, plus terminal-based logging.

## Overview

Wraps the SDK clients for the LLMs used. Ensures proper network-based communication by adding `tenacity` decorators that handle API errors. Outputs proper terminal-based logging. Includes the functionality to do a dry run without making actual API calls.

## Features

- **Logging:** A custom `TqdmLoggingHandler` to format logs compatibly alongside `tqdm` progress bars dynamically.

- **`@api_retry`**  
  A `tenacity` retry wrapper applied to API errors (`ConnectionError`, `TimeoutError`, `Exception`). Injects retries on 429, 500, 502, 503, 504 status codes if needed.

## Core Functions

- **`gen_with_<client>(client, prompt_text, model_id, max_tokens)`**  
  For each of the 4 LLMs, a dedicated generation function (`gen_with_<client>()`) that abstracts the API call and response parsing logic. Each function is decorated with `@api_retry` to ensure robustness against transient API issues. Furthermore, each model is set up with specific parameters (e.g., `max_tokens`, and each model's reasoning effort).

---

- **`llm_generation(llm_name, clients, prompt_text, max_tokens)`**  
  The central router for API interactions. Each `prompt_text` is routed to the designated `gen_with_<client>()` wrapper via `llm_name`.  
  **Note:** Logic is bypassed entirely using empty strings if `DRY_RUN` (see `constants.py`) is True. Delays iterations based on `REQUEST_DELAY_SECONDS`.

## Dependencies

- **Internal:** `constants`
- **External:** `time`, `logging`, `tqdm`, `tenacity`
