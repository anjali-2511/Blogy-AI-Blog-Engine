from keyword_engine import generate_keywords

def generate_prompt(keyword):
    keywords = generate_keywords(keyword)

    prompt = f"""
    Write a 1200-word SEO optimized blog on "{keyword}"

    Include keywords:
    {', '.join(keywords)}

    Use:
    - Headings (H1, H2, H3)
    - FAQs
    - CTA
    - Internal linking
    """

    return prompt