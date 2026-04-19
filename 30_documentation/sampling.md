# [`sampling.py`](../20_experiments/50_src/sampling.py)

Handles randomized selection, CSV and path restructuring, plus formatting of generated questions properly for qualitative human analysis.

## Overview

After the question generation, this module samples a specific subset (balanced distribution across LLMs and question types). It restructures question files into sampling files and automatically creates CSV templates for expert raters for analysis.

## Core Functions

### Cleaning Setup

- **`clean_directory(path, description)` / `clean_samples(exp_path)`**
  Removes existing `sampled` directories to ensure fresh files for each run. The `sampled` folder for each experiment describes a structured directory, which is unsuitable for direct human evaluation.
- **`clean_renamed_samples()`**
  Clears out the `70_sampled_questions` output folder. This folder includes sequentially renamed question files that are blinded for evaluation.

### Sampling Logic

- **`sample_questions_exp1()` & `collect_questions_exp1()`**
  Gathers all Exp 1 questions, ranomly sampling 24 questions (6 per LLM: 3 MCQ + 3 Open-Ended). Files are copied to the `sampled` folders for Exp 1 and saves the selected question set to `exp1_sampled.csv`.
- **`sample_questions_exp2()`**
  Samples 24 questions for Exp 2 with proper Bloom level coverage (levels 1-3 for MCQ, 3 random levels for Open-Ended). Files are copied to `sampled` for Exp 2 and saves them to `exp2_sampled.csv`.

### Formatting Output for Evaluation

- **`filter_question_content(content)`**
  Takes raw markdown files from question generation and strips away intermediate steps leaving only:
  1. Header (`## Multiple-Choice-Question` or `## Offene Frage`)
  2. Learning Objective (`### Lernziel`)
  3. Formulated Question (`### Formulierte Frage`)
  4. Source Text (`### Quelltext`)
- **`create_renamed_samples()`**  
  Reads sampled CSVs and generates blinded text files (`001_mcq_layer1.txt`, etc.) in `70_sampled_questions` using `filter_question_content()`.

### Evaluation Bootstrapping

- **`create_evaluation_csv(csv_path, eval_columns, n_evaluators, evaluator_prefix, exp_label)`**
  Takes a sampled CSV and generates empty rubric templates with specific columns for expert analysis.
- **`generate_expert_evaluation_csvs()`**
  Creates 3 copies of rater CSVs (one for each expert) for both experiments, stored in `60_analyses/csv/qualitative`.

## Control Flow

- **`run_sampling()`**
  The entry function. It sets the random seed, enables cleaning, generates samples for both experiments, creates blind test CSVs with rater rubrics, and prepares the `70_sampled_questions` folder for final analysis.

## Dependencies

- **Internal:** `constants`
- **External:** `os`, `random`, `shutil`, `pandas`
