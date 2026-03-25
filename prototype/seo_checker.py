def analyze_seo(blog, keyword):
    words = blog.split()
    word_count = len(words)

    keyword_count = blog.lower().count(keyword.lower())
    keyword_density = (keyword_count / word_count) * 100 if word_count > 0 else 0

    sentences = blog.split(".")
    avg_sentence_length = word_count / len(sentences) if len(sentences) > 0 else 0

    readability = "Good" if avg_sentence_length < 20 else "Needs Improvement"

    score = 0

    # Word count scoring
    if word_count > 150:
        score += 10
    if word_count > 400:
        score += 20
    if word_count > 800:
        score += 30

    # Keyword density scoring
    if 1 <= keyword_density <= 3:
        score += 30
    elif keyword_density <= 5:
        score += 20

    # Readability scoring
    if readability == "Good":
        score += 40

    return {
        "Word Count": word_count,
        "Keyword Density (%)": round(keyword_density, 2),
        "Readability": readability,
        "SEO Score": score
    }