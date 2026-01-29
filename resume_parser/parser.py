# resume_parser/parser.py

import pdfplumber
import docx

def parse_pdf(file_path):
    text = ""
    pages = 0
    with pdfplumber.open(file_path) as pdf:
        pages = len(pdf.pages)
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text, pages

def parse_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text, 1

def parse_txt(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read(), 1
