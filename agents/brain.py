# agents/brain.py

import random
import re

# ==============================
# 🧠 INPUT ANALYZER
# ==============================

def analyze_user_input(user_input):
    text = user_input.lower()

    data = {
        "product": "",
        "target": "",
        "problem": ""
    }

    # target detection
    if "student" in text:
        data["target"] = "students"
    elif "beginner" in text:
        data["target"] = "beginners"
    else:
        data["target"] = "people"

    # product detection
    if "ai" in text:
        data["product"] = "AI system"
    elif "course" in text:
        data["product"] = "course"
    elif "earning" in text or "money" in text:
        data["product"] = "earning method"
    else:
        data["product"] = "online skill"

    # problem extraction (simple)
    match = re.findall(r"(earn|learn|start|make money|freelancing)", text)
    if match:
        data["problem"] = match[0]
    else:
        data["problem"] = "confusion"

    return data


# ==============================
# ✍️ POST GENERATOR
# ==============================

def generate_post(context, platform):
    product = context["product"]
    target = context["target"]
    problem = context["problem"]

    hooks = [
        f"Most {target} are stuck in this loop...",
        f"If you're a {target}, you need to read this",
        f"I wish I knew this earlier",
        f"This is why {target} fail in {problem}"
    ]

    bodies = [
        f"I see many {target} trying to {problem} but they follow random methods.",
        f"The real issue is not effort, it's lack of direction.",
        f"Without a proper system, you're just guessing."
    ]

    insights = [
        f"Once I understood the system behind {product}, everything changed.",
        f"A simple roadmap can save months of confusion.",
        f"Clarity beats motivation every time."
    ]

    ctas = [
        "If you want, I can explain how it works.",
        "Comment or DM me if you're serious.",
        "Let me know if you want the full breakdown."
    ]

    # platform tone tweak
    if platform == "reddit":
        style = "short"
    elif platform == "quora":
        style = "detailed"
    else:
        style = "simple"

    post = f"""
{random.choice(hooks)}

{random.choice(bodies)}

{random.choice(insights)}

{random.choice(ctas)}
"""

    return post.strip()


# ==============================
# 🌐 MULTI PLATFORM POSTS
# ==============================

def generate_all_posts(user_input):
    context = analyze_user_input(user_input)

    return {
        "reddit": generate_post(context, "reddit"),
        "quora": generate_post(context, "quora"),
        "facebook": generate_post(context, "facebook")
    }
