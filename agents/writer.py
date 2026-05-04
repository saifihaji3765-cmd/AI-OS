# agents/writer.py

import random

# ==============================
# 🧠 REPLY STYLES
# ==============================

openers = [
    "Bhai honestly bolu",
    "Simple baat hai",
    "Agar tu beginner hai",
    "Maine bhi same phase face kiya tha",
    "Ye problem bahut common hai"
]

value_lines = [
    "sabse pehle basics clear karna padta hai warna aage sab confuse hota hai",
    "log directly advance cheezon par jump karte hain aur wahi galti hoti hai",
    "agar sahi roadmap mil jaye to learning fast ho jati hai",
    "consistency aur sahi direction sabse important hoti hai",
    "random cheeze try karne se time waste hota hai"
]

experience_lines = [
    "maine bhi starting me bahut time waste kiya tha",
    "mujhe bhi ye samajhne me time laga",
    "pehle mujhe bhi koi clear direction nahi thi",
    "trial and error me kaafi time gaya",
    "baad me ek simple system follow kiya"
]

soft_hooks = [
    "agar tu chahe to main explain kar sakta hoon kaise kaam karta hai",
    "agar interested ho to bata deta hoon pura step by step",
    "agar tu serious hai to main share kar sakta hoon",
    "agar chaho to main simple breakdown de dunga",
    "agar help chahiye ho to bol dena"
]

# ==============================
# ✍️ REPLY GENERATOR
# ==============================

def generate_reply(question):
    """
    High-converting human-like reply generate karta hai
    """

    opener = random.choice(openers)
    value = random.choice(value_lines)
    exp = random.choice(experience_lines)
    hook = random.choice(soft_hooks)

    reply = f"{opener}, {value}. {exp} jisse mujhe clarity mili. {hook}."

    return reply
