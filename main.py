# main.py

from agents.scraper import fetch_questions
from agents.analyzer import analyze_questions
from agents.decision import make_decision
from agents.writer import generate_reply

from core.risk_control import check_risk
from core.memory import save_data


def run_system():
    print("🚀 AI Growth Engine Started...\n")

    # Step 1: Fetch data
    questions = fetch_questions()
    print(f"📥 Fetched {len(questions)} questions")

    # Step 2: Analyze data
    analyzed = analyze_questions(questions)
    print(f"🧠 Analyzed {len(analyzed)} questions")

    for item in analyzed:
        question = item["question"]

        # Step 3: Risk check
        if not check_risk():
            print("⚠️ High risk detected. Slowing down...\n")
            break

        # Step 4: Decision making
        decision = make_decision(item)

        if decision == "reply":
            # Step 5: Generate reply
            reply = generate_reply(question)

            print("\n💬 Question:", question)
            print("🤖 Reply:", reply)

            # Step 6: Save data
            save_data(question, reply)

        else:
            print(f"⏭️ Skipped: {question}")


if __name__ == "__main__":
    run_system()
