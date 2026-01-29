from skill_dictionaries.data_science import SKILL_LIST as DS_SKILLS
from skill_dictionaries.web_development import SKILL_LIST as WEB_SKILLS
from skill_dictionaries.cybersecurity import SKILL_LIST as CYBER_SKILLS

def extract_skills_from_jd(row, domain):
    text = ""

    if domain == "cybersecurity":
        text = row.get("description", "")
        skills = CYBER_SKILLS

    elif domain == "web_development":
        text = f"{row.get('job_summary', '')} {row.get('job_skills', '')}"
        skills = WEB_SKILLS

    else:  # data_science
        text = f"{row.get('description', '')} {row.get('skills_desc', '')}"
        skills = DS_SKILLS

    text = text.lower()

    found = set()
    for skill in skills:
        if skill in text:
            found.add(skill)

    return list(found)
