# 🧠 AI Text Sentiment API (Flask + Hugging Face)

This project is part of my 5-week AI engineering prep.  
It demonstrates how to build a minimal Flask API that wraps a pre-trained NLP model using the Hugging Face `transformers` library.

---

## ✅ What It Does

- Accepts a `POST` request with a text string
- Runs a **sentiment analysis model**
- Returns the **sentiment label** (POSITIVE/NEGATIVE) and **confidence score**

---

## 🚀 Example Usage

### 🧪 Sample Input (JSON)

```json
POST /analyze
Content-Type: application/json

{
  "text": "This is the best tool I've ever used!"
}
```
### 📤 Sample Output
```
{
  "label": "POSITIVE",
  "score": 0.9996
}
```
## 🧰 Tech Stack
* Python 3.10
* Flask
* Hugging Face Transformers (pipeline("sentiment-analysis"))
* PyTorch (model backend)

## 🛠 How to Run Locally

1. Activate your virtual environment:

    ```bash
    path\to\freshvenv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the server:

    ```bash
    python app.py
    ```

4. Test it with `curl`, Postman, or the included Python script:

    ```python
    import requests

    response = requests.post("http://127.0.0.1:5000/analyze", json={
        "text": "The experience was amazing!"
    })

    print(response.json())
    ```

---

## 📦 Files

- `app.py` — Flask app with `/analyze` endpoint
- `test_api.py` — Quick test script
- `requirements.txt` — Required Python packages

---

## 🖼️ Coming Soon: Image Support

This API will be extended to support **image classification and captioning** as an additional endpoint.
