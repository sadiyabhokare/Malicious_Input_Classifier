# app.py
import streamlit as st
import pandas as pd
import joblib
from utils.feature_extraction import extract_features

# Load model and label encoder
model = joblib.load("model/rf_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

st.set_page_config(page_title="🛡️ Malicious Input Classifier", layout="centered")
st.title("🛡️ Malicious Input Classifier for Web Forms")
st.markdown("Classifies form inputs as **Benign**, **SQL Injection**, or **XSS Attack**.")

# UI option
option = st.radio("Choose Input Mode:", ("🔤 Enter Single Input", "📁 Upload CSV File"))

if option == "🔤 Enter Single Input":
    user_input = st.text_area("Enter form input here:")
    if user_input:
        features = extract_features(user_input)
        prediction = model.predict([features])[0]
        result_label = label_encoder.inverse_transform([prediction])[0]

        emoji_map = {
            "Benign": "🟢",
            "SQLI": "🔴",
            "XSS": "🟠"
        }

        st.markdown(f"### Prediction: {emoji_map.get(result_label, '❓')} **{result_label}**")

elif option == "📁 Upload CSV File":
    uploaded_file = st.file_uploader("Upload a CSV file with column `input_text`", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        if "input_text" not in df.columns:
            st.error("❌ CSV must contain a column named `input_text`.")
        else:
            df["features"] = df["input_text"].apply(extract_features)
            df["prediction"] = df["features"].apply(lambda x: model.predict([x])[0])
            df["label"] = label_encoder.inverse_transform(df["prediction"])
            
            emoji_map = {
                "Benign": "🟢",
                "SQLI": "🔴",
                "XSS": "🟠"
            }
            df["status"] = df["label"].apply(lambda lbl: f"{emoji_map.get(lbl, '❓')} {lbl}")
            
            st.success("✅ Prediction completed!")
            st.dataframe(df[["input_text", "status"]])
