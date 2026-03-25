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
{keyword.title()} is becoming an important topic in today’s digital world. Businesses and individuals are using it to improve efficiency and achieve better results.

## What is {keyword.title()}?
{keyword.title()} refers to strategies and tools used to improve performance, productivity, and outcomes in a specific domain.

## Key Benefits of {keyword.title()}
- Improves productivity and efficiency
- Saves time and cost
- Helps in better decision making
- Enhances scalability

## How to Use {keyword.title()}
1. Understand your goals
2. Choose the right tools
3. Implement step-by-step strategy
4. Measure performance

## Related Articles
- Learn more about SEO strategies
- Explore AI content marketing tools

## Conclusion
{keyword.title()} is a powerful approach for modern businesses to stay competitive and grow efficiently.

## FAQ

Q1: What is {keyword}?
A: It is a concept or tool used to improve outcomes in a specific area.

Q2: Why is {keyword} important?
A: It helps improve efficiency, reduce cost, and increase performance.
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