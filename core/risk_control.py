# core/risk_control.py

import time
import random
from collections import deque
from datetime import datetime

from config import DEBUG, MIN_DELAY, MAX_DELAY


# ==============================
# ⚙️ LIMIT SETTINGS
# ==============================

MAX_ACTIONS_PER_MINUTE = 4
MAX_ACTIONS_PER_SESSION = 25

# Track last actions
action_times = deque()
total_actions = 0


# ==============================
# 🧠 TIME HELPER
# ==============================

def now():
    return time.time()


# ==============================
# 🧠 CLEAN OLD DATA
# ==============================

def clean_old_actions():
    current = now()

    while action_times and current - action_times[0] > 60:
        action_times.popleft()


# ==============================
# 🔒 MAIN RISK CHECK
# ==============================

def check_risk():
    global total_actions

    try:
        clean_old_actions()

        # ⛔ Session limit
        if total_actions >= MAX_ACTIONS_PER_SESSION:
            if DEBUG:
                print("⛔ Session limit reached")
            return False

        # ⛔ Rate limit
        if len(action_times) >= MAX_ACTIONS_PER_MINUTE:
            wait_time = random.randint(20, 40)

            if DEBUG:
                print(f"⛔ Rate limit hit → sleeping {wait_time}s")

            time.sleep(wait_time)
            return False

        # 🎲 Random delay (human behavior)
        delay = random.randint(MIN_DELAY, MAX_DELAY)

        if DEBUG:
            print(f"⏳ Human delay: {delay}s")

        time.sleep(delay)

        # ✅ Log action
        action_times.append(now())
        total_actions += 1

        return True

    except Exception as e:
        if DEBUG:
            print("❌ Risk control error:", e)

        # fail-safe → allow but slow
        time.sleep(10)
        return True
