from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API key from Render Environment Variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            response = model.generate_content(question)
            answer = response.text

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
