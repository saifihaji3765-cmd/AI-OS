import requests
from config import TELEGRAM_ENABLED, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, SYSTEM_STATS, DEBUG


# =========================
# 🟣 TELEGRAM AUTO POST
# =========================
def send_to_telegram(message):
    if not TELEGRAM_ENABLED:
        if DEBUG:
            print("Telegram disabled")
        return False

    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }

        res = requests.post(url, data=payload, timeout=10)

        if res.status_code == 200:
            SYSTEM_STATS["telegram_posts"] += 1
            return True
        else:
            if DEBUG:
                print("Telegram failed:", res.text)
            return False

    except Exception as e:
        if DEBUG:
            print("Telegram Error:", e)
        return False


# =========================
# 🔗 PLATFORM LINKS (SEND BUTTON)
# =========================
def get_post_link(platform):
    """
    Send button ke liye correct URL dega
    """
    if platform == "reddit":
        return "https://www.reddit.com/submit"

    elif platform == "quora":
        return "https://www.quora.com/"

    elif platform == "facebook":
        return "https://www.facebook.com/"

    else:
        return "#"


# =========================
# 🚀 PROCESS CONTENT (MAIN)
# =========================
def process_content(items):
    """
    Content ko process karega:
    - Telegram auto post
    - baaki ke liye send links attach karega
    """
    final = []

    for item in items:
        try:
            platform = item["platform"]
            content = item["content"]

            # 🟣 Telegram AUTO
            if platform == "telegram":
                send_to_telegram(content)

            # 🔗 Send button ke liye link add
            item["post_url"] = get_post_link(platform)

            final.append(item)

        except Exception as e:
            if DEBUG:
                print("Poster Error:", e)

    return final
