import streamlit as st
from prompt_engine import generate_prompt

st.title("AI Blog Generator")

keyword = st.text_input("Enter a keyword")

if st.button("Generate Blog"):
    if keyword:
        prompt = generate_prompt(keyword)

        # Mock AI output (temporary)
        blog = f"""
        # {keyword.title()} - Complete Guide

        ## Introduction
        This blog explains everything about {keyword}.

        ## Benefits
        - Improves productivity
        - Saves time
        - Scalable solution

        ## Conclusion
        {keyword} is a powerful solution for modern businesses.

        ## FAQ
        Q1: What is {keyword}?
        A: It is an AI-based solution.

        """

        st.write(blog)
    else:
        st.warning("Please enter a keyword")