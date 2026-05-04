 # agents/analyzer.py

from config import DEBUG


# ==============================
# 🧠 SCORE CALCULATION
# ==============================

def calculate_score(question, engagement):
    """
    Question ko score dega:
    jitna high score → utna valuable
    """

    q = question.lower()
    score = 0

    # 💰 Money intent (high value)
    money_keywords = [
        "earn", "money", "income", "make money",
        "passive income", "online earning"
    ]

    # 🎯 Beginner intent (easy sell)
    beginner_keywords = [
        "how", "start", "beginner", "learn",
        "guide", "step by step"
    ]

    # 🤖 AI / skill keywords
    skill_keywords = [
        "ai", "coding", "python", "freelancing",
        "business", "online work"
    ]

    # scoring
    for word in money_keywords:
        if word in q:
            score += 5

    for word in beginner_keywords:
        if word in q:
            score += 3

    for word in skill_keywords:
        if word in q:
            score += 2

    # engagement bonus
    if engagement > 50:
        score += 5
    elif engagement > 10:
        score += 3
    elif engagement > 0:
        score += 1

    return score


# ==============================
# 🧠 MAIN ANALYZER
# ==============================

def analyze_questions(questions):
    """
    Questions ko analyze + rank karega
    """

    analyzed = []

    if DEBUG:
        print("🧠 Analyzing questions...")

    for item in questions:
        try:
            question = item.get("question", "")
            engagement = item.get("engagement", 0)
            source = item.get("source", "unknown")

            score = calculate_score(question, engagement)

            analyzed.append({
                "question": question,
                "engagement": engagement,
                "source": source,
                "score": score
            })

        except Exception as e:
            if DEBUG:
                print("❌ Analyzer error:", e)
            continue

    # 🔥 Sort by score (high → low)
    analyzed.sort(key=lambda x: x["score"], reverse=True)

    if DEBUG:
        print(f"✅ Analyzed & sorted: {len(analyzed)}")

        # Top 3 preview
        print("\n🏆 Top Questions:")
        for i, item in enumerate(analyzed[:3], start=1):
            print(f"{i}. ({item['score']}) {item['question']}")

    return analyzed
