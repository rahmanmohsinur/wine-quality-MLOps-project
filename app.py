# /app.py

"""Minimal Flask interface for running prediction with a saved model."""
from pathlib import Path
from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)
MODEL_PATH = Path("artifacts/model_trainer/model.joblib")

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/predict")
def predict():
    if not MODEL_PATH.exists():
        return jsonify({"error": "Model not found. Run main.py first."}), 503
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Send a JSON object containing feature values."}), 400
    try:
        features = pd.DataFrame([payload])
        model = joblib.load(MODEL_PATH)
        prediction = float(model.predict(features)[0])
        return jsonify({"predicted_quality": prediction})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)