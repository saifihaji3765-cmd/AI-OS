from agents.scraper import get_target_questions
from agents.writer import generate_all_content, generate_blog
from agents.poster import process_content
from config import SYSTEM_STATS, DEBUG


# =========================
# 🧠 MAIN COMMAND SYSTEM
# =========================
def run_system(user_input="", command=""):
    """
    Command based AI system
    """

    command = command.lower().strip()

    # =========================
    # 🔵 TELEGRAM COMMAND
    # =========================
    if command == "telegram":
        posts = get_target_questions()

        if not posts:
            return [{"platform": "system", "content": "No data found"}]

        content = generate_all_content(posts, user_input)

        final = process_content([c for c in content if c["platform"] == "telegram"])

        return final


    # =========================
    # 🔴 REDDIT COMMAND
    # =========================
    elif command == "reddit":
        posts = get_target_questions()

        if not posts:
            return [{"platform": "system", "content": "No questions found"}]

        content = generate_all_content(posts, user_input)

        reddit_only = [c for c in content if c["platform"] == "reddit"]

        return process_content(reddit_only)


    # =========================
    # 🟢 QUORA COMMAND
    # =========================
    elif command == "quora":
        posts = get_target_questions()

        if not posts:
            return [{"platform": "system", "content": "No questions found"}]

        content = generate_all_content(posts, user_input)

        quora_only = [c for c in content if c["platform"] == "quora"]

        return process_content(quora_only)


    # =========================
    # 🔵 FACEBOOK COMMAND
    # =========================
    elif command == "facebook":
        posts = get_target_questions()

        if not posts:
            return [{"platform": "system", "content": "No data found"}]

        content = generate_all_content(posts, user_input)

        fb_only = [c for c in content if c["platform"] == "facebook"]

        return process_content(fb_only)


    # =========================
    # 📝 BLOG COMMAND
    # =========================
    elif command == "blog":
        if not user_input:
            return [{"platform": "system", "content": "Enter topic for blog"}]

        blog = generate_blog(user_input, user_input)

        return [{
            "platform": "blog",
            "content": blog
        }]


    # =========================
    # 📊 REPORT COMMAND
    # =========================
    elif command == "report":
        report = f"""
📊 System Report

Questions Fetched: {SYSTEM_STATS['questions_fetched']}
Answers Generated: {SYSTEM_STATS['answers_generated']}
Telegram Posts: {SYSTEM_STATS['telegram_posts']}
Manual Posts: {SYSTEM_STATS['manual_posts']}
"""

        return [{
            "platform": "report",
            "content": report.strip()
        }]


    # =========================
    # ❌ UNKNOWN COMMAND
    # =========================
    else:
        return [{
            "platform": "system",
            "content": "Invalid command (use: telegram / reddit / quora / facebook / blog / report)"
        }]
