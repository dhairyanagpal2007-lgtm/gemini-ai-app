from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="AIzaSyDyfBC54LpDztUqXpMfC5CekWvo2tmigys")

model = genai.GenerativeModel("models/gemini-2.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        response = model.generate_content(question)
        answer = response.text
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
