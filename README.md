# ATS-Resume-Analyzer

## 📝 Overview

The ATS Resume Analyzer is a powerful AI-driven tool designed to evaluate resumes against job descriptions. This Streamlit-based web app uses Google's Gemini AI, OCR, NLP, and visualization techniques to assess resumes for ATS (Applicant Tracking System) compatibility, keyword match, and overall suitability.

## 🚀 Features

✅ Resume Evaluation: Provides a professional HR-like review of the resume.

✅ Percentage Match: Calculates how well a resume aligns with a job description.

✅ ATS Score Checker: Analyzes ATS-friendliness based on structure, keywords, and formatting.

✅ Keyword Analysis: Compares job description and resume keywords using bar charts.

✅ PDF to Text Extraction: Converts resume PDFs into text for further analysis.

## 🔧 How It Works

User Uploads Resume (PDF format only).

Gemini AI Processes Resume: Converts PDF into images, extracts content using OCR, and evaluates it.

AI-Powered Analysis:

Matches job descriptions and resumes.

Scores based on ATS best practices.

Identifies missing keywords and key skills.

Data Visualization: Uses Plotly to compare keyword frequency between resume and job description.

## 🛠 Technologies Used

🖥 Streamlit (Frontend)

🤖 Google Gemini AI (Generative AI)

📄 pdf2image (PDF-to-Image Conversion)

🔄 Base64 Encoding (For Image Processing)

📊 NLTK & Counter (Keyword Analysis)

📈 Plotly (Data Visualization)

## 🌍 Where Can This Be Used?

👩‍💼 Job Seekers: Optimize resumes to pass ATS systems and increase hiring chances.

🏢 Recruiters & HRs: Quickly evaluate resumes against job descriptions.

📚 Career Consultants: Help clients improve their resumes with AI-driven insights.

🖥 Hiring Portals: Implement AI-based resume screening to enhance candidate filtering.

## 🤔 Why Is This Helpful?

⏳ Saves Time: Automated analysis in seconds instead of manual screening.

📈 Increases Job Interview Chances: Ensures resumes are ATS-friendly and aligned with job descriptions.

🔍 Identifies Missing Keywords: Helps applicants tailor their resumes for better visibility.

🖥 User-Friendly & Interactive: Simple upload & analyze process with clear visual feedback.

## 💻 How to Run Locally

pip install -r requirements.txt

streamlit run app.py

## 👨‍💻 Author

Built by Dhairya Kataria 🚀
