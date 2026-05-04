# ui/controller.py

from agents.brain import generate_all_posts
import webbrowser

def run_interface():
    print("=" * 50)
    print("🧠 AI MARKETING CONTROL PANEL")
    print("=" * 50)

    user_input = input("\n👉 Tum kya sell karna chahte ho?\n> ")

    posts = generate_all_posts(user_input)

    print("\n" + "=" * 50)
    print("📌 GENERATED POSTS")
    print("=" * 50)

    print("\n🔴 REDDIT POST:\n")
    print(posts["reddit"])

    print("\n🟢 QUORA ANSWER:\n")
    print(posts["quora"])

    print("\n🔵 FACEBOOK POST:\n")
    print(posts["facebook"])

    print("\n" + "=" * 50)

    send = input("\n👉 SEND ALL? (yes/no): ")

    if send.lower() == "yes":
        print("\n🚀 Opening platforms...\n")

        webbrowser.open("https://www.reddit.com")
        webbrowser.open("https://www.quora.com")
        webbrowser.open("https://www.facebook.com")

        print("👉 Platforms opened — paste & post")

    else:
        print("❌ Cancelled")
