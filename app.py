import streamlit as st
import tempfile
import os

# ---------------- Imports ----------------
from resume_parser import parse_resume
from domain_detector import detect_domain
from dataset_selector import get_dataset_path
from job_skill_intelligence import load_job_data, build_role_skill_matrix
from skill_extractor import extract_skills
from skill_gap_analyser import compute_skill_gap
from learning_path_recommender import build_learning_path
from skill_dictionaries.advanced_skills import ADVANCED_SKILLS

from skill_dictionaries.data_science import SKILL_LIST as DS_SKILLS
from skill_dictionaries.web_development import SKILL_LIST as WEB_SKILLS
from skill_dictionaries.cybersecurity import SKILL_LIST as CYBER_SKILLS

ALL_SKILLS = list(set(DS_SKILLS + WEB_SKILLS + CYBER_SKILLS))

SUPPORTED_DOMAINS = {
    "data_science",
    "web_development",
    "cybersecurity"
}

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Skill Gap Recommender",
    page_icon="🎯",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style="text-align:center;">🎯 Smart Skill Gap & Learning Path Recommender</h1>
<p style="text-align:center; font-size:18px;">
Upload your resume and get <b>market-driven insights</b> with a
<b>personalized learning roadmap</b>.
</p>
<hr>
""", unsafe_allow_html=True)

# ---------------- UPLOAD ----------------
st.subheader("📄 Upload Your Resume")
uploaded_file = st.file_uploader("PDF format only", type=["pdf"])

# ---------------- MAIN PIPELINE ----------------
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        resume_path = tmp.name

    with st.spinner("🔍 Analyzing your resume..."):
        resume = parse_resume(resume_path)
        candidate_skills = extract_skills(resume["clean_text"], ALL_SKILLS)

    # -------- SKILLS & DOMAIN --------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Extracted Skills")
        st.success(", ".join(candidate_skills["skills"]))

    domain = detect_domain(candidate_skills["skills"])

    with col2:
        st.markdown("### 🧭 Detected Domain")
        if domain == "unsupported":
            st.error("Unsupported Domain")
        else:
            st.info(domain.replace("_", " ").title())

    if domain == "unsupported":
        st.warning("""
        🚧 This resume does not match supported domains.

        **Supported Domains**
        - 📊 Data Science
        - 🌐 Web Development
        - 🔐 Cybersecurity
        """)
        os.remove(resume_path)
        st.stop()

    # -------- MARKET ANALYSIS --------
    st.markdown("---")
    st.subheader("📊 Job Market Skill Demand")

    dataset_path = get_dataset_path(domain)
    with st.spinner("Analyzing job market demand..."):
        jobs = load_job_data(dataset_path, sample_size=20000)
        market_skills = build_role_skill_matrix(jobs, domain)

    gaps = compute_skill_gap(candidate_skills["skills"], market_skills)

    # -------- ADVANCED FALLBACK --------
    if not gaps:
        st.info("🎯 You meet core market requirements. Showing **advanced career-growth skills**.")
        gaps = [
            (skill, "career_growth")
            for skill in ADVANCED_SKILLS.get(domain, [])
            if skill not in candidate_skills["skills"]
        ][:5]

    # -------- SKILL GAPS --------
    st.markdown("---")
    st.subheader("🚨 Priority Skill Gaps")

    for skill, score in gaps:
        st.markdown(
            f"""
            <div style="padding:12px; border-radius:10px; background:#f8f9fa; margin-bottom:8px;">
                <b>{skill.upper()}</b>
                <span style="float:right; color:#555;">{score}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -------- LEARNING PATH --------
    st.markdown("---")
    st.subheader("📚 Personalized Learning Path")

    learning_path = build_learning_path(gaps, candidate_skills["skills"])

    for step in learning_path:
        with st.expander(f"📌 {step['skill'].title()}"):
            if step["recommended_courses"]:
                for course in step["recommended_courses"]:
                    st.write("•", course)
            else:
                st.write("No course mapping available yet.")

    os.remove(resume_path)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Built with ❤️ using NLP, Job Market Intelligence & Streamlit</p>",
    unsafe_allow_html=True
)
