import streamlit as st
import random
from keyword_engine import generate_keywords
from seo_checker import analyze_seo

# -------- Context Function --------
def get_context(keyword):
    if any(word in keyword.lower() for word in ["coder", "developer", "programmer"]):
        return "person"
    elif "seo" in keyword.lower() or "marketing" in keyword.lower():
        return "marketing"
    else:
        return "general"

# -------- UI --------
st.title("AI Blog Generator with SEO Analyzer")

st.markdown("## 🚀 AI Blog Generation Workflow")
st.markdown("""
### Steps:
1. Enter Keyword  
2. Generate Keyword Clusters  
3. Create Blog  
4. Analyze SEO  
""")

st.markdown("### 💡 Try Sample Keywords:")
st.write("SEO optimization, AI tools, digital marketing, programmer, startup growth")

keyword = st.text_input("Enter a keyword")

if st.button("Generate Blog"):
    if keyword:

        st.write("🔄 Processing...")

        # -------- Keyword Clustering --------
        keywords = generate_keywords(keyword)

        st.subheader("Keyword Clusters")
        for k in keywords:
            st.write("-", k)

        st.write("✅ Keywords Generated")

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

        # -------- Dynamic Sections --------
        benefits = [
            f"Improves {keyword} efficiency",
            f"Saves time using {keyword}",
            f"Enhances {keyword} performance",
            f"Supports growth using {keyword}"
        ]

        faq_answer = random.choice([
            f"{keyword.title()} helps improve efficiency and productivity.",
            f"{keyword.title()} is widely used to solve real-world problems.",
            f"{keyword.title()} plays a crucial role in modern systems."
        ])

        extra_section = ""
        if random.choice([True, False]):
            extra_section = f"""
## Advanced Insights
{keyword.title()} is evolving rapidly and is being adopted across industries. Understanding its real-world applications can help maximize its potential.
"""

        use_case_section = ""
        if random.choice([True, False]):
            use_case_section = f"""
## Use Cases
- {keyword} in startups  
- {keyword} in enterprises  
"""

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

- {benefits[0]}  
- {benefits[1]}  
- {benefits[2]}  
- {benefits[3]}  

## How to Use {keyword.title()}

- Learn the basics  
- Practice regularly  
- Apply in real-world scenarios  

{extra_section}

{use_case_section}

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

Q1: What is {keyword.lower()}?  
A: {faq_answer}

Q2: Why is it important?  
A: It helps solve real-world problems and improves efficiency.
"""

        st.subheader("Generated Blog")
        st.write(blog)

        st.success("✅ Blog Generated Successfully!")
        st.write("✅ Blog Generated")

        # -------- Download Feature --------
        st.download_button(
            label="📥 Download Blog",
            data=blog,
            file_name=f"{keyword}_blog.txt",
            mime="text/plain"
        )

        # -------- SEO Analysis --------
        seo_results = analyze_seo(blog, keyword)

        st.write("💡 Suggestions to Improve SEO")

        if seo_results["SEO Score"] < 50:
            st.write("- Increase content length")
            st.write("- Reduce keyword repetition")
            st.write("- Improve readability")
        else:
            st.write("Your blog is well optimized!")

        st.subheader("📊 SEO Analysis Report")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Word Count", seo_results["Word Count"])
            st.metric("Keyword Density (%)", seo_results["Keyword Density (%)"])

        with col2:
            st.metric("Readability", seo_results["Readability"])
            st.metric("SEO Score", seo_results["SEO Score"])

        st.write("✅ SEO Analysis Completed")

        # -------- AI Pipeline --------
        st.markdown("## 🧠 AI Pipeline")
        st.markdown("""
Keyword Input → Keyword Clustering → Context Understanding → Blog Generation → SEO Analysis
""")

    else:
        st.warning("Please enter a keyword")