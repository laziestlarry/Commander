from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    req = request.get_json()
    prompt = req.get("prompt", "Hello Commander!")
    try:
        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are the AutonomaX Mission AI Commander."},
                      {"role": "user", "content": prompt}]
        )
        answer = res["choices"][0]["message"]["content"]
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)