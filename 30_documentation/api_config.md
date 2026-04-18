# [`api_config.py`](../20_experiments/50_src/api_config.py)

Manages loading of API credentials and initialization of language model clients.

## Overview

Loading environment variables and securely initializing instances of various LLM clients. It includes base configurations and ensures that all required keys are available before the application is initialized.

## Core Functions

- **`load_api_keys()`**  
  Uses `dotenv` to load the `.env` file and extracts API keys for Anthropic, OpenAI, DeepSeek, and xAI. Raises a `ValueError` if any configured key is missing.  
  **Returns:** `dict` of parsed API keys.

- **`init_clients()`**  
  Instantiates the API clients using the keys obtained from `load_api_keys()`. It also configures custom URLs for non-standard endpoints (DeepSeek and xAI using the OpenAI SDK).  
  **Returns:** `dict` mapping LLM provider names (`anthropic`, `openai`, `deepseek`, `xai`) to the client objects.

## Dependencies

- **External:** `os`, `dotenv`, `anthropic`, `openai`
