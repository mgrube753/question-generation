import os

BASE_PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXPERIMENTS_BASE_PATH = os.path.join(BASE_PROJECT_PATH, "20_experiments")
INPUT_SOURCES_PATH = os.path.join(EXPERIMENTS_BASE_PATH, "30_input_sources")
PROMPT_TEMPLATES_PATH = os.path.join(EXPERIMENTS_BASE_PATH, "40_prompts")
ANALYSES_PATH = os.path.join(EXPERIMENTS_BASE_PATH, "60_analyses")
EXP1_PATH = os.path.join(EXPERIMENTS_BASE_PATH, "10_exp1")
EXP2_PATH = os.path.join(EXPERIMENTS_BASE_PATH, "20_exp2")

# LLM Configuration
LLM_MODEL_IDS = {
    "anthropic": "claude-opus-4-5-20251101",
    "openai": "gpt-5.2-2025-12-11",
    "deepseek": "deepseek-reasoner",
    "xai": "grok-4-0709",
}
LLM_NAMES = list(LLM_MODEL_IDS.keys())
REQUEST_DELAY_SECONDS = 10

# Layer configuration (OSI/ISO model layers 1-7)
LAYERS = list(range(1, 8))

# Question types
QUESTION_TYPES = ["mcq", "open_ended"]

# Bloom's Taxonomy levels (ordered from lowest to highest cognitive level)
BLOOM_LEVELS_ORDERED = [
    "Remembering",
    "Understanding",
    "Applying",
    "Analyzing",
    "Evaluating",
    "Creating",
]

DEFAULT_MAX_TOKENS = 4000
MAX_TOKENS_BY_BLOOM = {
    "Remember": 4000,
    "Understand": 5000,
    "Apply": 6000,
    "Analyze": 7000,
    "Evaluate": 8000,
    "Create": 10000,
}

# MCQ questions only use Bloom levels 1-3
BLOOM_LEVELS_MCQ = BLOOM_LEVELS_ORDERED[:3]  # Remembering, Understanding, Applying

# Open-ended questions use all 6 Bloom levels
BLOOM_LEVELS_OPEN_ENDED = BLOOM_LEVELS_ORDERED  # All 6 levels

# Prompt file paths for MCQ (3-step process) and Open-Ended (2-step process)
PROMPT_MCQ_STEM = os.path.join(
    PROMPT_TEMPLATES_PATH, "experiment", "prompt_mcq_stem.md"
)
PROMPT_MCQ_KEYS = os.path.join(
    PROMPT_TEMPLATES_PATH, "experiment", "prompt_mcq_keys.md"
)
PROMPT_MCQ_DISTRACTORS = os.path.join(
    PROMPT_TEMPLATES_PATH, "experiment", "prompt_mcq_distractors.md"
)
PROMPT_OPEN_ENDED = os.path.join(
    PROMPT_TEMPLATES_PATH, "experiment", "prompt_open_ended.md"
)

PROMPT_OPEN_ENDED_QUESTION = os.path.join(
    PROMPT_TEMPLATES_PATH, "experiment", "prompt_open_ended_q.md"
)

PROMPT_OPEN_ENDED_ANSWER = os.path.join(
    PROMPT_TEMPLATES_PATH, "experiment", "prompt_open_ended_a.md"
)

BLOOM_DATA_FILE = os.path.join(PROMPT_TEMPLATES_PATH, "experiment", "bloom.md")

LEARNING_OBJECTIVES_FILE = os.path.join(
    PROMPT_TEMPLATES_PATH, "experiment", "lernziele.md"
)

# Experiment 1: Content Fidelity
EXP1_TOTAL_QUESTIONS = 56
EXP1_SAMPLE_SIZE = 24
EXP1_BLOOM_LEVELS_PER_TYPE = 3  # 3 Bloom levels per question type

# Experiment 2: Bloom Alignment
EXP2_TOTAL_QUESTIONS = 48
EXP2_SAMPLE_SIZE = 24
EXP2_MCQ_PER_BLOOM = 2  # 2 questions per Bloom level (levels 1-3) = 6 MCQ per LLM
EXP2_OPEN_ENDED_PER_BLOOM = 1  # 1 question per Bloom level (all 6) = 6 OE per LLM

RANDOM_SEED = 2026
DRY_RUN = False
GENERATE_MCQ = True
GENERATE_OPEN_ENDED = True
