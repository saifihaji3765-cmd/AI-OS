from agents.writer_agent import generate_post
from agents.research_agent import research_platforms


def command_response(user_input):
    """
    Command Mode
    Handle:
    - research
    - selling
    - scraping
    - platform analysis
    """

    text = user_input.lower()

    # ==================================
    # RESEARCH COMMANDS
    # ==================================

    if "research" in text or "find" in text:
        return research_platforms(user_input)

    # ==================================
    # SELLING / CONTENT COMMANDS
    # ==================================

    if "sell" in text or "post" in text:
        return generate_post(user_input)

    # ==================================
    # REDDIT / QUORA / PLATFORM COMMANDS
    # ==================================

    if (
        "reddit" in text
        or "quora" in text
        or "stack" in text
        or "hacker" in text
        or "devto" in text
    ):

        return research_platforms(user_input)

    # ==================================
    # DEFAULT
    # ==================================

    return f"""
⚡ Command detected

Your command:
{user_input}

System is ready for:
- research
- analysis
- content generation
"""
