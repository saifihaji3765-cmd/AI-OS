import requests
from config import (
    TARGET_SUBREDDITS,
    TARGET_TOPICS,
    USE_REDDIT,
    DEBUG
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (AI-OS Bot)"
}


# =========================
# 🔴 REDDIT FETCH
# =========================
def fetch_reddit(limit=10):
    posts = []

    if not USE_REDDIT:
        return posts

    for subreddit in TARGET_SUBREDDITS:
        url = f"https://www.reddit.com/r/{subreddit}/new.json?limit={limit}"

        try:
            res = requests.get(url, headers=HEADERS, timeout=10)

            if res.status_code != 200:
                continue

            data = res.json()

            for post in data["data"]["children"]:
                p = post["data"]

                posts.append({
                    "platform": "reddit",
                    "id": p.get("id"),
                    "title": p.get("title"),
                    "body": p.get("selftext", ""),
                    "url": "https://www.reddit.com" + p.get("permalink", "")
                })

        except Exception as e:
            if DEBUG:
                print("Reddit Error:", e)

    return posts


# =========================
# 🧠 FILTER LOGIC
# =========================
def filter_questions(posts):
    filtered = []

    for post in posts:
        text = (post["title"] + " " + post["body"]).lower()

        # question check
        if "?" in post["title"]:
            for keyword in TARGET_TOPICS:
                if keyword.lower() in text:
                    filtered.append(post)
                    break

    return filtered


# =========================
# 🚀 FINAL OUTPUT
# =========================
def get_target_data():
    all_data = []

    # reddit data
    reddit_posts = fetch_reddit()
    all_data.extend(reddit_posts)

    # filter
    final_data = filter_questions(all_data)

    if DEBUG:
        print(f"Total: {len(all_data)} | Filtered: {len(final_data)}")

    return final_data
