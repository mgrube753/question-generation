# Experiments

This directory contains the experimental framework for evaluating Large Language Model capabilities in educational question generation. We focus on both content adherence assessment (Experiment 1) and Bloom's Taxonomy alignment (Experiment 2).

## Structure Overview

### Experiment Directories

- **[`10_exp1/`](10_exp1/)** - Content Adherence Experiment
  - [`questions/`](10_exp1/questions/) - Generated questions organized by LLM and type
  - [`sampled/`](10_exp1/sampled/) - Sampled questions for expert evaluation
- **[`20_exp2/`](20_exp2/)** - Bloom's Taxonomy Alignment Experiment
  - [`questions/`](20_exp2/questions/) - Generated questions targeting specific cognitive levels
  - [`sampled/`](20_exp2/sampled/) - Sampled questions for expert evaluation
  
Here, the `sampled/` questions are still sorted by LLM and question type in a structured directory format, not suitable for blind testing.

### Supporting Infrastructure

- **[`30_input_sources/`](30_input_sources/)** - Source materials (ISO-OSI layer descriptions)
- **[`40_prompts/`](40_prompts/)** - Prompt templates for generation + rater rubrics for evaluation
- **[`50_src/`](50_src/)** - Python implementation and evaluation notebooks
- **[`60_analyses/`](60_analyses/)** - Analysis data and expert instructions for both experiments
- **[`70_sampled_questions/`](70_sampled_questions/)** - Renamed sample collections for the raters, properly organized for blind testing and analysis
- **[`80_workshop/`](80_workshop/)** - Workshop materials and notes

## Experimental Design

### Models Used

- **Anthropic** Claude Opus 4.5
- **OpenAI** GPT-5.2
- **DeepSeek** V3.2 Thinking Mode
- **xAI** Grok-4

### Source Materials

Both experiments use extracted text from lecture materials about the ISO-OSI reference model, stored in **[`30_input_sources/`](30_input_sources/)**:

- `layer1.txt` - Physical Layer
- `layer2.txt` - Data Link Layer
- `layer3.txt` - Network Layer
- `layer4.txt` - Transport Layer
- `layer5.txt` - Session Layer
- `layer6.txt` - Presentation Layer
- `layer7.txt` - Application Layer

The second experiment used all these layers combined into a single file, `concatenated_common.txt`.

### Generation & Sampling

To ensure a balanced evaluation, we applied a the following generation and sampling procedure for the experiments across our 4 LLMs:

**Experiment 1:**

- **Generation:** 56 total questions. For each of the 7 ISO-OSI layers, we generated 1 MCQ and 1 Open-Ended OE question per LLM. A random Bloom's Taxonomy level was assigned to each question, while MCQs were primarily designed to target Bloom levels 1-3. This was done by double prompting the models for MCQs to create the same amount of questions for both types.
- **Sampling:** From the 56 generated questions, we sampled 24 questions for human evaluation (6 per LLM: 3 MCQs and 3 OE questions).

**Experiment 2:**

- **Generation:** 48 total questions, based on the complete ISO-OSI script. For Open-Ended questions, we targeted all 6 Bloom levels. For MCQs, we applied double prompting per level in this experiment as well for Bloom levels 1-3.
- **Sampling:** From the 48 generated questions, we sampled 24 questions (again 6 per LLM: 3 MCQs and 3 OE questions).

