# agents/writer.py

import random
from config import DEBUG


# ==============================
# 🧠 DATA POOLS (HUMAN STYLE)
# ==============================

OPENERS = [
    "Bhai honestly bolu",
    "Simple baat hai",
    "Agar tu beginner hai",
    "Maine bhi same phase face kiya tha",
    "Ye problem bahut common hai"
]

VALUE_LINES = [
    "sabse pehle basics strong karna padta hai warna aage sab confuse hota hai",
    "log direct advanced cheezon par jump karte hain aur wahi galti hoti hai",
    "agar sahi roadmap mil jaye to learning fast ho jati hai",
    "random cheeze try karne se sirf time waste hota hai",
    "consistency + direction hi game change karta hai"
]

EXPERIENCE_LINES = [
    "maine bhi starting me kaafi time waste kiya tha",
    "mujhe bhi ye samajhne me time laga",
    "pehle mujhe koi clear direction nahi mil rahi thi",
    "trial and error me kaafi phase gaya",
    "baad me ek simple system follow kiya"
]

HOOKS = [
    "agar tu chahe to main explain kar sakta hoon kaise kaam karta hai",
    "agar interested ho to bata deta hoon step by step",
    "agar serious hai to main pura breakdown share kar sakta hoon",
    "agar chaho to main simple roadmap de dunga",
    "agar help chahiye ho to bol dena"
]


# ==============================
# 🎯 QUESTION INTENT DETECTION
# ==============================

def detect_intent(question):
    q = question.lower()

    if "earn" in q or "money" in q:
        return "money"

    if "learn" in q or "start" in q:
        return "learning"

    if "ai" in q:
        return "ai"

    return "general"


# ==============================
# ✍️ REPLY GENERATOR
# ==============================

def generate_reply(question):
    """
    High-converting human-like reply
    """

    try:
        opener = random.choice(OPENERS)
        value = random.choice(VALUE_LINES)
        exp = random.choice(EXPERIENCE_LINES)
        hook = random.choice(HOOKS)

        intent = detect_intent(question)

        # 🎯 Intent-based tweak
        if intent == "money":
            extra = "agar tu sahi approach use kare to earning start kar sakta hai"
        elif intent == "learning":
            extra = "agar tu structured tareeke se chale to fast progress karega"
        elif intent == "ai":
            extra = "AI tools sahi use kare to kaafi kaam easy ho jata hai"
        else:
            extra = "agar tu sahi direction pakad le to result milta hai"

        reply = f"{opener}, {value}. {exp} jisse mujhe clarity mili. {extra}. {hook}."

        if DEBUG:
            print("✍️ Reply generated")

        return reply

    except Exception as e:
        if DEBUG:
            print("❌ Writer error:", e)

        return "Bhai agar tu chahe to main help kar sakta hoon isme."
