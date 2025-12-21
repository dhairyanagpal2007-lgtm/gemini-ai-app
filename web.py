from flask import Flask, render_template, request
import google.generativeai as genai
import os
from PIL import Image

app = Flask(__name__)

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form.get("question")

        image_file = request.files.get("image")

        if image_file and image_file.filename != "":
            img = Image.open(image_file)
            response = model.generate_content([question, img])
        else:
            response = model.generate_content(question)

        answer = response.text

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
