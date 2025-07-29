# IMPORT LIBRARIES
import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
from pdf import extract_text_from_pdf

# CONFIGURE GOOGLE GENERATIVE AI
# Load the API key from the environment variable
# Ensure you have set the GOOGLE_API_KEY in your .env file
KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=KEY)

# Initialize the Generative Model   
# Note: Replace "gemini-1.5-flash" with the appropriate model name if needed
model=genai.GenerativeModel("gemini-1.5-flash")

# create a def function to analyze pdf and job description
def analyze_pdf_and_job_description(pdf_doc, job_description):
    if not pdf_doc or not job_description:
        return "Please provide both a PDF document and a job description."
    # Extract text from the PDF file
    pdf_text = extract_text_from_pdf(pdf_doc)
    st.write("Extracted Text from PDF successfully.")    
    # Combine the PDF text and job description
    combined_text = f"compare the resume {pdf_text} with Job Description {job_description} and get ATS score in scale of 1 to 100. Provide a detailed explanation of the score and how the resume can be improved to match the job description."
    
    
    # Generate a response using the model
    ats_score = model.generate_content(combined_text)   
    combined_text = f"compare the resume {pdf_text} with Job Description {job_description} and say am i good fit for the job or not. generate results in bullet points."
    good_fit = model.generate_content(combined_text)
    combined_text = f"compare the resume {pdf_text} with Job Description {job_description} and provide SWOT analysis in bullet points."

    swot_analysis = model.generate_content(combined_text)
    
    combined_text = f"compare the resume {pdf_text} with Job Description {job_description} and give the probability of getting shortlisted for the job in percentage."

    probability = model.generate_content(combined_text)
    return ats_score.text+good_fit.text+swot_analysis.text+ probability.text
