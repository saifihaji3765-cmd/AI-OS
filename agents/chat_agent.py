import requests


def chat_response(user_input):
    """
    Chat Mode
    General AI conversation
    """

    text = user_input.lower()

    # ===================================
    # SIMPLE BUILT-IN RESPONSES
    # ===================================

    if "hello" in text or "hi" in text:
        return """
👋 Hello!

I am your AI Command OS.

You can:
- ask coding questions
- ask business questions
- research ideas
- generate content
"""

    elif "best skill" in text:
        return """
🔥 Best Skills To Learn:

1. AI + Automation
2. Coding
3. Sales
4. Content Creation
5. Marketing

AI + coding combo is extremely powerful.
"""

    elif "python" in text:
        return """
🐍 Python is one of the best programming languages.

Used for:
- AI
- automation
- web apps
- data science
- bots
"""

    elif "ai" in text:
        return """
🧠 AI can help with:
- coding
- automation
- business
- research
- content writing
- problem solving
"""

    # ===================================
    # DEFAULT RESPONSE
    # ===================================

    return f"""
🤖 AI Response

You asked:
{user_input}

Currently basic AI mode is active.

Future upgrades:
- Mythos AI
- OpenAI
- Memory
- Live web research
"""
