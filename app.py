from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
# import openai  # (keep this for future, but not using for now)

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

    print("Skipping real OpenAI call for now...")  # For now, skipping actual API call

    # --- Normally you would call OpenAI here, but we're skipping it now ---
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # prompt = f"""You are an expert evaluator.
    # Evaluate the following answer for the concept "{concept}" at the cognitive level "{micro_level}".
    #
    # Answer:
    # {answer}
    #
    # Respond with three fields only:
    # 1. Overall score (1-5)
    # 2. Hint for improvement
    # 3. Next micro-level (one of: recall, reframe, apply, contrast, critique, remix)
    # """
    # completion = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}],
    # )
    # response_text = completion.choices[0].message['content']

    # --- Fake hardcoded response for now ---
    return jsonify({
        "overall": 4.2,
        "hint": "Try to connect this to a real-world situation.",
        "next_level": "apply"
    })

if __name__ == "__main__":
    app.run(port=5000)
