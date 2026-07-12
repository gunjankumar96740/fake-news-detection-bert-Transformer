# 📰 Fake News Detection using BERT Transformer

A deep learning-based Fake News Detection system built using **BERT (bert-base-uncased)**. The model classifies news articles as **Fake** or **Real** using a fine-tuned Transformer model and is deployed as an interactive **Streamlit** web application.

---

## 🚀 Live Demo

🔗 **Streamlit App:** *(Add your Streamlit link here)*

🔗 **Hugging Face Model:** https://huggingface.co/GunjanKumar96740/fake-news-detection-bert

---

## 📌 Project Overview

Fake news spreads rapidly through online platforms, making automated detection an important NLP task.

This project fine-tunes the **BERT (Bidirectional Encoder Representations from Transformers)** model for binary text classification. Users can enter a news article or headline through a Streamlit interface, and the model predicts whether it is **Fake** or **Real**.

---

## ✨ Features

- Fine-tuned BERT (`bert-base-uncased`)
- Binary classification (Fake / Real News)
- Interactive Streamlit web application
- Hugging Face model hosting
- Confidence score for predictions
- GPU-supported training with PyTorch

---

## 🛠️ Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- Streamlit
- Scikit-learn
- Pandas
- NumPy

---

## 📊 Dataset

The model was trained on a combined fake and real news dataset containing thousands of news articles.

The dataset includes:

- Fake News
- Real News

**Note:** The dataset is not included in this repository because of its size.

---

## 🧠 Model Architecture

- Base Model: **bert-base-uncased**
- Tokenizer: BERT Tokenizer
- Maximum Sequence Length: 512
- Optimizer: AdamW
- Loss Function: Cross Entropy Loss

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Test Accuracy | **99.97%** |
| Weighted F1 Score | **99.97%** |

---

## 📂 Project Structure

```text
fake-news-detection-bert-Transformer/
│
├── app.py
├── predict.py
├── requirements.txt
├── README.md
├── data_quality_assessment.ipynb
│
└── docs/
    ├── data_quality_report.md
    └── project_requirements.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/gunjankumar96740/fake-news-detection-bert-Transformer.git

cd fake-news-detection-bert-Transformer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Application

### Home Page

*(Add screenshot here)*

### Prediction Example

*(Add screenshot here)*

---

## 🎯 Future Improvements

- Multi-language fake news detection
- Explainable AI (attention visualization)
- Support for longer news articles
- Model optimization for faster inference
- Docker deployment
- REST API using FastAPI

---

## 👨‍💻 Author

**Gunjan Kumar**

- GitHub: https://github.com/gunjankumar96740
- Hugging Face: https://huggingface.co/GunjanKumar96740

---

## ⭐ If you found this project useful, consider giving it a star!
