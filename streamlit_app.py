"""
streamlit_app.py

This script creates a Streamlit web application for AI-powered job search. 

Main functionalities:
1. Provides a user-friendly interface for job searches.
2. Uses a FAISS-based search function to retrieve job listings.
3. Displays AI-refined job results in a structured format.

Dependencies:
- Python 3.8+
- `streamlit`
- `query_faiss.py` (must contain the `search_jobs` function)
- `FAISS` and an integrated LLM (Gemini/OpenAI) for enhanced job search

"""

import streamlit as st
from query_faiss import search_jobs  # Import FAISS + Gemini function

# Streamlit UI Setup
st.title("🔍 AI-Powered Job Search")
st.write("Enter a job query below and get AI-refined job listings!")

#  User Input for Job Query
query = st.text_input("💼 Job Search Query:", "")

if st.button("Search Jobs"):
    if query:
        st.info("🔄 Searching for the best job matches...")

        # Call FAISS + Gemini function to retrieve AI-refined job results
        refined_results = search_jobs(query, k=10)  

        if refined_results:
            st.subheader("🎯 AI-Refined Job Listings:")

            # Split the AI response into individual job postings
            jobs = refined_results.split("\n\n")  # Assumes jobs are separated by double newlines
            
            for idx, job in enumerate(jobs, 1):
                lines = job.splitlines()
                
                if len(lines) > 1:
                    company_line = lines[0].strip()  # First line is company name
                    details = "\n".join(lines[1:])  # Remaining job details
                    
                    # Display company name in bold + "is hiring!"
                    st.markdown(f"<h3><b>{idx}. {company_line} is hiring!</b></h3>", unsafe_allow_html=True)
                    
                    # Display job details below with spacing
                    st.write(details)

                # Add a horizontal divider for clarity
                st.markdown("<hr style='border: 1px solid #ccc; margin: 20px 0;'>", unsafe_allow_html=True)
            
        else:
            st.warning("❌ No relevant jobs found.")
    else:
        st.warning("⚠️ Please enter a job query.")
