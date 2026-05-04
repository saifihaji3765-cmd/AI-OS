# core/memory.py

import json
import os
from datetime import datetime

from config import DEBUG


# ==============================
# ⚙️ FILE SETTINGS
# ==============================

FILE_PATH = "data.json"
MAX_MEMORY = 1000   # max records


# ==============================
# 📥 LOAD MEMORY
# ==============================

def load_data():
    try:
        if not os.path.exists(FILE_PATH):
            return []

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        if DEBUG:
            print("❌ Memory load error:", e)
        return []


# ==============================
# 💾 SAVE MEMORY
# ==============================

def save_data(question, reply):
    try:
        data = load_data()

        # ❌ Duplicate check
        for item in data:
            if item["question"] == question:
                if DEBUG:
                    print("⚠️ Duplicate skipped")
                return

        # 🆕 New entry
        entry = {
            "question": question,
            "reply": reply,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data.append(entry)

        # 🧹 Limit memory size
        if len(data) > MAX_MEMORY:
            data = data[-MAX_MEMORY:]

        # 💾 Save file
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        if DEBUG:
            print("💾 Memory saved")

    except Exception as e:
        if DEBUG:
            print("❌ Memory save error:", e)


# ==============================
# 🔍 CHECK EXISTING QUESTION
# ==============================

def is_duplicate(question):
    data = load_data()

    for item in data:
        if item["question"] == question:
            return True

    return False
