import streamlit as st
from prompt_engine import generate_prompt
from seo_checker import analyze_seo
from keyword_engine import generate_keywords

st.title("AI Blog Generator with SEO Analyzer")

keyword = st.text_input("Enter a keyword")

if st.button("Generate Blog"):
    if keyword:
        keywords = generate_keywords(keyword)

        st.subheader("Keyword Clusters")
        for k in keywords:
            st.write("-", k)
        prompt = generate_prompt(keyword)

        # Mock AI output
        blog = f"""
        # {keyword.title()} - Complete Guide

        ## Introduction
        This blog explains everything about {keyword}. It helps improve SEO and content strategy.

        ## Benefits
        - Improves productivity
        - Saves time
        - Helps rank on Google

        ## Conclusion
        {keyword} is essential for modern businesses.

        ## FAQ
        Q1: What is {keyword}?
        A: It is an AI-based solution.
        """

        st.subheader("Generated Blog")
        st.write(blog)

        # SEO Analysis
        seo_results = analyze_seo(blog, keyword)

        st.subheader("SEO Analysis")
        for key, value in seo_results.items():
            st.write(f"{key}: {value}")

    else:
        st.warning("Please enter a keyword")