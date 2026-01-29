from skill_extractor.skill_dictionary import SKILL_LIST

def extract_skills_rule_based(text):
    found_skills = set()
    for skill in SKILL_LIST:
        if f" {skill} " in f" {text} ":
            found_skills.add(skill)
    return list(found_skills)
