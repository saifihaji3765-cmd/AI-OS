from agents.chat_agent import chat_response
from agents.command_agent import command_response


def process_input(user_input):
    """
    Main AI Brain
    Decide karega:
    - Chat mode
    - Command mode
    """

    text = user_input.lower()

    # =========================
    # COMMAND MODE
    # =========================
    command_keywords = [
        "reddit",
        "quora",
        "stack",
        "hacker",
        "producthunt",
        "devto",
        "sell",
        "find",
        "scrape",
        "analyze",
        "research",
        "problem",
        "question",
        "keyword"
    ]

    if any(word in text for word in command_keywords):
        return command_response(user_input)

    # =========================
    # CHAT MODE
    # =========================
    return chat_response(user_input)
