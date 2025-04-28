from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
# import openai  # (keep this commented out for now)

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/score", methods=["POST"])
def score_answer():
    data = request.get_json()
    print("Received data:", data)

    concept = data.get("concept")
    micro_level = data.get("micro_level")
    answer = data.get("answer")

    if not all([concept, micro_level, answer]):
        return jsonify({"error": "Missing fields"}), 400

    # ⚡ NO OpenAI call, no delays
    # Commented out OpenAI live call for now
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # prompt = f"""Evaluate the following answer for the concept "{concept}" at the micro-level "{micro_level}": {answer}"""
    # completion = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}],
    # )
    # response_text = completion.choices[0].message['content']

    # ⚡ Just return a hardcoded fast JSON
    return jsonify({
        "overall": 4.2,
        "hint": "Try to connect this to a real-world situation.",
        "next_level": "apply"
    })

if __name__ == "__main__":
    app.run(port=5000)
