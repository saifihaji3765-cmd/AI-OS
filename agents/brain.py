import time
from config import (
    MAX_POSTS_PER_RUN,
    DELAY_BETWEEN_ACTIONS,
    ENABLE_RATE_LIMIT,
    AUTO_POST_TELEGRAM,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    DEBUG
)

from agents.scraper import get_target_data
from agents.writer import generate_all_content

import requests


# =========================
# 🟣 TELEGRAM SENDER (AUTO)
# =========================
def send_to_telegram(message):
    if not AUTO_POST_TELEGRAM:
        return False

    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }

        res = requests.post(url, data=payload, timeout=10)

        return res.status_code == 200

    except Exception as e:
        if DEBUG:
            print("Telegram Error:", e)
        return False


# =========================
# 🧠 MAIN SYSTEM RUNNER
# =========================
def run_system(user_link=None):
    """
    Full system execute karega
    """

    # STEP 1: scrape data
    raw_posts = get_target_data()

    if not raw_posts:
        return []

    # STEP 2: limit control
    selected_posts = raw_posts[:MAX_POSTS_PER_RUN]

    # STEP 3: generate content
    all_content = generate_all_content(selected_posts)

    final_output = []

    # STEP 4: process each content
    for item in all_content:
        try:
            platform = item["platform"]
            content = item["content"]

            # Telegram auto post
            if platform == "telegram":
                if AUTO_POST_TELEGRAM:
                    send_to_telegram(content)

            # save for UI/manual platforms
            final_output.append(item)

            # rate limit
            if ENABLE_RATE_LIMIT:
                time.sleep(DELAY_BETWEEN_ACTIONS)

        except Exception as e:
            if DEBUG:
                print("Brain Error:", e)

    return final_output
