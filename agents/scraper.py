# agents/scraper.py

import random
import feedparser

from config import (
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT,
    KEYWORDS,
    MAX_QUESTIONS,
    DEBUG
)

# Reddit optional import (safe)
try:
    import praw
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    REDDIT_ENABLED = True
except:
    REDDIT_ENABLED = False


# ==============================
# 🔴 REDDIT FETCH
# ==============================

def fetch_reddit():
    results = []

    if not REDDIT_ENABLED or not REDDIT_CLIENT_ID:
        if DEBUG:
            print("⚠️ Reddit disabled (no API keys)")
        return results

    try:
        for keyword in KEYWORDS:
            posts = reddit.subreddit("all").search(keyword, limit=5)

            for post in posts:
                if "?" in post.title:
                    results.append({
                        "question": post.title,
                        "source": "reddit",
                        "engagement": post.score
                    })

    except Exception as e:
        if DEBUG:
            print("❌ Reddit Error:", e)

    return results


# ==============================
# 🟡 GOOGLE RSS FETCH
# ==============================

def fetch_google():
    results = []

    try:
        for keyword in KEYWORDS:
            url = f"https://news.google.com/rss/search?q={keyword.replace(' ', '+')}"
            feed = feedparser.parse(url)

            for entry in feed.entries[:5]:
                results.append({
                    "question": entry.title,
                    "source": "google",
                    "engagement": random.randint(1, 10)
                })

    except Exception as e:
        if DEBUG:
            print("❌ Google RSS Error:", e)

    return results


# ==============================
# 🔁 FALLBACK DATA
# ==============================

def fallback_data():
    sample = [
        "How to earn money online as a beginner?",
        "Best way to learn Python fast?",
        "Can AI help me make money?",
        "How to start freelancing with no experience?",
        "What is the best online business idea?"
    ]

    return [{
        "question": q,
        "source": "fallback",
        "engagement": random.randint(1, 10)
    } for q in sample]


# ==============================
# 🧠 MAIN FUNCTION
# ==============================

def fetch_questions():
    all_data = []

    if DEBUG:
        print("📡 Fetching data...")

    # Reddit
    reddit_data = fetch_reddit()
    all_data.extend(reddit_data)

    # Google
    google_data = fetch_google()
    all_data.extend(google_data)

    # If nothing found → fallback
    if not all_data:
        if DEBUG:
            print("⚠️ No real data → using fallback")
        all_data = fallback_data()

    # Limit questions
    all_data = all_data[:MAX_QUESTIONS]

    if DEBUG:
        print(f"✅ Total collected: {len(all_data)}")

    return all_data
