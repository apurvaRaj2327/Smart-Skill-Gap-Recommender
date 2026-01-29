import spacy
from skill_extractor.skill_dictionary import SKILL_LIST

nlp = spacy.load("en_core_web_sm")

def extract_skills_ner(text):
    doc = nlp(text)
    skills = set()

    for token in doc:
        if token.text.lower() in SKILL_LIST:
            skills.add(token.text.lower())

    return list(skills)
