import streamlit as st
from prompt_engine import generate_prompt
from seo_checker import analyze_seo
from keyword_engine import generate_keywords

# -------- Context Function --------
def get_context(keyword):
    if keyword.lower() in ["coder", "developer", "programmer"]:
        return "person"
    elif "seo" in keyword.lower() or "marketing" in keyword.lower():
        return "marketing"
    else:
        return "general"

# -------- UI --------
st.title("AI Blog Generator with SEO Analyzer")

keyword = st.text_input("Enter a keyword")

if st.button("Generate Blog"):
    if keyword:

        # -------- Keyword Clustering --------
        keywords = generate_keywords(keyword)

        st.subheader("Keyword Clusters")
        for k in keywords:
            st.write("-", k)

        # -------- Context Logic --------
        context = get_context(keyword)

        if context == "person":
            intro = f"{keyword.title()} is a professional who writes code and develops software applications."
            definition = f"A {keyword.lower()} is responsible for building, testing, and maintaining software systems."

        elif context == "marketing":
            intro = f"{keyword.title()} is a crucial strategy used in digital marketing."
            definition = f"{keyword.title()} helps improve online visibility and organic traffic."

        else:
            intro = f"{keyword.title()} is an important concept used across industries."
            definition = f"{keyword.title()} plays a key role in improving efficiency and performance."

        # -------- Blog Generation --------
        blog = f"""
# {keyword.title()} - Complete Guide

## Introduction
{intro}

## What is {keyword.title()}?
{definition}

## Why is This Concept Important?
- Plays a key role in its domain  
- Helps improve efficiency and productivity  
- Supports real-world problem solving  

## Key Benefits of This Approach
- Improves productivity  
- Saves time and effort  
- Enables better solutions  

## How to Use {keyword.title()}
- Learn the basics  
- Practice regularly  
- Apply in real-world scenarios  

## Real-World Examples
- Companies hire skilled professionals in this field  
- Startups rely on experts for product development  
- Individuals learn these skills for career growth  

## Related Articles
- Learn more about SEO strategies  
- Explore AI content marketing tools
 
## Advanced Tips
- Focus on quality over quantity  
- Keep content updated regularly  
- Analyze performance using tools   

## Conclusion
{keyword.title()} is an essential concept in its field and plays a major role in growth and innovation.

## FAQ

Q1: What is a {keyword.lower()}?
A: {definition}

Q2: Why is it important?
A: It helps solve real-world problems and improves efficiency.
"""

        st.subheader("Generated Blog")
        st.write(blog)

        # -------- SEO Analysis --------
        seo_results = analyze_seo(blog, keyword)

        st.subheader("SEO Analysis")
        for key, value in seo_results.items():
            st.write(f"{key}: {value}")

    else:
        st.warning("Please enter a keyword")