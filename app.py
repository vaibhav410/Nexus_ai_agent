from flask import Flask, render_template, request, jsonify
from agents.agent import process_ai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    user_input = data.get("text", "")
    mode = data.get("mode", "therapy")
    reply = process_ai(user_input, mode)
    return jsonify({"reply": reply})



if __name__ == "__main__":
    app.run(debug=True)
