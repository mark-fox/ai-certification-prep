from flask import Flask, request, jsonify
from transformers import pipeline

# Load sentiment model once at startup
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0f"
)

# Initialize Flask app
app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    results = sentiment_model(data["text"])
    return jsonify(results[0])  # Return just the first result

if __name__ == "__main__":
    app.run(debug=True)