[This resource](https://teachingtools.uzh.ch/de/tools/lernziel-taxonomien) of University of Zurich shows in a tabular format which Bloom levels are suitable for which question types and how well they fit. Based on this, we designed the generation process.

## Implementation Framework

### Prompt Templates

Located in **[`40_prompts/`](40_prompts/)**:

- **[`experiment/`](40_prompts/experiment/)** - Question generation prompts
  - [`prompt_mcq_stem.md`](40_prompts/experiment/prompt_mcq_stem.md) - MCQ stem generation
  - [`prompt_mcq_keys.md`](40_prompts/experiment/prompt_mcq_keys.md) - MCQ answer key generation
  - [`prompt_mcq_distractors.md`](40_prompts/experiment/prompt_mcq_distractors.md) - MCQ distractor generation
  - [`prompt_open_ended_q.md`](40_prompts/experiment/prompt_open_ended_q.md) - Open-ended question generation
  - [`prompt_open_ended_a.md`](40_prompts/experiment/prompt_open_ended_a.md) - Open-ended answer generation
  - [`bloom.md`](40_prompts/experiment/bloom.md) - Bloom's Taxonomy verbs and definitions
  - [`learning_objectives.md`](40_prompts/experiment/learning_objectives.md) - Experiment-specific learning objectives
  
  The prompt skeletons are designed using a certain structure, including **Role**, **Task**, **Context**, **Reasoning Steps**, **Output Format**, and **Stop Conditions**. This structure is based on a mixture of two OpenAI cookbook resources:

    - <https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide>
    - <https://cookbook.openai.com/examples/gpt4-1_prompting_guide>

- **[`evaluation/`](40_prompts/evaluation/)** - Assessment prompts and rubrics
  - [`exp1_rubric.md`](40_prompts/evaluation/exp1_rubric.md) - Categories for first experiment
  - [`exp2_rubric.md`](40_prompts/evaluation/exp2_rubric.md) - Categories for second experiment

### Core Scripts

Located in **[`50_src/`](50_src/)**:

| Script | Purpose |
|--------|---------|
| [`main.py`](50_src/main.py) | Main execution entry point |
| [`question_generation.py`](50_src/question_generation.py) | Question generation logic |
| [`api_config.py`](50_src/api_config.py) | LLM client initialization |
| [`api_calls.py`](50_src/api_calls.py) | LLM API interactions |
| [`prompt_utils.py`](50_src/prompt_utils.py) | Prompt parsing and data handling |
| [`file_utils.py`](50_src/file_utils.py) | File I/O utilities |
| [`constants.py`](50_src/constants.py) | Configuration constants |
| [`sampling.py`](50_src/sampling.py) | Sample selection for qualitative evaluations |

### Evaluation Notebooks

| Notebook | Purpose |
|----------|---------|
| [`evaluation1_qual.ipynb`](50_src/evaluation1_qual.ipynb) | Experiment 1 qualitative analysis |
| [`evaluation2_qual.ipynb`](50_src/evaluation2_qual.ipynb) | Experiment 2 qualitative analysis |

## Bloom's Taxonomy Integration

The second experiment utilizes Bloom's Taxonomy, described and used via [`40_prompts/experiment/bloom.md`](40_prompts/experiment/bloom.md):

1. **Remembering**
2. **Understanding**
3. **Applying**
4. **Analyzing**
5. **Evaluating**
6. **Creating**

### Description & Verb Integration

Each level includes specific German descriptions and action verbs for each Bloom level to construct the prompts, properly parsed via [`50_src/prompt_utils.py`](50_src/prompt_utils.py). This was done for systematic question generation targeting specific cognitive demands + question type constraints.

Moreover, learning objectives from [`40_prompts/experiment/learning_objectives.md`](40_prompts/experiment/learning_objectives.md) are integrated to guide question generation aligned with goals for each experiment:

- **Experiment 1:** One learning objective for each of the 7 ISO-OSI layers
- **Experiment 2:** One learning objective for each of the 6 Bloom levels

## Usage Instructions

### Prerequisites

1. Create a `.env` file in the project root with API keys:

   ```sh
   ANTHROPIC_API_KEY=your_key
   OPENAI_API_KEY=your_key
   DEEPSEEK_API_KEY=your_key
   XAI_API_KEY=your_key
   ```

2. Install dependencies from root directory:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Experiments

All data were generated using the scripts in this directory. \
To run the Python files and the notebooks, go to the [`50_src/`](50_src/) directory and execute the following commands:

```bash
python main.py                    # Generate questions
python sampling.py                # Sample questions for manual review
```

### Running the Evaluation Notebooks

Open and execute the Jupyter notebooks in [`50_src/`](50_src/):

```bash
jupyter notebook evaluation1_qual.ipynb  # Qualitative results (Exp 1)
jupyter notebook evaluation2_qual.ipynb  # Qualitative results (Exp 2)
```

Evaluation outputs are saved to [`../40_evaluation/`](../40_evaluation/).

## Evaluation Data

### Expert Workshops

Before the actual evaluation, the `80_workshop/` directory was created. It contains materials and protocols from performed expert workshops for both experiment groups. These sessions were highly important for refining the rating criteria and analyzing the generated questions and answers.

The first phase was a preparatory session with one expert from each group (eye-to-eye) to conduct an initial review of the setup. The second phase was a joint workshop with all experts of each group to gain more insights on the experimental setup.

In this directory, you can find:

- **`info.md` & `note.md`**: To exactly understand the directory setup and gain insights on the workshop process and outcomes.
- **`initial/`**: Discussion material between the authors to prepare the two phases of both workshops.
- **`e1/` & `e2/`**: Specific reviews and notes according to Experiment 1 and Experiment 2.
- **`afterwards/`**: Post-workshop synthesis, plus `changes_on_top.md` documenting final decisions and rubric refinements agreed upon during another author discussion.

This workshop led to a new generation run for both experiments, which then formed the basis for the blind test and the subsequent qualitative evaluation.

### Expert Instructions

Instruction files for the raters are located in [`60_analyses/expert_instructions/`](60_analyses/expert_instructions/):

- [`expert_instructions_exp1.md`](60_analyses/expert_instructions/expert_instructions_exp1.md) - Guidelines for Experiment 1 experts
- [`expert_instructions_exp2.md`](60_analyses/expert_instructions/expert_instructions_exp2.md) - Guidelines for Experiment 2 experts

### Analysis Data

The raters' data were collected and stored in [`60_analyses/csv/`](60_analyses/csv/):

- `qualitative/exp1/` - Experiment 1 evaluation ratings
- `qualitative/exp2/` - Experiment 2 evaluation ratings

This data was used in the evaluation notebooks for evaluation. The resulting tables and plots are saved in [`../40_evaluation/`](../40_evaluation/) as follows:

```sh
40_evaluation/
├── exp1/
│   └── qualitative/
│       ├── plots/
│       └── tables/
└── exp2/
    └── qualitative/
        ├── plots/
        └── tables/
```
