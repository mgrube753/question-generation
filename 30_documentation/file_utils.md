# [`file_utils.py`](../20_experiments/50_src/file_utils.py)

Simple, reusable routines for file reading, writing, and string sanitization.

## Overview

It incapsulates common, abstracted file I/O operations and formatting utilities.

## Core Functions

- **`load_txt(file_path)`**  
  Reads text files (UTF-8). Catches missing files or access errors and prints warnings instead of crashing.  
  **Returns:** `str` (or `None` on error).

---

- **`save_result(file_path, content)`**  
  Ensures target directories exist using `os.makedirs`, and writes the payload into the given file. Prints an error if writing fails.

## Dependencies

- **External:** `os`
