# [`constants.py`](../20_experiments/50_src/constants.py)

Center of all configuration attributes, paths, hyperparameters, and structured constants for the project.

## Overview

Stores the application's configuration. By this, settings are manageable from a single source file.

## Key Configurations

### Paths

Defines the directory layout starting from the project's root:

- `BASE_PROJECT_PATH`, `EXPERIMENTS_BASE_PATH`
- Outputs & Inputs: `INPUT_SOURCES_PATH`, `PROMPT_TEMPLATES_PATH`, `ANALYSES_PATH`
- Experiment directories: `EXP1_PATH`, `EXP2_PATH`

### LLM Config

- **`LLM_MODEL_IDS`:** Dictionary mapping providers (`anthropic`, `openai`, `deepseek`, `xai`) to their exact model IDs.
- **`REQUEST_DELAY_SECONDS`:** API rate limits.

### Domain Specific

- **`LAYERS`:** List with ISO-OSI model layers 1-7.
- **`QUESTION_TYPES`:** Specifies supported types `mcq` and `open_ended`.
- **`BLOOM_LEVELS_ORDERED`:** Sequential list covering all six levels of Bloom's Taxonomy.
- **`BLOOM_LEVELS_MCQ` (1-3) & `BLOOM_LEVELS_OPEN_ENDED` (1-6):** Defines which Bloom levels are applicable for each question type.
- **`MAX_TOKENS_BY_BLOOM`:** Dictionary linking token limits per Bloom taxonomy level. To ensure proper reasoning and answering, the maximum of tokens is set to 12000 for each level.

### Prompt Templates

- **MCQ Prompts:** `PROMPT_MCQ_STEM`, `PROMPT_MCQ_KEYS`, `PROMPT_MCQ_DISTRACTORS` handle the 3-step generation for multiple-choice questions.
- **Open-Ended Prompts:** `PROMPT_OPEN_ENDED_QUESTION`, `PROMPT_OPEN_ENDED_ANSWER` provide the 2-step generation for open-ended assessment.
- **Context Files:** `BLOOM_DATA_FILE` and `LEARNING_OBJECTIVES_FILE` are crucial to inject the underlying theoretical frameworks into the prompts.

### Execution Flags

- `RANDOM_SEED`, `DRY_RUN`
- Flags to enable or disable specific generation outputs: `GENERATE_MCQ`, `GENERATE_OPEN_ENDED`.

## Dependencies

- **External:** `os`
