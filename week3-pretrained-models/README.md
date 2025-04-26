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
