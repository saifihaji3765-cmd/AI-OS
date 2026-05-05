from flask import Flask, render_template, request
from agents.brain import run_system
from config import DEBUG

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        user_input = request.form.get("input", "").strip()

        if DEBUG:
            print("User Input:", user_input)

        # run full AI system
        results = run_system(user_input)

    return render_template("index.html", results=results)


# Health check (Render ke liye useful)
@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # Render ke liye required
    app.run(host="0.0.0.0", port=10000)
