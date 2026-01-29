# skill_extractor/normalizer.py

NORMALIZATION_MAP = {
    "ml": "machine learning",
    "machine-learning": "machine learning",
    "dl": "deep learning",
    "cv": "computer vision"
}

def normalize_skills(skills):
    normalized = set()
    for skill in skills:
        skill = skill.lower().strip()
        normalized.add(NORMALIZATION_MAP.get(skill, skill))
    return list(normalized)
