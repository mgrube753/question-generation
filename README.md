# AI for exam preparation: A good idea in higher education?

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python3.10+](https://img.shields.io/badge/python-3.10%2B-green.svg)](https://www.python.org/downloads/release/python-3100/)

This repository and its material is based on a [Bachelor thesis](https://github.com/mgrube753/bachelor-thesis) by Grube (2025, University of Rostock) and is used in the paper **"AI for exam preparation: A good idea in higher education?** (Cap, Grube, Rubach, in preparation). \
It includes the official implementation, prompts, datasets, and evaluation data for the upcoming publication.

## Overview

We present a comprehensive study to evaluate Large Language Models in generating questions (Multiple-Choice and Open-Ended). Our research is driven by the following research questions:

* **RQ1:** How effectively can LLMs be constrained to generate questions based on instructional materials?
* **RQ2:** Does the restriction to a question format influence achieving the cognitive level in generating questions?
* **RQ3:** Do the answers of the LLMs fit the generated questions?

To address these questions, our framework focuses on two main areas:

1. **Experiment 1:** Content Adherence Assessment (addressing RQ1 & RQ3)
2. **Experiment 2:** Bloom's Taxonomy Alignment (addressing RQ2 & RQ3)

Our framework supports generation, sampling, and evaluation (via blind test rating) across multiple state-of-the-art models:

* **Anthropic** Claude Opus 4.5
* **OpenAI** GPT-5.2
* **DeepSeek** V3.2 Thinking Mode
* **xAI** Grok-4

## Repository Structure

The project is modularized to separate research context, data generation, and evaluation. Detailed READMEs are provided in the respective subdirectories.

* **[`10_literature_review/`](10_literature_review/)** - Literature research and related work analysis, see the [Literature Review README](10_literature_review/README.md).
* **[`20_experiments/`](20_experiments/)** - Main directory containing the following:
  * **Generated questions** in a stuctured directory format
  * **Input data** based on the ISO-OSI model
  * **Prompts** used for stepwise generation for each question type
  * **Source code**, including evaluation notebooks
  * **Rating rubrics/guidelines** for the blind test analyses
  * **CSV tables** with all ratings of all raters for both experiments
  * **Sampled question sets** for both experiments, used for the blind test, and
  * **Workshop materials** to prepare the raters for the blind test.
  * See the [Experiments README](20_experiments/README.md) for an in-depth explanation.

* **[`40_evaluation/`](40_evaluation/)** - Qualitative evaluation files (plots and tables) for both experiments from the notebooks in [`20_experiments/50_src/`](20_experiments/50_src/).
* **[`50_archive*/`](50_archive090126/)** - Archived versions of experiment runs from early stages (soon).

## Setup & Installation

To run the codebase or evaluate the generated data, set up the Python environment:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mgrube753/question-generation.git
   cd question-generation
   ```

2. **Create a virtual environment and install dependencies (e.g., as follows):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure API Access:**
   The framework located in [`20_experiments/50_src/`](20_experiments/50_src/) depends on external LLM APIs. Ensure you configure your API keys before running the generation scripts to create new question sets.

   Set up your four environment variables (e.g., via a `.env` file):

   ```bash
   OPENAI_API_KEY="sk-..."
   ANTHROPIC_API_KEY="sk-ant-..."
   ...
   ```

## Reproducibility & Execution

For detailed instructions on how the experiments are structured, how the prompts are designed, and how to execute the Python scripts (`main.py`, `sampling.py`) properly, please refer to the comprehensive guide in **[`20_experiments/README.md`](20_experiments/README.md)**.

## Citation

If you find this work useful in your research, please consider citing our paper:

```bibtex
@inproceedings{cap2026title,
  title={...},
  author={Cap, Clemens and Rubach, Charlott and Grube, Malte},
  year={2026}
}
```
