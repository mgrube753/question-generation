# Documentation

In this directory, you will find the technical documentation for the Python modules used in the generation pipeline. Each markdown file corresponds to a specific module, providing information on their functions and interactions within the pipeline. The modules are stored in the [`../20_experiments/50_src/`](../20_experiments/50_src/) directory and organized as follows:

## Structure Overview

### Core Modules

- **[`main.md`](main.md)** - Main entry point, launching the generation pipeline for both experiments.
- **[`question_generation.md`](question_generation.md)** - Logic for generating different types of questions (MCQ and Open-Ended) across various Bloom's Taxonomy levels, learning objectives, and ISO-OSI layers.

### API and Configuration

- **[`api_calls.md`](api_calls.md)** - Interactions with the LLM APIs (Anthropic, DeepSeek, OpenAI, xAI), including retry logic and error handling.
- **[`api_config.md`](api_config.md)** - Initialization of LLM clients and configuration using environment variables.
- **[`constants.md`](constants.md)** - Configuration constants used throughout the project, mostly paths and fixed parameters for generation.

### Utilities and Sampling

- **[`prompt_utils.md`](prompt_utils.md)** - Utilities for parsing prompt templates, handling learning objectives, and creating final prompts.
- **[`file_utils.md`](file_utils.md)** - File I/O utilities for reading source materials and saving generated questions.
- **[`sampling.md`](sampling.md)** - Logic for sampling generated questions for qualitative expert evaluation.
