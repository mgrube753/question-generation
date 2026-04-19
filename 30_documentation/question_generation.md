# [`question_generation.py`](../20_experiments/50_src/question_generation.py)

The core logic for Experiments 1 & 2 by mapping API calls to question formats.

## Overview

Coordinates the models to output Multiple-Choice Questions (MCQs) and Open-Ended questions based on Bloom's revised taxonomy. Generates output files in a structured manner while using a `ThreadPoolExecutor`. Each experimental pipeline is tracked by a progress bar and a CSV file each, from which the sampling for human evaluation is later drawn.

## Key Workflows

- **`run_exp1(clients)`**
  **Content Fidelity:** 56 question generation runs are conducted (4 LLMs, 7 Layers, 2 question types). Selects randomly a Bloom level, and applies a certain layer of the ISO-OSI model as the source text.

- **`run_exp2(clients)`**
  **Bloom Alignment:** 48 runs (4 LLMs, 6 Bloom levels, 2 question types). Uses all 7 ISO-OSI layers for each run. Generates MCQ outputs from levels 1-3 (each is repeated) and Open-ended questions for levels 1-6.

## Core Logic & Generation

- **`generate_mcq_question(llm_name, clients, source_text, bloom... max_tokens)`**
  A strict 3-step generation via `constants.PROMPT_MCQ_STEM`, `KEYS`, and `DISTRACTORS`, each in a new conversation. Cumulatively builds responses sequentially and parses them into a 3-step Markdown file.

- **`generate_open_ended_question(...)`**
  A 2-step generation using `PROMPT_OPEN_ENDED_QUESTION` followed by `PROMPT_OPEN_ENDED_ANSWER`. Output is built sequentially and saved in a structured Markdown file for each question, as done for MCQs.

- **`generate_task(task_params)`**
  Takes parameters from the pool executor, decides output format functions via `q_type`, and captures exceptions. Saving is done by using `file_utils.save_result` while incrementing the local counter via `increment_counter(...)`.

- **`create_csvs(exp_name, headers, rows)`**
  Writes structured CSV files for both experiments, presenting row-wise data of the generated questions, including the LLM used, such as the OSI layer (Exp 1), question type, Bloom level, ...

## Utilities

- `increment_counter(llm_name)`, `reset_counters()`, `get_progress()`: Modifying parallel states using `threading.Lock()` to continuous display completion ratios for each provider.

## Dependencies

- **Internal:** `constants`, `file_utils`, `prompt_utils`, `api_calls.llm_generation`
- **External:** `os`, `csv`, `random`, `shutil`, `concurrent.futures.ThreadPoolExecutor`, `threading`, `tqdm`, `collections.defaultdict`
