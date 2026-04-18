# [`main.py`](../20_experiments/50_src/main.py)

Entry point for executing the entire experimental question generation pipeline.

## Overview

Central script for the application. It initializes the environment, and sequentially runs Experiment 1 ("Content Fidelity") and Experiment 2 ("Bloom Alignment").

## Core Functions

- **`main()`**
  1. Printing project metrics and parameters directly from `constants.py` (LLMs, Layers, Question Types).
  2. Initializes necessary language model clients via `api_config.init_clients()`. Fails if environment variables (`.env`) are missing or incorrectly configured.
  3. Pre-loads and caches unstructured markdown data into structured memory using `prompt_utils.get_bloom()`.
  4. Triggers generation for 56 parallel requests within `question_generation.run_exp1(clients)`.
  5. Triggers generation for 48 parallel requests within analogous `question_generation.run_exp2(clients)`.

## Execution Flags

- Uses `sys.stdout.reconfigure(line_buffering=True)` and `sys.stderr` buffering to ensure progress bars (`tqdm`) and asynchronous logging display properly onto the terminal.

## Dependencies

- **Internal:** `api_config.init_clients`, `question_generation.run_exp1`, `question_generation.run_exp2`, `prompt_utils.get_bloom`, `constants`
- **External:** `sys`
