def compute_skill_gap(candidate_skills, market_skills, top_n=10):
    candidate_set = set(candidate_skills)

    missing = []
    for skill, score in market_skills.items():
        if skill not in candidate_set:
            missing.append((skill, score))

    missing.sort(key=lambda x: x[1], reverse=True)
    return missing[:top_n]
