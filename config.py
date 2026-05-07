import os
from dotenv import load_dotenv

# ==============================
# LOAD ENV VARIABLES
# ==============================
load_dotenv()

# ==============================
# APP SETTINGS
# ==============================
APP_NAME = "AI Command OS"
DEBUG = True

# ==============================
# AI SETTINGS
# ==============================
AI_MODEL = "mythos"

# Future API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MYTHOS_API_KEY = os.getenv("MYTHOS_API_KEY", "")

# ==============================
# MEMORY SETTINGS
# ==============================
MEMORY_ENABLED = True
VECTOR_DB_ENABLED = True

# ==============================
# SCRAPER SETTINGS
# ==============================
SCRAPE_LIMIT = 10
REQUEST_TIMEOUT = 10

HEADERS = {
    "User-Agent": "Mozilla/5.0 (AI Command OS)"
}

# ==============================
# TARGET PLATFORMS
# ==============================
PLATFORMS = [
    "reddit",
    "quora",
    "stackexchange",
    "hackernews",
    "indiehackers",
    "producthunt",
    "devto"
]

# ==============================
# DEFAULT CTA
# ==============================
DEFAULT_CTA = """
🚀 Built with AI Command OS
"""

# ==============================
# MEMORY FILES
# ==============================
CONVERSATION_MEMORY = "memory/conversations.json"
KNOWLEDGE_MEMORY = "memory/knowledge.json"
VECTOR_MEMORY = "memory/vector_db.json"
LOG_MEMORY = "memory/logs.json"
