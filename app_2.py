import base64
import streamlit as st
import os
import io
import pdf2image
import google.generativeai as genai
import pandas as pd
from collections import Counter
import plotly.express as px

# Configure API
genai.configure(api_key="AIzaSyDrxC5xFCB-UhmtEqU2wlzc8NqfPQl-uZU")

# Add Poppler path
os.environ['PATH'] += os.pathsep + r'C:\Program Files (x86)\poppler-24.07.0\Library\bin'

def get_gemini_response(prompt, pdf_content, input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        pdf_parts = []
        for image in images:
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            pdf_parts.append(
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
                }
            )
        return pdf_parts, first_page
    else:
        raise FileNotFoundError("No file uploaded")


def keyword_analysis(job_description, resume_text):
    # Tokenize and clean text
    job_words = [word.lower() for word in job_description.split()]
    resume_words = [word.lower() for word in resume_text.split()]
    
    # Count word frequencies
    job_word_count = Counter(job_words)
    resume_word_count = Counter(resume_words)
    
    # Compare keyword occurrences
    keywords = {word: {'job': job_word_count[word], 'resume': resume_word_count[word]}
                for word in job_word_count}
    
    # Visualization
    word_list = list(keywords.keys())
    job_freq = [keywords[word]['job'] for word in word_list]
    resume_freq = [keywords[word]['resume'] for word in word_list]

    data = {
        'Keywords': word_list,
        'Job Description Frequency': job_freq,
        'Resume Frequency': resume_freq,
    }

    df = pd.DataFrame(data)
    fig = px.bar(
        df.melt(id_vars='Keywords', var_name='Source', value_name='Frequency'),
        x='Keywords', y='Frequency', color='Source',
        title="Keyword Analysis: Job Description vs Resume",
        barmode='group'
    )
    return fig

# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>ATS Resume Analyzer</h1>", unsafe_allow_html=True)

# Sidebar for input
with st.sidebar:
    st.markdown("### Upload Resume")
    uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"], help="Limit 200MB per file")
    input_text = st.text_area("Enter Job Description:", height=150)

if uploaded_file is not None:
    pdf_content, first_page_image = input_pdf_setup(uploaded_file)
    st.sidebar.image(first_page_image, caption="Uploaded Resume - Page 1", use_column_width=True)
    st.sidebar.success("Resume uploaded successfully!", icon="✅")

# Tabs for different functionalities
tab1, tab2, tab3, tab4 = st.tabs(["Evaluation", "Percentage Match", "ATS Score Checker", "Keyword Analysis"])

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """
You are an advanced ATS (Applicant Tracking System) with expertise in analyzing resumes. 
Your task is to score the resume based on how well it aligns with the job description.
Provide a detailed score breakdown highlighting the match with job requirements, keywords used, and overall suitability.
"""

input_prompt4 = """
I am providing you with the Base64-encoded image of a resume. Please decode the image, 
extract its content using OCR capabilities, and return the extracted text in a structured format, 
preserving headings, sections, and any other key details from the resume.
"""

# Tab 1: Evaluation
with tab1:
    if st.button("Evaluate Resume"):
        if uploaded_file:
            st.markdown("<h3 style='text-align: center;'>Processing...</h3>", unsafe_allow_html=True)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.subheader("Evaluation Result")
            st.write(response)
        else:
            st.error("Please upload a resume to proceed.", icon="🚨")

# Tab 2: Percentage Match
with tab2:
    if st.button("Calculate Match"):
        if uploaded_file:
            st.markdown("<h3 style='text-align: center;'>Processing...</h3>", unsafe_allow_html=True)
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
            st.subheader("Percentage Match Result")
            st.write(response)
        else:
            st.error("Please upload a resume to proceed.", icon="🚨")

# Tab 3: ATS Score Checker
with tab3:
    if st.button("Get ATS Score"):
        if uploaded_file:
            st.markdown("<h3 style='text-align: center;'>Processing...</h3>", unsafe_allow_html=True)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.subheader("ATS Score Breakdown")
            st.write(response)
        else:
            st.error("Please upload a resume to proceed.", icon="🚨")

with tab4:
    if st.button("PDF Text"):
        if uploaded_file and input_text:
            st.markdown("<h3 style='text-align: center;'>Processing...</h3>", unsafe_allow_html=True)
            resume_string = get_gemini_response(input_prompt4, pdf_content, "")
            response = keyword_analysis(input_text, resume_string)
            st.subheader("Keyword Analysis")
            st.write(response)
        else:
            st.error("Please upload a resume and job description to proceed.", icon="🚨")


# Footer
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    footer:after {
        content: "Built by Dhairya Kataria";
        visibility: visible;
        display: block;
        position: relative;
        padding: 10px;
        top: 2px;
        color: grey;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
