import streamlit as st


st.title('CV Analyzer')

st.header('This page helps you analyze your CV against a job description.')

st.sidebar.subheader('Upload your CV')
pdfdoc = st.sidebar.file_uploader("click here to browse", type=["pdf"])
#pdf_doc 
st.sidebar.markdown("Designed by Gajarajan")

jobdescription = st.text_area("Enter the job description here", height=200,max_chars=10000)
# job_description

submit=st.button('Generate score')


if submit:
    with st.spinner("Analyzing..."):
        # Import the function to analyze PDF and job description
        from analysis import analyze_pdf_and_job_description
        if pdfdoc and jobdescription:
            result = analyze_pdf_and_job_description(pdfdoc, jobdescription)
            st.write(result)
        else:
            st.error("Please upload a PDF document and enter a job description.")