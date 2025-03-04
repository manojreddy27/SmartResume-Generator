import streamlit as st
import google.generativeai as genai
import json
import pdfkit
from io import BytesIO

# Set up Google API Key
GOOGLE_API_KEY = "your-google-api-key-here"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate a resume based on user inputs
def generate_resume(name, email, phone, experience, skills, education, career_goal, scenario):
    prompt = f"""
    Generate a professional, ATS-friendly resume for the following details:
    Name: {name}
    Email: {email}
    Phone: {phone}
    Experience: {experience}
    Skills: {skills}
    Education: {education}
    Career Goal: {career_goal}
    Scenario: {scenario}
    Ensure the resume is well-structured, formatted, and concise.
    """
    
    response = genai.generate_text(prompt)
    return response.result.strip()

# Function to convert resume text to PDF
def convert_to_pdf(resume_text):
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8'
    }
    pdf_data = pdfkit.from_string(resume_text, False, options=options)
    return BytesIO(pdf_data)

# Streamlit UI
st.title("SmartResume Generator")
st.write("Generate customized, ATS-friendly resumes instantly!")

# User Inputs
with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    education = st.text_area("Education (Degrees, Certifications, etc.)")
    experience = st.text_area("Work Experience (Jobs, Internships, Projects, etc.)")
    skills = st.text_area("Skills")
    career_goal = st.text_area("Career Goals")
    scenario = st.selectbox("Select Scenario", [
        "University Career Services",
        "Job Placement Agencies",
        "Freelancers and Gig Workers"
    ])
    submit_button = st.form_submit_button("Generate Resume")

if submit_button:
    if all([name, email, phone, education, experience, skills, career_goal]):
        resume_text = generate_resume(name, email, phone, experience, skills, education, career_goal, scenario)
        st.subheader("Generated Resume:")
        st.text_area("", resume_text, height=400)
        
        # Convert to PDF
        pdf_file = convert_to_pdf(resume_text)
        st.download_button("Download Resume as PDF", pdf_file, f"{name}_Resume.pdf", "application/pdf")
    else:
        st.warning("Please fill out all fields before generating the resume.")
