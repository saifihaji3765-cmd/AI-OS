# agents/decision.py

import random
from config import MAX_REPLIES, DEBUG


# ==============================
# ⚙️ INTERNAL STATE
# ==============================

reply_count = 0


# ==============================
# 🧠 RELEVANCE CHECK
# ==============================

def is_relevant(question):
    q = question.lower()

    keywords = [
        "earn", "money", "income",
        "learn", "start", "beginner",
        "ai", "coding", "freelancing",
        "online", "business"
    ]

    return any(word in q for word in keywords)


# ==============================
# 🧠 DECISION FUNCTION
# ==============================

def make_decision(item):
    global reply_count

    question = item.get("question", "")
    score = item.get("score", 0)
    engagement = item.get("engagement", 0)

    # 🔒 Max reply limit
    if reply_count >= MAX_REPLIES:
        if DEBUG:
            print("⛔ Max reply limit reached")
        return "skip"

    # ❌ Not relevant
    if not is_relevant(question):
        if DEBUG:
            print("❌ Not relevant")
        return "skip"

    # ❌ Low score
    if score < 5:
        if DEBUG:
            print("❌ Low score")
        return "skip"

    # ❌ Dead engagement
    if engagement == 0:
        if DEBUG:
            print("❌ No engagement")
        return "skip"

    # 🎲 Human randomness (important)
    if random.random() < 0.15:
        if DEBUG:
            print("🎲 Random skip (human behavior)")
        return "skip"

    # ✅ Approve reply
    reply_count += 1

    if DEBUG:
        print("✅ Approved for reply")

    return "reply"
