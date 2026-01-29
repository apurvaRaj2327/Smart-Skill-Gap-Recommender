from resume_parser.parser import parse_pdf, parse_docx, parse_txt
from resume_parser.cleaner import clean_text
from resume_parser.utils import validate_file
from resume_parser.config import SUPPORTED_FORMATS, MIN_TEXT_LENGTH


def parse_resume(file_path):
    ext = validate_file(file_path, SUPPORTED_FORMATS)

    if ext == ".pdf":
        raw_text, pages = parse_pdf(file_path)
    elif ext == ".docx":
        raw_text, pages = parse_docx(file_path)
    elif ext == ".txt":
        raw_text, pages = parse_txt(file_path)

    if len(raw_text) < MIN_TEXT_LENGTH:
        raise ValueError("Resume text too short or unreadable.")

    cleaned_text = clean_text(raw_text)

    return {
        "raw_text": raw_text,
        "clean_text": cleaned_text,
        "metadata": {
            "file_type": ext,
            "pages": pages
        }
    }
