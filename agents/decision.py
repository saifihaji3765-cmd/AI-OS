# agents/decision.py

import random

MAX_ACTIONS_PER_RUN = 5   # thoda increase (sell focus)

action_count = 0


def is_relevant(question):
    """
    Check karega ki question hamare product se related hai ya nahi
    """

    q = question.lower()

    keywords = [
        "earn", "money", "income",
        "learn", "start", "beginner",
        "ai", "trading", "coding", "freelancing"
    ]

    for word in keywords:
        if word in q:
            return True

    return False


def make_decision(item):
    global action_count

    question = item["question"]

    # limit control
    if action_count >= MAX_ACTIONS_PER_RUN:
        return "skip"

    # ❌ irrelevant → skip
    if not is_relevant(question):
        return "skip"

    # 🧠 human behavior (important)
    if random.random() < 0.15:
        return "skip"

    action_count += 1
    return "reply"
