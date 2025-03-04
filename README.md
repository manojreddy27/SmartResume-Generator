# SmartResume Generator: Customized Resumes for Every Opportunity


# Overview:

The Resume Generator project aims to develop an AI-driven tool for automating the creation of professional resumes. The objective is to build a generative model that can craft tailored resumes based on user inputs such as personal information, job experience, and career goals. By analyzing these details, the model produces well-structured resumes that effectively highlight the candidate’s skills, achievements, and qualifications. This tool streamlines the resume creation process, enabling users to generate polished and personalized resumes quickly, thereby enhancing their ability to present themselves effectively to potential employers and improve their job application success.



Scenario 1: University Career Services

A university's career services department offers a resume generator to assist students in creating polished resumes tailored to specific industries. Students input details such as their academic achievements, internships, and extracurricular activities, and the tool generates resumes highlighting the most relevant skills and experiences for fields like finance, engineering, or marketing. This service helps students stand out in competitive job markets, similar to how career advisors provide tailored guidance based on individual career goals.



Scenario 2:Job Placement Agencies

A job placement agency uses the resume generator to streamline the job application process for clients. Candidates provide their work history, skills, and job preferences, and the tool produces multiple resume versions optimized for different job roles. This ensures that clients can quickly apply to various positions with resumes tailored to each opportunity, enhancing their chances of securing interviews. The approach is akin to personalized job coaching, where advisors help candidates, craft resumes for specific roles.



Scenario 3:Freelancers and Gig Workers
Freelancers and gig workers use the resume generator to create dynamic resumes that reflect their diverse project experience and skill sets. By inputting details of past projects, skills, and client testimonials, the tool generates resumes suited for different types of gigs, such as web development, graphic design, or writing. This allows freelancers to quickly customize their resumes when bidding for new projects, similar to how they might adjust their portfolios to match the needs of potential clients.

---
## Setup & Installation
### Prerequisites
- Python **3.8+**
- Google API Key for Generative AI
- Streamlit Cloud (for deployment, optional)
### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up API Key
Create a `.env` file in the project directory and add your **Google API Key**:
```plaintext
GOOGLE_API_KEY=your_google_api_key_here
```

### Run the Application Locally
```bash
streamlit run app.py
```
---
## Deployment on Streamlit Cloud

### 1. **Rename the Main File (If Necessary)**
Ensure your main script is named `app.py`.

### 2. **Create a `requirements.txt` File**
```plaintext
streamlit
google-generativeai
pdfkit
wkhtmltopdf
```

### 3. **Push Code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 4. **Deploy on Streamlit Cloud**
- Go to **Streamlit Cloud** (https://share.streamlit.io/)
- Click **New App** → Select your **GitHub Repository**
- Set the main file as `app.py`
- Add **API keys** to Streamlit secrets
- Deploy!

---
## Future Enhancements
🔹 AI-Based Resume Optimization – Integrate NLP to analyze job descriptions and suggest resume improvements for better ATS compatibility.   
🔹 User Authentication & Resume Storage – Allow users to create accounts and save multiple resume versions using Firebase or a database .
🔹 Multiple Resume Formats – Enable users to download resumes in DOCX, TXT, and JSON formats for flexibility.
