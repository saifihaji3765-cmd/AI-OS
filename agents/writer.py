from config import DEFAULT_LINK, TONE, CTA_STYLE, DEBUG


# =========================
# 🧠 CORE ANSWER GENERATOR
# =========================
def generate_human_answer(question, body=""):
    """
    Human-like answer banata hai
    """
    intro = "I see many people struggling with this."
    problem = f"{question}"

    insight = "Most people try random methods and get confused."

    solution = "The right way is to follow a clear system step by step instead of guessing."

    cta = generate_cta()

    answer = f"""
{intro}

{problem}

{insight}

{solution}

{cta}
"""

    return answer.strip()


# =========================
# 🎯 CTA GENERATOR
# =========================
def generate_cta():
    """
    CTA ko soft ya direct banata hai
    """
    if CTA_STYLE == "soft":
        return f"If you want, I can share the exact system here: {DEFAULT_LINK}"
    else:
        return f"Check this now: {DEFAULT_LINK}"


# =========================
# 🔴 REDDIT FORMAT
# =========================
def format_reddit(post):
    title = post["title"]
    body = generate_human_answer(post["title"], post["body"])

    return {
        "platform": "reddit",
        "title": title,
        "content": body
    }


# =========================
# 🔵 FACEBOOK FORMAT
# =========================
def format_facebook(post):
    content = f"""
Most people are stuck in this loop...

{post['title']}

Clarity beats motivation every time.

{generate_cta()}
"""

    return {
        "platform": "facebook",
        "content": content.strip()
    }


# =========================
# 🟢 QUORA FORMAT
# =========================
def format_quora(post):
    content = generate_human_answer(post["title"], post["body"])

    return {
        "platform": "quora",
        "content": content
    }


# =========================
# 🟣 TELEGRAM FORMAT (AUTO)
# =========================
def format_telegram(post):
    content = f"""
🔥 {post['title']}

{generate_human_answer(post['title'], post['body'])}
"""

    return {
        "platform": "telegram",
        "content": content.strip()
    }


# =========================
# 🚀 MAIN FUNCTION
# =========================
def generate_all_content(posts):
    """
    Sab platforms ke liye content banata hai
    """
    results = []

    for post in posts:
        try:
            # reddit
            results.append(format_reddit(post))

            # facebook
            results.append(format_facebook(post))

            # quora
            results.append(format_quora(post))

            # telegram
            results.append(format_telegram(post))

        except Exception as e:
            if DEBUG:
                print("Writer Error:", e)

    return results
