import os
from constants import BLOOM_LEVELS_ORDERED, BLOOM_DATA_FILE, PROMPT_TEMPLATES_PATH
from file_utils import load_txt


def load_prompt(prompt_path):
    if os.path.isabs(prompt_path):
        return load_txt(prompt_path)

    # Try as relative path within prompt templates
    filename = prompt_path if prompt_path.endswith(".md") else f"{prompt_path}.md"
    path = os.path.join(PROMPT_TEMPLATES_PATH, filename)
    return load_txt(path)


def format_prompt(template, **values):
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


_bloom_cache = None


def get_bloom():
    global _bloom_cache
    if _bloom_cache is None:
        raw = load_txt(BLOOM_DATA_FILE)
        _bloom_cache = parse_bloom_md(raw)
        print(f"[INFO] Loaded Bloom's Taxonomy data for {len(_bloom_cache)} levels")
    return _bloom_cache


def get_bloom_level_index(level_name):
    try:
        return BLOOM_LEVELS_ORDERED.index(level_name) + 1
    except ValueError:
        return 0


def get_bloom_level_name(index):
    if 1 <= index <= len(BLOOM_LEVELS_ORDERED):
        return BLOOM_LEVELS_ORDERED[index - 1]
    return None
