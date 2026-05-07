import requests
from bs4 import BeautifulSoup
from config import HEADERS


def research_platforms(user_input):
    """
    Real research system
    Fetches basic live data
    """

    results = []

    # =====================================
    # REDDIT SEARCH
    # =====================================

    try:

        url = "https://www.reddit.com/r/learnprogramming/new.json?limit=5"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code == 200:

            data = response.json()

            for post in data["data"]["children"]:

                title = post["data"]["title"]

                results.append(f"🔴 Reddit: {title}")

    except Exception:
        pass

    # =====================================
    # HACKER NEWS
    # =====================================

    try:

        hn_url = "https://news.ycombinator.com/"

        response = requests.get(
            hn_url,
            headers=HEADERS,
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        titles = soup.select(".titleline a")

        for item in titles[:5]:

            results.append(f"🟠 HackerNews: {item.text}")

    except Exception:
        pass

    # =====================================
    # DEV.TO
    # =====================================

    try:

        devto_url = "https://dev.to/"

        response = requests.get(
            devto_url,
            headers=HEADERS,
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.select("h2 a")

        for item in articles[:5]:

            text = item.text.strip()

            if text:
                results.append(f"🟣 Dev.to: {text}")

    except Exception:
        pass

    # =====================================
    # NO RESULTS
    # =====================================

    if not results:

        return """
❌ No live data found.

Possible reasons:
- rate limit
- internet blocked
- temporary issue
"""

    # =====================================
    # FINAL RESPONSE
    # =====================================

    final_text = "\n\n".join(results)

    return f"""
🌍 LIVE PLATFORM RESEARCH

Command:
{user_input}

=================================

{final_text}
"""
