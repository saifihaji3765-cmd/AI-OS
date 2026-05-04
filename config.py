# config.py

import os

# ==============================
# 🔐 ENVIRONMENT VARIABLES LOAD
# ==============================

# Agar system me env variables set nahi hain
# to yeh fallback empty rakhega (crash nahi karega)

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "ai-growth-engine")

# ==============================
# 🔍 KEYWORDS (CORE TARGETING)
# ==============================

KEYWORDS = [
    "make money online",
    "earn money online",
    "learn coding",
    "learn python",
    "ai tools",
    "freelancing beginner",
    "how to start earning",
    "passive income ideas",
    "online business ideas"
]

# ==============================
# ⚙️ SYSTEM SETTINGS
# ==============================

# Kitne questions per run process karne hain
MAX_QUESTIONS = 20

# Delay range (risk control ke liye)
MIN_DELAY = 5
MAX_DELAY = 12

# Max replies ek run me
MAX_REPLIES = 5

# Debug mode (logs zyada print karega)
DEBUG = True


# ==============================
# 🧪 VALIDATION FUNCTION
# ==============================

def validate_config():
    """
    Check karega ki config sahi hai ya nahi
    """

    errors = []

    if not REDDIT_CLIENT_ID:
        errors.append("Missing REDDIT_CLIENT_ID")

    if not REDDIT_CLIENT_SECRET:
        errors.append("Missing REDDIT_CLIENT_SECRET")

    if errors:
        print("\n⚠️ CONFIG WARNING:")
        for err in errors:
            print(f" - {err}")
        print("👉 System limited mode me chalega (no Reddit API)\n")

    else:
        print("✅ Config loaded successfully\n")
