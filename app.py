# app.py

from flask import Flask, request, render_template
import re

app = Flask(__name__)

# 🔗 link extract
def extract_link(text):
    urls = re.findall(r'(https?://\S+)', text)
    return urls[0] if urls else ""

# 🧠 simple analyzer
def analyze(text):
    t = text.lower()
    data = {
        "target": "students" if "student" in t else "people",
        "product": "AI system" if "ai" in t else "system",
        "problem": "earning" if "earn" in t else "learning",
        "angle": "automation" if "auto" in t or "automatic" in t else "general",
        "link": extract_link(text)
    }
    return data

# ✍️ post generator (NO random)
def generate_post(ctx, platform):
    target = ctx["target"]
    product = ctx["product"]
    problem = ctx["problem"]
    link = ctx["link"]
    angle = ctx["angle"]

    if angle == "automation":
        hook = f"Stop doing everything manually — {target} are wasting time."
        body = f"I see many {target} trying {problem} manually, but automation is the real advantage."
        insight = f"An {product} can work in the background and save hours."
    else:
        hook = f"Most {target} are stuck because they follow random methods."
        body = f"They try to {problem} without a clear system."
        insight = f"Without a system, results stay inconsistent."

    cta = "If you want, I can explain how it works."
    if link:
        cta += f" {link}"

    if platform == "reddit":
        end = "What do you think?"
    elif platform == "quora":
        end = "This is something beginners ignore."
    else:
        end = "DM me if you're serious."

    return f"{hook}\n\n{body}\n\n{insight}\n\n{cta}\n\n{end}"

# 🌐 routes
@app.route("/", methods=["GET", "POST"])
def home():
    posts = None

    if request.method == "POST":
        user_input = request.form.get("input", "")
        ctx = analyze(user_input)

        posts = {
            "reddit": generate_post(ctx, "reddit"),
            "quora": generate_post(ctx, "quora"),
            "facebook": generate_post(ctx, "facebook")
        }

    return render_template("index.html", posts=posts)

# 🚀 run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
