# main.py

import sys
import traceback

from agents.scraper import fetch_questions
from agents.analyzer import analyze_questions
from agents.decision import make_decision
from agents.writer import generate_reply
from agents.poster import post_reply

from core.risk_control import check_risk
from core.memory import save_data
from database.db import init_db, save_to_db


def run_system():
    print("=" * 50)
    print("🚀 AI GROWTH ENGINE STARTED")
    print("=" * 50)

    try:
        # Initialize database
        init_db()

        # Step 1: Fetch questions
        questions = fetch_questions()
        print(f"📥 Total Questions Fetched: {len(questions)}")

        if not questions:
            print("❌ No questions found. Exiting...")
            return

        # Step 2: Analyze
        analyzed = analyze_questions(questions)
        print(f"🧠 Analyzed Questions: {len(analyzed)}")

        # Step 3: Process each
        for i, item in enumerate(analyzed, start=1):
            try:
                question = item.get("question", "No Question")
                source = item.get("source", "unknown")

                print("\n" + "-" * 50)
                print(f"🔎 Processing #{i}")
                print(f"❓ Question: {question}")

                # Step 4: Risk check
                if not check_risk():
                    print("⚠️ Risk high → stopping system")
                    break

                # Step 5: Decision
                decision = make_decision(item)
                print(f"🤔 Decision: {decision}")

                if decision != "reply":
                    continue

                # Step 6: Generate reply
                reply = generate_reply(question)

                print("🤖 Generated Reply:")
                print(reply)

                # Step 7: Posting (manual/assist)
                post_reply(question, reply, source)

                # Step 8: Save memory
                save_data(question, reply)

                # Step 9: Save database
                save_to_db(question, reply, source)

            except Exception as inner_error:
                print("❌ Error in processing item:")
                traceback.print_exc()
                continue

        print("\n✅ System Finished Successfully")

    except Exception as e:
        print("💥 CRITICAL ERROR:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_system()
