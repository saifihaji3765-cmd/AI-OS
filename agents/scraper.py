import requests
from bs4 import BeautifulSoup
from config import HEADERS


def search_real_data(user_input):
    """
    Real multi-platform scraper
    """

    results = []

    query = user_input.lower()

    # =====================================
    # REDDIT
    # =====================================

    try:

        reddit_url = "https://www.reddit.com/r/learnprogramming/new.json?limit=5"

        response = requests.get(
            reddit_url,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code == 200:

            data = response.json()

            for post in data["data"]["children"]:

                title = post["data"]["title"]

                if query in title.lower() or len(query) > 2:

                    results.append(
                        f"🔴 Reddit:\n{title}"
                    )

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

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        titles = soup.select(".titleline a")

        for item in titles[:5]:

            text = item.text.strip()

            if text:

                results.append(
                    f"🟠 HackerNews:\n{text}"
                )

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

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        articles = soup.select("h2 a")

        for item in articles[:5]:

            text = item.text.strip()

            if text:

                results.append(
                    f"🟣 Dev.to:\n{text}"
                )

    except Exception:
        pass

    # =====================================
    # STACK EXCHANGE
    # =====================================

    try:

        stack_url = "https://stackoverflow.com/questions"

        response = requests.get(
            stack_url,
            headers=HEADERS,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        questions = soup.select(".s-post-summary--content-title a")

        for item in questions[:5]:

            text = item.text.strip()

            if text:

                results.append(
                    f"🔵 StackOverflow:\n{text}"
                )

    except Exception:
        pass

    # =====================================
    # NO RESULTS
    # =====================================

    if not results:

        return []

    # =====================================
    # LIMIT RESULTS
    # =====================================

    return results[:10]
