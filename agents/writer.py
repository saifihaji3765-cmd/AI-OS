from config import DEFAULT_CTA


def generate_post(user_input):
    """
    Human-like content generator
    """

    text = user_input.lower()

    # =====================================
    # AI / CODING POSTS
    # =====================================

    if "ai" in text or "coding" in text:

        return f"""
🚀 Learning AI + Coding right now is one of the smartest decisions.

Most students waste years consuming random content without building real skills.

The real advantage comes from:
✅ building projects
✅ solving problems
✅ learning by doing

Start small.
Stay consistent.
Build real systems.

{DEFAULT_CTA}
"""

    # =====================================
    # BUSINESS / SELLING POSTS
    # =====================================

    if "sell" in text or "business" in text:

        return f"""
🔥 Most people try to sell products.

Smart people solve problems.

If your product:
- saves time
- improves skills
- helps people grow

people will naturally become interested.

Focus on value first.
Sales come later.

{DEFAULT_CTA}
"""

    # =====================================
    # DEFAULT POST
    # =====================================

    return f"""
⚡ Human-Like AI Post

Your command:
{user_input}

This system can generate:
- business posts
- AI content
- coding content
- marketing content
- CTA based posts

{DEFAULT_CTA}
"""
