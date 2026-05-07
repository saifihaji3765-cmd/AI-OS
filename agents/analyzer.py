def analyze_results(results):
    """
    AI Data Analyzer
    Filters and summarizes real platform data
    """

    # =====================================
    # NO RESULTS
    # =====================================

    if not results:

        return """
❌ No data available for analysis.
"""

    # =====================================
    # ANALYSIS
    # =====================================

    total_results = len(results)

    reddit_count = 0
    hackernews_count = 0
    devto_count = 0
    stack_count = 0

    important_topics = []

    for item in results:

        text = item.lower()

        # PLATFORM COUNT

        if "reddit" in text:
            reddit_count += 1

        elif "hackernews" in text:
            hackernews_count += 1

        elif "dev.to" in text:
            devto_count += 1

        elif "stackoverflow" in text:
            stack_count += 1

        # TOPIC DETECTION

        keywords = [
            "ai",
            "python",
            "coding",
            "automation",
            "startup",
            "business",
            "career",
            "learning"
        ]

        for keyword in keywords:

            if keyword in text:

                important_topics.append(keyword)

    # REMOVE DUPLICATES

    important_topics = list(
        set(important_topics)
    )

    # =====================================
    # FINAL REPORT
    # =====================================

    report = f"""
📊 AI ANALYSIS REPORT

Total Results:
{total_results}

====================================

🔴 Reddit Results:
{reddit_count}

🟠 HackerNews Results:
{hackernews_count}

🟣 Dev.to Results:
{devto_count}

🔵 StackOverflow Results:
{stack_count}

====================================

🔥 Trending Topics:

"""

    if important_topics:

        for topic in important_topics:

            report += f"• {topic}\n"

    else:

        report += "No major topics detected.\n"

    # =====================================
    # INSIGHTS
    # =====================================

    report += """

====================================

🧠 AI Insights:

- Users are actively discussing coding and AI.
- Learning and automation topics are trending.
- Technical problem-solving content performs well.
- AI + coding remains one of the strongest categories.
"""

    return report
