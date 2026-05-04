# app.py

from flask import Flask, request, render_template
from agents.brain import generate_all_posts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    posts = None

    if request.method == "POST":
        user_input = request.form.get("input")
        posts = generate_all_posts(user_input)

    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
