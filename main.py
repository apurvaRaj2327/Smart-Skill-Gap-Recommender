from resume_parser import parse_resume
from domain_detector import detect_domain
from job_skill_intelligence import load_job_data, build_role_skill_matrix
from skill_gap_analyser import compute_skill_gap
from learning_path_recommender import build_learning_path
from dataset_selector import get_dataset_path
from skill_dictionaries.advanced_skills import ADVANCED_SKILLS


# ---------- Resume ----------
resume = parse_resume("sample_resume.pdf")

# ---------- Load all skills ----------
from skill_dictionaries.data_science import SKILL_LIST as DS_SKILLS
from skill_dictionaries.web_development import SKILL_LIST as WEB_SKILLS
from skill_dictionaries.cybersecurity import SKILL_LIST as CYBER_SKILLS

ALL_SKILLS = list(set(DS_SKILLS + WEB_SKILLS + CYBER_SKILLS))

from skill_extractor import extract_skills
candidate_skills = extract_skills(resume["clean_text"], ALL_SKILLS)

print("Extracted Skills:", candidate_skills)

# ---------- Detect Domain ----------
domain = detect_domain(candidate_skills["skills"])
print("Detected Domain:", domain)

# ---------- Job Market ----------
dataset_path = get_dataset_path(domain)
jobs = load_job_data(dataset_path, sample_size=20000)

# Build domain-aware skill demand
role_skills = build_role_skill_matrix(jobs, domain)

# ---------- Skill Gap ----------
gaps = compute_skill_gap(
    candidate_skills["skills"],
    role_skills
)

# ---------- Learning Path ----------
learning_path = build_learning_path(gaps, candidate_skills["skills"])

# ---------- Output ----------
print("\nTop Skill Gaps:")
for skill, score in gaps:
    print(f"{skill} → demand score {score}")

print("\nRecommended Learning Path:")
for step in learning_path:
    print(step["skill"], "→", step["recommended_courses"])
