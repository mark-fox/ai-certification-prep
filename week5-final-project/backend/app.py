from flask import Flask, request, jsonify
from transformers import pipeline
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS


# Load sentiment model once at startup
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0f"
)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    results = sentiment_model(data["text"])
    return jsonify(results[0])  # Return just the first result

@app.route("/classify-image", methods=["POST"])
def classify_image():
    if "image" not in request.files:
        return jsonify({"error": "No image file uploaded."}), 400

    image_file = request.files["image"]
    if image_file.filename == "":
        return jsonify({"error": "Empty filename."}), 400

    # Save and process the image
    filename = secure_filename(image_file.filename)
    filepath = os.path.join("temp_image.jpg")
    image_file.save(filepath)

    try:
        from PIL import Image
        image = Image.open(filepath)

        classifier = pipeline("image-classification")
        results = classifier(image)

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == "__main__":
    app.run(debug=True)
