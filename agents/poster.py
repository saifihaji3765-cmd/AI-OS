# agents/poster.py

import time
import webbrowser

# ==============================
# 🧠 POST MODES
# ==============================

MODE = "manual"   # "manual" | "browser"

# ==============================
# ✍️ POST FUNCTION
# ==============================

def post_reply(question, reply, source):
    """
    Safe posting handler
    """

    print("\n🚀 Posting Mode:", MODE)
    print("📌 Source:", source)

    if MODE == "manual":
        print("\n--- COPY THIS REPLY ---")
        print(reply)
        print("----------------------\n")
        return

    elif MODE == "browser":
        open_browser_search(question)
        print("\n👉 Page open ho gaya — reply paste kar de manually\n")


# ==============================
# 🌐 BROWSER OPEN (SMART ASSIST)
# ==============================

def open_browser_search(question):
    """
    Direct Google search open karega
    jahan tu relevant post find karke reply paste kare
    """

    query = question.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)
    time.sleep(2)
