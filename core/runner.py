# core/runner.py

import time
import traceback
from datetime import datetime

from main import run_system
from config import DEBUG, MIN_DELAY, MAX_DELAY


# ==============================
# ⚙️ LOOP SETTINGS
# ==============================

# Minimum aur maximum wait (seconds)
MIN_INTERVAL = 300   # 5 min
MAX_INTERVAL = 900   # 15 min

# Max runs per session (optional safety)
MAX_RUNS = 50


# ==============================
# 🧠 TIME HELPER
# ==============================

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==============================
# 🔁 AUTO RUNNER
# ==============================

def start_runner():
    print("=" * 60)
    print("🔄 AI AUTO RUNNER STARTED")
    print("=" * 60)

    run_count = 0

    while True:
        try:
            run_count += 1

            print(f"\n🕒 [{get_time()}] RUN #{run_count} STARTED\n")

            # 🚀 Run main system
            run_system()

            print(f"\n✅ RUN #{run_count} COMPLETED")

            # 🛑 Safety stop
            if run_count >= MAX_RUNS:
                print("⛔ Max runs reached. Stopping runner safely.")
                break

            # 🎲 Random interval (human behavior)
            wait_time = int((MIN_INTERVAL + MAX_INTERVAL) / 2)

            print(f"⏳ Next run in {wait_time} seconds...\n")
            time.sleep(wait_time)

        except KeyboardInterrupt:
            print("\n🛑 Manual stop detected. Exiting...")
            break

        except Exception as e:
            print("\n💥 RUNNER ERROR:")
            traceback.print_exc()

            print("\n⏳ Retrying in 60 seconds...\n")
            time.sleep(60)


# ==============================
# ▶️ ENTRY POINT
# ==============================

if __name__ == "__main__":
    start_runner()
