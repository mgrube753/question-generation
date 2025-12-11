"""
Prompt Utilities for Question Generation

Provides functions for loading and formatting prompts,
as well as Bloom's Taxonomy data handling.
"""

import os
from constants import BLOOM_LEVELS_ORDERED, BLOOM_DATA_FILE, PROMPT_TEMPLATES_PATH
from file_utils import load_txt


def load_prompt(prompt_path):
    """
    Load a prompt template from a file.

    Args:
        prompt_path: Full path to the prompt file, or filename within PROMPT_TEMPLATES_PATH

    Returns:
        String content of the prompt, or None if not found
    """
    if os.path.isabs(prompt_path):
        return load_txt(prompt_path)

    # Try as relative path within prompt templates
    filename = prompt_path if prompt_path.endswith(".md") else f"{prompt_path}.md"
    path = os.path.join(PROMPT_TEMPLATES_PATH, filename)
    return load_txt(path)


def format_prompt(template, **values):
    """
    Format a prompt template with the given values.

    Args:
        template: Prompt template string with {placeholders}
        **values: Key-value pairs to substitute into the template

    Returns:
        Formatted prompt string, or original template if formatting fails
    """
    if template is None:
        return None

    # If template is empty, return empty string
    if not template.strip():
        return ""

    try:
        return template.format(**values)
    except KeyError as e:
        print(
            f"[WARNING] Missing key {e} in prompt formatting. Available keys: {list(values.keys())}"
        )
        return template


def parse_bloom_md(md_content):
    """
    Parse Bloom's Taxonomy data from markdown format.

    Expected format:
    ## Descriptions
    - LevelName: Description text

    ## Verbs
    - LevelName: verb1, verb2, verb3

    Returns:
        Dictionary with level names as keys and {description, verbs} as values
    """
    bloom_data = {
        level: {"description": "", "verbs": ""} for level in BLOOM_LEVELS_ORDERED
    }
    if not md_content:
        return bloom_data

    current_section = None
    lines = md_content.splitlines()

    for line in lines:
        line_stripped = line.strip()
        if line_stripped.startswith("## Descriptions"):
            current_section = "descriptions"
            continue
        elif line_stripped.startswith("## Verbs"):
            current_section = "verbs"
            continue

        if current_section and line_stripped.startswith("- "):
            try:
                parts = line_stripped[2:].split(":", 1)
                if len(parts) == 2:
                    level_name = parts[0].strip()
                    content = parts[1].strip()
                    if level_name in bloom_data:
                        if current_section == "descriptions":
                            bloom_data[level_name]["description"] = content
                        elif current_section == "verbs":
                            bloom_data[level_name]["verbs"] = content
            except Exception as e:
                print(
                    f"[WARNING] Could not parse Bloom data line: '{line_stripped}'. Error: {e}"
                )
    return bloom_data


# Cache for Bloom data to avoid repeated file reads
_bloom_cache = None


def get_bloom():
    """
    Get Bloom's Taxonomy data (cached).

    Returns:
        Dictionary with level names as keys and {description, verbs} as values
    """
    global _bloom_cache
    if _bloom_cache is None:
        raw = load_txt(BLOOM_DATA_FILE)
        _bloom_cache = parse_bloom_md(raw)
        print(f"[INFO] Loaded Bloom's Taxonomy data for {len(_bloom_cache)} levels")
    return _bloom_cache


def get_bloom_level_index(level_name):
    """
    Get the 1-based index for a Bloom level name.

    Args:
        level_name: Name of the Bloom level (e.g., "Remembering")

    Returns:
        Integer index (1-6) or 0 if not found
    """
    try:
        return BLOOM_LEVELS_ORDERED.index(level_name) + 1
    except ValueError:
        return 0


def get_bloom_level_name(index):
    """
    Get the Bloom level name for a 1-based index.

    Args:
        index: 1-based index (1-6)

    Returns:
        Level name string or None if invalid index
    """
    if 1 <= index <= len(BLOOM_LEVELS_ORDERED):
        return BLOOM_LEVELS_ORDERED[index - 1]
    return None
