# 🎯 Smart Skill Gap & Learning Path Recommender

A **multi-domain, NLP-powered recommender system** that analyzes a candidate’s resume, detects their professional domain, compares their skills with **real job-market demand**, and generates a **personalized learning roadmap**.

🚀 Live App (Streamlit):  
👉 https://YOUR_APP_NAME.streamlit.app

---

## 🔍 What This Project Does

1. 📄 Parses resumes (PDF)
2. 🧠 Extracts technical skills using NLP
3. 🧭 Detects professional domain automatically
4. 📊 Analyzes job-market demand using LinkedIn job data
5. 🚨 Identifies skill gaps
6. 📚 Recommends a personalized learning path
7. 🌐 Works as a deployed Streamlit web app

---

## 🧠 Supported Domains

- 📊 **Data Science**
- 🌐 **Web Development**
- 🔐 **Cybersecurity**

If a resume belongs to an unsupported domain, the system clearly informs the user.

---

## 🛠️ Tech Stack

- **Python**
- **spaCy (NLP)**
- **Pandas / NumPy**
- **Scikit-learn**
- **PDFMiner**
- **Streamlit**
- **Job market datasets (LinkedIn / Kaggle)**

---

## 🧩 Project Architecture


---

## 📊 How Skill Gap Is Computed

- Extracted resume skills are compared with **job-market demand frequency**
- Skills missing from the resume but highly demanded are ranked higher
- If no major gaps exist, **advanced career-growth skills** are recommended

---

## 📈 Example Output

- **Detected Domain:** Web Development  
- **Top Skill Gaps:** AWS, Docker, Angular  
- **Learning Path:** Curated courses & prerequisites per skill  
- **Visualization:** Skill-demand bar charts

---

## 🚀 How to Run Locally

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/smart-skill-gap-recommender.git
cd smart-skill-gap-recommender

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

---

## 🔧 WHAT YOU MUST EDIT (IMPORTANT)

Replace:
- `YOUR_APP_NAME`
- `YOUR_USERNAME`
- `YOUR_LINKEDIN`

Everything else is ready to go.

---

## ✅ NEXT STEPS (DO THIS NOW)

1️⃣ Create `README.md` in project root  
2️⃣ Paste the above content  
3️⃣ Commit & push:

```bash
git add README.md
git commit -m "Add professional README"
git push
