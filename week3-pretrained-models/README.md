# 🤖 Pretrained Text Models Exploration

This project is part of my 5-week AI engineering prep.  
In Week 3, I explored **using pre-trained NLP models** from the Hugging Face 🤗 Transformers library.

The goal was to practice:
- Loading and using models without retraining
- Performing common text AI tasks
- Documenting outputs clearly

---

## 🧠 Tasks Covered

| Task | Model/Method |
|-----|--------------|
| Sentiment Analysis | `pipeline('sentiment-analysis')` |
| Text Summarization | `pipeline('summarization')` |
| Question Answering | `pipeline('question-answering')` |

Each task was performed with a few lines of Python using Hugging Face's `pipeline()` interface.

---

## 🛠️ Tools & Libraries

- Python 3.10
- Hugging Face Transformers
- PyTorch (for backend support)
- Jupyter Notebook (VS Code)

---

## 📁 Files

- `text-models.ipynb` — Notebook containing all tasks
- (Optional future expansion: `image-models.ipynb`)

---

## 📸 Sample Outputs

> _Sentiment Analysis Example:_

```python
[{'label': 'POSITIVE', 'score': 0.9998}]
```

---

## 🖼️ Image Models (New)

| Task | Model/Method |
|-----|--------------|
| Image Classification | `pipeline('image-classification')` |
| Image Captioning | `pipeline('image-to-text')` |

We extended Week 3 to include simple image-based AI tasks:
- 🏷️ **Image Classification**: Predict the main object(s) in a photo
- 🖼️ **Image Captioning**: Generate a full natural-language description for an input image

These were performed using pre-trained models from Hugging Face without any fine-tuning.

---

## 📁 Updated Files

- `text-models.ipynb` — NLP tasks (sentiment, summarization, question answering)
- `image-models.ipynb` — Computer vision tasks (classification, captioning)
- `sample-images/` — Folder containing example images for testing

---
