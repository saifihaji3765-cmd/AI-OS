# ===== SYSTEM CONFIG =====

# 🔗 CTA Link (main conversion link)
DEFAULT_LINK = "https://your-link.com"


# =========================
# 🔥 TELEGRAM SETTINGS (AUTO)
# =========================

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

AUTO_POST_TELEGRAM = True


# =========================
# ⚠️ SEMI-AUTO PLATFORMS
# =========================

USE_REDDIT = True
USE_QUORA = True
USE_FACEBOOK = True


# =========================
# 📊 LIMITS & CONTROL
# =========================

MAX_POSTS_PER_RUN = 5
DELAY_BETWEEN_ACTIONS = 10  # seconds

# Safety control
ENABLE_RATE_LIMIT = True


# =========================
# 🎯 TARGETING
# =========================

TARGET_SUBREDDITS = [
    "learnprogramming",
    "Entrepreneur",
    "smallbusiness"
]

TARGET_TOPICS = [
    "earn money online",
    "AI tools",
    "freelancing",
    "students income"
]


# =========================
# 🧠 AI STYLE
# =========================

TONE = "human"
CTA_STYLE = "soft"


# =========================
# 🔥 DEBUG
# =========================

DEBUG = True
