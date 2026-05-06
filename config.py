# ===============================
# 🔧 SYSTEM CONFIG (AI Growth Engine)
# ===============================

# 🔗 Default Product Link (agar user input me link na mile)
DEFAULT_LINK = "https://your-link.com"

# 🎯 Topics / Keywords (scraper filter ke liye)
TARGET_TOPICS = [
    "earn money",
    "online income",
    "learn skills",
    "freelancing",
    "AI tools",
    "business ideas"
]

# 📊 Posting Limits
MAX_POSTS_PER_RUN = 5   # ek run me kitne posts
DELAY_BETWEEN_ACTIONS = 5  # seconds (future scheduler)

# 🧠 Content Style
TONE = "human"   # human / aggressive
CTA_STYLE = "soft"  # soft / hard

# 🤖 Telegram Config (AUTO POST)
TELEGRAM_ENABLED = False  # True karega to auto post
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# 🔍 Debug Mode
DEBUG = True

# 📊 Report Storage (basic memory)
SYSTEM_STATS = {
    "questions_fetched": 0,
    "answers_generated": 0,
    "telegram_posts": 0,
    "manual_posts": 0
}
