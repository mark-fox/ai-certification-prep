# 🧠 AI Sentiment & Image Classifier

This is a full-stack AI-powered web application built as the final project for a 5-week AI engineering prep course.  
It uses pre-trained Hugging Face models for both **text sentiment analysis** and **image classification**, wrapped in a Flask API and served through a modern React frontend.

---

## ✨ Features

- 💬 Analyze text sentiment (POSITIVE / NEGATIVE)
- 🖼️ Upload images and get top predicted labels
- 🔁 Real-time interaction between React and Flask
- 🎯 Clean, responsive UI with live result previews

---

## 🧰 Tech Stack

| Layer      | Tools                                      |
|------------|--------------------------------------------|
| Frontend   | React, JavaScript                          |
| Backend    | Python, Flask, Hugging Face Transformers   |
| AI Models  | distilBERT (text), ResNet (image)          |
| Styling    | Inline styles (lightweight and flexible)   |

---

## 🚀 How to Run Locally

### 🧠 Backend (Flask API)

1. **Navigate to backend folder**:

    ```bash
    cd backend
    ```

2. **(Optional) Create a virtual environment**:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the server**:

    ```bash
    python app.py
    ```

Server runs at: `http://127.0.0.1:5000`

---

### 🌐 Frontend (React)

1. **Navigate to frontend folder**:

    ```bash
    cd frontend
    ```

2. **Install dependencies**:

    ```bash
    npm install
    ```

3. **Run the React app**:

    ```bash
    npm start
    ```

Opens automatically at: `http://localhost:3000`

---

## 🔮 Future Ideas

- Deploy to Render / Netlify for live demo
- Add file type validation
- Include image captioning as bonus feature
- Support batch predictions


---

## 🧠 Credits

- Hugging Face Transformers
- Flask + Flask-CORS
- React (Create React App)

---
