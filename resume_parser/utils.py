# resume_parser/utils.py

import os

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()

def validate_file(file_path, supported_formats):
    ext = get_file_extension(file_path)
    if ext not in supported_formats:
        raise ValueError(f"Unsupported file format: {ext}")
    return ext
