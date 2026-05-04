# agents/analyzer.py

import random
from collections import Counter

# (optional) agar tu AI API use karega future me
# from openai import OpenAI
# client = OpenAI()

# ==============================
# 🔥 1. AI KEYWORD GENERATOR
# ==============================

def generate_keywords(questions):
    """
    Questions se important keywords extract karta hai
    (basic version – later AI se upgrade karenge)
    """

    words = []

    for item in questions:
        q = item["question"].lower()

        for w in q.split():
            if len(w) > 4:  # small words ignore
                words.append(w)

    # top frequent words
    common = Counter(words).most_common(10)

    keywords = [w[0] for w in common]

    return keywords


# ==============================
# 📈 2. TREND DETECTION
# ==============================

def detect_trends(questions):
    """
    Kaunsa topic trend me hai detect karta hai
    """

    trend_map = {}

    for item in questions:
        key = item.get("keyword", "general")

        if key not in trend_map:
            trend_map[key] = 0

        trend_map[key] += item.get("engagement", 1)

    return trend_map


# ==============================
# 💰 3. PROFIT SCORING SYSTEM
# ==============================

def calculate_profit_score(question):
    """
    Question ka paisa potential calculate karta hai
    """

    q = question.lower()

    score = 0

    # 🔥 High intent keywords
    money_words = [
        "earn", "money", "income", "profit", "business",
        "freelance", "client", "job"
    ]

    # 🔥 Learning intent
    learning_words = [
        "how", "learn", "start", "beginner"
    ]

    for word in money_words:
        if word in q:
            score += 5

    for word in learning_words:
        if word in q:
            score += 3

    # randomness (real feel ke liye)
    score += random.randint(0, 3)

    return score


# ==============================
# 🧠 MAIN ANALYZER
# ==============================

def analyze_questions(questions):
    """
    Full AI analysis:
    - keywords
    - trends
    - profit score
    """

    print("🧠 Generating keywords...")

    keywords = generate_keywords(questions)

    print("🔥 Keywords:", keywords)

    trends = detect_trends(questions)

    analyzed = []

    for item in questions:
        q = item["question"]

        profit_score = calculate_profit_score(q)

        analyzed.append({
            "question": q,
            "source": item["source"],
            "engagement": item["engagement"],
            "profit_score": profit_score
        })

    # 🔥 Sort by best opportunity
    analyzed = sorted(analyzed, key=lambda x: x["profit_score"], reverse=True)

    return analyzed
