import React, { useState } from "react";

function App() {
  const [textInput, setTextInput] = useState("");
  const [textResult, setTextResult] = useState(null);
  const [imageFile, setImageFile] = useState(null);
  const [imageResult, setImageResult] = useState(null);
  const [textLoading, setTextLoading] = useState(false);
  const [imageLoading, setImageLoading] = useState(false);
  const [imagePreview, setImagePreview] = useState(null);


  const handleTextSubmit = async () => {
    setTextLoading(true);
    setTextResult(null);
    setTextInput("");

    try {
      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: textInput }),
      });

      const data = await response.json();
      setTextResult(data);
      setTextLoading(false);
  } catch (error) {
      console.error("Text API error:", error);
      alert("Something went wrong. Please try again.");
  } finally {
      setTextLoading(false);
  }
  };
  const handleImageSubmit = async () => {
    if (!imageFile) return;

    setImageLoading(true);
    setImageResult(null);
    setImageFile(null);

    try {
      const formData = new FormData();
      formData.append("image", imageFile);

      const response = await fetch("http://127.0.0.1:5000/classify-image", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setImageResult(data);
      setImageLoading(false);
  } catch (error) {
      console.error("Image API error:", error);
      alert("Something went wrong. Please try again.");
  } finally {
      setImageLoading(false);
  }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>🧠 AI Web App</h1>

      <section>
        <h2>Text Sentiment Analysis</h2>
        <textarea
          rows="4"
          style={{ width: "100%" }}
          value={textInput}
          onChange={(e) => setTextInput(e.target.value)}
          placeholder="Type a sentence..."
        />
        <button onClick={handleTextSubmit} disabled={textLoading}>
          Analyze Sentiment
        </button>
        {textLoading && <p>⏳ Loading...</p>}

        {textResult && (
          <p>
            <strong>{textResult.label}</strong> ({(textResult.score * 100).toFixed(2)}%)
          </p>
        )}
      </section>

      <hr />

      <section>
        <h2>Image Classification</h2>
        <div style={{ marginBottom: "1rem" }}>
          <input
        type="file"
        accept="image/*"
        onChange={(e) => {
          const file = e.target.files[0];
          setImageFile(file);
          if (file) {
            setImagePreview(URL.createObjectURL(file));
          } else {
            setImagePreview(null);
          }
        }}
      />
</div>
        {imagePreview && (
          <div style={{ marginBottom: "1rem" }}>
            <img
              src={imagePreview}
              alt="Preview"
              style={{ maxWidth: "100%", maxHeight: "200px", borderRadius: "6px" }}
            />
          </div>
        )}

        <button onClick={handleImageSubmit} disabled={imageLoading}>
          Classify Image
        </button>
        {imageLoading && <p>⏳ Loading...</p>}

        {imageResult && (
  <>
    <ul>
      {imageResult.map((res, index) => (
        <li key={index}>
          {res.label} — {(res.score * 100).toFixed(2)}%
        </li>
      ))}
    </ul>
    <button onClick={() => {
      setImageResult(null);
      setImageFile(null);
      setImagePreview(null);
    }}>
      Reset Image
    </button>
  </>
)}

      </section>
    </div>
  );
}

export default App;
