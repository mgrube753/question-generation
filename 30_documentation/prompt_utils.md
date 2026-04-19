# [`prompt_utils.py`](../20_experiments/50_src/prompt_utils.py)

Handles loading, formatting, parsing, and caching of prompt templates and structural experiment metadata.

## Overview

A utility module using markdown-based context components (prompt templates, Bloom verbs and descriptions, plus learning objectives). It parses text files to extract structured information and provides helper functions to inject this information into the generation prompts.

## Core Functions

- **`load_prompt(prompt_path)`**
  Uses absolute or relative filenames to load markdown templates from `PROMPT_TEMPLATES_PATH`.

- **`format_prompt(template, **values)`**
  Injects values properly into string templates using `.format()`. Handles `KeyError`, indicating missing keys.

- **`parse_bloom_md(md_content)`**
  Parses formatted markdown content (by searching for specific markdown headers) into a nested dict: `{"Level": {"description": "...", "verbs": "..."}}`.

- **`get_bloom()` & `get_bloom_level_index/name`**
  Retrieves and caches Bloom's taxonomy data. Uses helpers to resolve index levels to names and vice versa using `constants.py`.
  **Returns:** The cached dictionary containing Bloom's definition.

- **`parse_learning_objectives_md(md_content)`**
  Extracting learning objectives for both experiments (`exp1`, `exp2`) by detecting specific markdown headers.

- **`get_learning_objectives()` / `get_learning_objective(experiment, layer, bloom_level)`**
  Returns objectives from `LEARNING_OBJECTIVES_FILE`. Mapping by `layer_num` for Exp 1 or by `bloom_idx` for Exp 2 to a designated string is provided.
  **Returns:** `str` The localized objective text.

## Dependencies

- **Internal:** `constants`, `file_utils.load_txt`
- **External:** `os`
