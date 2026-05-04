# agents/scraper.py

import praw
import feedparser

# ==============================
# 🔐 CONFIG (later config.py me shift karenge)
# ==============================

REDDIT_CLIENT_ID = "YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDDIT_USER_AGENT = "ai-growth-engine"

# ==============================
# 🔴 REDDIT SETUP
# ==============================

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# ==============================
# 🔴 REDDIT FETCH
# ==============================

def fetch_reddit():
    subreddits = ["learnprogramming", "Entrepreneur", "learnpython"]
    results = []

    for sub in subreddits:
        for post in reddit.subreddit(sub).hot(limit=5):
            if "?" in post.title:
                results.append({
                    "question": post.title,
                    "source": f"reddit/{sub}",
                    "engagement": post.score
                })

    return results

# ==============================
# 🟡 QUORA (RSS BASED - SAFE)
# ==============================

def fetch_quora():
    feeds = [
        "https://www.quora.com/q/python/rss",
        "https://www.quora.com/q/startups/rss"
    ]

    results = []

    for url in feeds:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            results.append({
                "question": entry.title,
                "source": "quora",
                "engagement": 10  # approx (RSS me exact nahi milta)
            })

    return results

# ==============================
# 🟢 MAIN FUNCTION
# ==============================

def fetch_questions():
    all_data = []

    try:
        reddit_data = fetch_reddit()
        all_data.extend(reddit_data)
    except Exception as e:
        print("Reddit error:", e)

    try:
        quora_data = fetch_quora()
        all_data.extend(quora_data)
    except Exception as e:
        print("Quora error:", e)

    return all_data
