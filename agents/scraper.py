import requests
import re
from config import TARGET_TOPICS, MAX_POSTS_PER_RUN, DEBUG

HEADERS = {
    "User-Agent": "Mozilla/5.0 (AI-Growth-Engine)"
}


# =========================
# 🔴 FETCH REDDIT
# =========================
def fetch_reddit_posts(limit=50):
    url = f"https://www.reddit.com/r/all/new.json?limit={limit}"
    posts = []

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)

        if res.status_code != 200:
            if DEBUG:
                print("Reddit fetch failed:", res.status_code)
            return []

        data = res.json()

        for item in data["data"]["children"]:
            p = item["data"]

            post = {
                "platform": "reddit",
                "id": p.get("id"),
                "title": p.get("title", ""),
                "body": p.get("selftext", ""),
                "url": "https://www.reddit.com" + p.get("permalink", ""),
                "score": p.get("score", 0),
                "comments": p.get("num_comments", 0)
            }

            posts.append(post)

    except Exception as e:
        if DEBUG:
            print("Scraper Error:", e)

    return posts


# =========================
# 🧠 SMART FILTER
# =========================
def is_high_intent_question(text):
    """
    High intent identify karega
    """
    patterns = [
        r"how to",
        r"how do i",
        r"best way",
        r"what is the best",
        r"how can i",
        r"guide",
        r"tips",
        r"help",
        r"earn",
        r"make money",
        r"learn",
    ]

    return any(re.search(p, text) for p in patterns)


def filter_relevant_posts(posts):
    filtered = []

    for post in posts:
        title = post["title"].lower()
        body = post["body"].lower()
        text = title + " " + body

        # ❌ skip empty / low quality
        if len(title) < 15:
            continue

        # ❌ no question
        if "?" not in title:
            continue

        # ❌ low engagement
        if post["comments"] < 2:
            continue

        # ❌ keyword match
        if not any(keyword in text for keyword in TARGET_TOPICS):
            continue

        # ❌ high intent check
        if not is_high_intent_question(text):
            continue

        # ❌ spam words remove
        if any(bad in text for bad in ["giveaway", "free crypto", "nsfw"]):
            continue

        filtered.append(post)

    return filtered


# =========================
# 🚀 FINAL FUNCTION
# =========================
def get_target_questions():
    raw_posts = fetch_reddit_posts()

    filtered_posts = filter_relevant_posts(raw_posts)

    # 🔥 ranking (best posts first)
    sorted_posts = sorted(
        filtered_posts,
        key=lambda x: (x["comments"] + x["score"]),
        reverse=True
    )

    selected = sorted_posts[:MAX_POSTS_PER_RUN]

    if DEBUG:
        print(f"Fetched: {len(raw_posts)}")
        print(f"Filtered: {len(filtered_posts)}")
        print(f"Selected: {len(selected)}")

    return selected
