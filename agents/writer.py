import re
from config import DEFAULT_LINK, CTA_STYLE, TONE, SYSTEM_STATS, DEBUG


# =========================
# 🔗 LINK EXTRACTOR
# =========================
def extract_link(text):
    match = re.search(r'(https?://\S+)', text)
    return match.group(0) if match else DEFAULT_LINK


# =========================
# 🎯 CTA GENERATOR
# =========================
def generate_cta(user_input=""):
    link = extract_link(user_input)

    if CTA_STYLE == "soft":
        return f"If you want, you can check this here: {link}"
    else:
        return f"Check this now: {link}"


# =========================
# 🧠 HUMAN ANSWER ENGINE
# =========================
def generate_human_answer(question, body="", user_input=""):
    intro_lines = [
        "I’ve seen many people struggle with this.",
        "This is actually more common than you think.",
        "A lot of beginners get stuck here."
    ]

    solution_lines = [
        "The real solution is to follow a clear and simple system.",
        "Instead of random trying, you need a structured approach.",
        "The difference comes from doing the right steps consistently."
    ]

    intro = intro_lines[hash(question) % len(intro_lines)]
    solution = solution_lines[hash(question) % len(solution_lines)]

    cta = generate_cta(user_input)

    answer = f"""
{intro}

{question}

{solution}

{cta}
"""

    SYSTEM_STATS["answers_generated"] += 1

    return answer.strip()


# =========================
# 📝 BLOG GENERATOR (SEO)
# =========================
def generate_blog(topic, user_input=""):
    link = extract_link(user_input)

    blog = f"""
# {topic.title()}

## Introduction
Many people are confused about this topic. Let's break it down in a simple way.

## Main Problem
People usually try random things and fail.

## Solution
The best way is to follow a step-by-step system and stay consistent.

## Final Tip
Focus on one thing and take action daily.

## Resource
{link}
"""

    return blog.strip()


# =========================
# 🔴 REDDIT FORMAT
# =========================
def format_reddit(post, user_input=""):
    return {
        "platform": "reddit",
        "title": post["title"],
        "content": generate_human_answer(post["title"], post["body"], user_input),
        "url": post.get("url", "")
    }


# =========================
# 🟢 QUORA FORMAT
# =========================
def format_quora(post, user_input=""):
    return {
        "platform": "quora",
        "content": generate_human_answer(post["title"], post["body"], user_input),
        "url": post.get("url", "")
    }


# =========================
# 🔵 FACEBOOK FORMAT
# =========================
def format_facebook(post, user_input=""):
    content = f"""
Most people ignore this...

{post['title']}

Clarity beats motivation.

{generate_cta(user_input)}
"""
    return {
        "platform": "facebook",
        "content": content.strip()
    }


# =========================
# 🟣 TELEGRAM FORMAT
# =========================
def format_telegram(post, user_input=""):
    content = f"""
🔥 {post['title']}

{generate_human_answer(post['title'], post['body'], user_input)}
"""
    return {
        "platform": "telegram",
        "content": content.strip()
    }


# =========================
# 🚀 MAIN FUNCTION
# =========================
def generate_all_content(posts, user_input=""):
    results = []

    for post in posts:
        try:
            results.append(format_reddit(post, user_input))
            results.append(format_quora(post, user_input))
            results.append(format_facebook(post, user_input))
            results.append(format_telegram(post, user_input))
        except Exception as e:
            if DEBUG:
                print("Writer Error:", e)

    return results
