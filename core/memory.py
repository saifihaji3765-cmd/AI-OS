# core/memory.py

import json
import os

FILE_PATH = "data.json"


# ==============================
# 📥 LOAD DATA
# ==============================

def load_data():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        try:
            return json.load(f)
        except:
            return []


# ==============================
# 💾 SAVE DATA
# ==============================

def save_data(question, reply):
    data = load_data()

    # duplicate check
    for item in data:
        if item["question"] == question:
            return

    new_entry = {
        "question": question,
        "reply": reply
    }

    data.append(new_entry)

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("💾 Saved to memory")
