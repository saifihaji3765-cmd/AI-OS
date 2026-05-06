from flask import Flask, render_template, request
from agents.brain import run_system
from config import DEBUG

app = Flask(__name__)


# =========================
# 🏠 HOME ROUTE
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        user_input = request.form.get("input", "")
        command = request.form.get("command", "")

        if DEBUG:
            print("INPUT:", user_input)
            print("COMMAND:", command)

        results = run_system(user_input, command)

    return render_template("index.html", results=results)


# =========================
# 🚀 RUN APP
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
