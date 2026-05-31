import os
from flask import Flask, request, jsonify
from app.predict import predict_sentiment
from app.model import load_model

app = Flask(__name__)

# Define model path relative to the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'sentiment_model.pkl')

model = load_model(MODEL_PATH)  # load once at startup

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    result = predict_sentiment(model, data["text"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)