# core/risk_control.py

import time
import random

# ==============================
# ⚙️ LIMIT SETTINGS
# ==============================

MAX_ACTIONS_PER_MINUTE = 3
COOLDOWN_TIME = (5, 15)  # seconds (random delay range)

# internal tracking
action_timestamps = []


# ==============================
# 🧠 RISK CHECK FUNCTION
# ==============================

def check_risk():
    """
    Decide karega system action le sakta hai ya nahi
    """

    global action_timestamps

    current_time = time.time()

    # purane timestamps remove (1 min se purane)
    action_timestamps = [
        t for t in action_timestamps if current_time - t < 60
    ]

    # limit check
    if len(action_timestamps) >= MAX_ACTIONS_PER_MINUTE:
        print("⛔ Rate limit hit. Cooling down...")
        time.sleep(random.randint(20, 40))
        return False

    # random delay (human behavior)
    delay = random.randint(*COOLDOWN_TIME)
    print(f"⏳ Waiting {delay} sec (human behavior)")
    time.sleep(delay)

    # action allowed → timestamp save
    action_timestamps.append(current_time)

    return True
