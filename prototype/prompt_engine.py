from keyword_engine import generate_keywords

def generate_prompt(keyword):
    keywords = generate_keywords(keyword)

    prompt = f"""
    Write a 1200-1500 word SEO optimized blog on: "{keyword}"

    Include the following keywords naturally:
    {', '.join(keywords)}

    Requirements:
    - Catchy H1 title
    - Proper H2 and H3 headings
    - Engaging introduction
    - Bullet points for readability
    - FAQ section (for featured snippets)
    - Call-to-action (CTA)
    - Internal linking suggestions
    - Focus on Indian audience (GEO optimization)

    Ensure:
    - Human-like tone
    - SEO optimized structure
    - High readability
    """

    return prompt