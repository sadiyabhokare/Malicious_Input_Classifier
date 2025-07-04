# Malicious_Input_Classifier
---
## 📂 Folder Structure

```
MaliciousInputClassifier/
├── app.py
├── train.py
├── sample_inputs.csv
├── requirements.txt
├── model/
│   ├── rf_model.pkl
│   └── label_encoder.pkl
└── utils/
    └── feature_extraction.py
```

---
markdown
# 🛡️ Malicious Input Classifier for Web Forms

A machine learning-powered application that classifies user-submitted form inputs as:
- 🟢 Benign
- 🔴 SQL Injection (SQLi)
- 🟠 Cross-Site Scripting (XSS)

Built with **scikit-learn** and deployed via **Streamlit**, this project demonstrates a lightweight, real-time defense layer against common web input attacks.

---

## 📌 Problem Statement

Web applications often receive malicious inputs through form fields such as:
- Login forms
- Comment boxes
- Search fields

These inputs can result in:
- 🛑 Data breaches
- 🔐 Account takeovers
- 🖼️ Website defacement

This project aims to mitigate such threats by building a machine learning classifier that detects **SQLi**, **XSS**, or **Benign** inputs in real-time.

---

## 🎯 Objectives

- 🔎 Analyze and extract key features from form inputs.
- 🧠 Train a machine learning model to detect attack types.
- 🖥️ Deploy a web-based dashboard for real-time and bulk prediction.
- 🚫 Prevent potential malicious inputs before backend processing.

---

## 🧱 System Architecture
This project follows a clean and modular architecture that separates UI, feature extraction, model inference, and output presentation.

🖼️ Architecture Diagram

---

## 📽️ Demo Video

👉 [Click here to watch the demo video](#)
*(Replace `#` with your YouTube/Drive/Streamlit Cloud video link)*

---

## 🧪 Sample Predictions

| Input                           | Prediction |
| ------------------------------- | ---------- |
| `' OR '1'='1`                   | 🔴 SQLI    |
| `<script>alert('xss')</script>` | 🟠 XSS     |
| `Hello! Great work!`            | 🟢 Benign  |

---

## 🛠️ Tech Stack

| Layer       | Technology                    |
| ----------- | ----------------------------- |
| 🧠 ML Model | `scikit-learn` (RandomForest) |
| 📊 Data     | `pandas`, `.csv` files        |
| 💾 Storage  | `joblib` model dumping        |
| 🎯 UI       | `Streamlit`                   |

---


## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/MaliciousInputClassifier.git
cd MaliciousInputClassifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train.py
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 👥 Team Members & Contributions

| Name               | Role and Contributions                                           |
| ------------------ | ---------------------------------------------------------------- |
| **\[Your Name 1]** | 🧠 ML Model Design, Feature Engineering, Model Training          |
| **\[Your Name 2]** | 💻 Frontend Development using Streamlit, UI Design, Input Modes  |
| **\[Your Name 3]** | 📦 Integration, Testing, Deployment Setup, Documentation, Report |

---
