from domain_role_map import DOMAIN_ROLE_KEYWORDS
from job_skill_intelligence.skill_extractor import extract_skills_from_jd

def build_role_skill_matrix(jobs, domain):
    role_keywords = DOMAIN_ROLE_KEYWORDS.get(domain, [])
    role_skill_count = {}

    for _, row in jobs.iterrows():
        title = str(row.get("job_title", "")).lower()

        # FILTER BY DOMAIN ROLES
        if not any(keyword in title for keyword in role_keywords):
            continue

        skills = extract_skills_from_jd(row, domain)

        for skill in skills:
            role_skill_count[skill] = role_skill_count.get(skill, 0) + 1

    return role_skill_count
