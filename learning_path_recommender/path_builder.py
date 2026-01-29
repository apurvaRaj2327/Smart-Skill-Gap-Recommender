# learning_path_recommender/path_builder.py

from learning_path_recommender.skill_prerequisites import SKILL_PREREQUISITES
from learning_path_recommender.course_catalog import COURSE_CATALOG

def build_learning_path(skill_gaps, candidate_skills):
    """
    skill_gaps: list of (skill, demand_score)
    candidate_skills: list of current skills
    """
    path = []

    for skill, score in skill_gaps:
        prereqs = SKILL_PREREQUISITES.get(skill, [])
        unmet_prereqs = [p for p in prereqs if p not in candidate_skills]

        path.append({
            "skill": skill,
            "priority_score": score,
            "missing_prerequisites": unmet_prereqs,
            "recommended_courses": COURSE_CATALOG.get(skill, [])
        })

    return path
