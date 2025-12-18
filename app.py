import google.generativeai as genai

genai.configure(api_key="AIzaSyDyfBC54LpDztUqXpMfC5CekWvo2tmigys")

model = genai.GenerativeModel("models/gemini-2.5-flash")

print("===== Gemini Question Answer App =====")
print("Type 'exit' to stop\n")

while True:
    question = input("Ask your question: ")

    if question.lower() == "exit":
        print("App closed")
        break

    response = model.generate_content(question)
    print("\nGemini Answer:")
    print(response.text)
    print("-----------------------------------")
