def extract_skills(text, skill_list):
    found = set()
    text = text.lower()

    for skill in skill_list:
        if skill in text:
            found.add(skill)

    return {
        "skills": list(found),
        "skill_count": len(found)
    }
