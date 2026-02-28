from flask import Flask, request, jsonify
from flask_cors import CORS
from brain import ask_brain

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Server running"


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    user_message = data["message"]

    print("User:", user_message)

    ai_reply = ask_brain(user_message)

    print("AI:", ai_reply)

    return jsonify({
        "reply": ai_reply
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
