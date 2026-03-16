# Experiments

This directory contains the experimental framework for evaluating Large Language Model capabilities in educational question generation, focusing on content adherence assessment and Bloom's Taxonomy alignment.

## Structure Overview

### Experiment Directories

- **[`10_exp1/`](10_exp1/)** - Content Adherence Experiment
  - [`questions/`](10_exp1/questions/) - Generated questions organized by LLM and type
  - [`sampled/`](10_exp1/sampled/) - Sampled questions for expert evaluation
- **[`20_exp2/`](20_exp2/)** - Bloom's Taxonomy Alignment Experiment
  - [`questions/`](20_exp2/questions/) - Generated questions targeting specific cognitive levels
  - [`sampled/`](20_exp2/sampled/) - Sampled questions for expert evaluation

### Supporting Infrastructure

- **[`30_input_sources/`](30_input_sources/)** - Source materials (OSI layer descriptions)
- **[`40_prompts/`](40_prompts/)** - Prompt templates for generation and evaluation
- **[`50_src/`](50_src/)** - Python implementation and evaluation notebooks
- **[`60_analyses/`](60_analyses/)** - Analysis data and expert/student instructions
- **[`70_sampled_questions/`](70_sampled_questions/)** - Renamed sample collections for blind evaluation
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

## Implementation Framework

### Prompt Templates

Located in **[`40_prompts/`](40_prompts/)**:

- **[`experiment/`](40_prompts/experiment/)** - Question generation prompts
  - [`prompt_mcq_stem.md`](40_prompts/experiment/prompt_mcq_stem.md) - MCQ stem generation
  - [`prompt_mcq_keys.md`](40_prompts/experiment/prompt_mcq_keys.md) - MCQ answer key generation
  - [`prompt_mcq_distractors.md`](40_prompts/experiment/prompt_mcq_distractors.md) - MCQ distractor generation
  - [`prompt_open_ended_q.md`](40_prompts/experiment/prompt_open_ended_q.md) - Open-ended question generation
  - [`prompt_open_ended_a.md`](40_prompts/experiment/prompt_open_ended_a.md) - Open-ended answer generation
  - [`bloom.md`](40_prompts/experiment/bloom.md) - Bloom's Taxonomy definitions
  - [`lernziele.md`](40_prompts/experiment/lernziele.md) - Learning objectives

- **[`evaluation/`](40_prompts/evaluation/)** - Assessment prompts and rubrics
  - [`exp1_adherence_eval.md`](40_prompts/evaluation/exp1_adherence_eval.md) - Adherence evaluation prompt for LLMs in first experiment
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
| [`prompt_utils.py`](50_src/prompt_utils.py) | Prompt parsing and Bloom data handling |
| [`file_utils.py`](50_src/file_utils.py) | File I/O utilities |
| [`constants.py`](50_src/constants.py) | Configuration constants |
| [`sampling.py`](50_src/sampling.py) | Sample selection for manual evaluation |
| [`check_truncation.py`](50_src/check_truncation.py) | Token length validation |

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

Each level includes specific German descriptions and action verbs for each Bloom level to construct the prompts, properly parsed via [`50_src/prompt_utils.py`](50_src/prompt_utils.py) for systematic question generation targeting specific cognitive demands + question type constraints.

Moreover, learning objectives from [`40_prompts/experiment/lernziele.md`](40_prompts/experiment/lernziele.md) are integrated to guide question generation aligned with goals for each experiment.

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

<!-- ### Notebook Conversion for Documentation -->

<!-- To include the notebooks in the thesis PDF, the following command was used (at [`50_src/`](50_src/)) to convert them to Python scripts: -->

<!-- ```bash -->
<!-- jupyter nbconvert --output-dir='nb_to_py' --to script evaluation*.ipynb -->
<!-- ``` -->

<!-- These generated Python scripts in [`50_src/nb_to_py/`](50_src/nb_to_py/) are then included in the thesis PDF after compilation. -->

## Evaluation Data

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
