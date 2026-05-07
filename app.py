from flask import Flask, render_template, request
from agents.brain import process_input

app = Flask(__name__)

# =========================
# HOME
# =========================
@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        user_input = request.form.get("user_input")

        if user_input:
            response = process_input(user_input)

    return render_template(
        "index.html",
        response=response
    )

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
