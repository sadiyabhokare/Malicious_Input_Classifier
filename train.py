# for train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
from utils.feature_extraction import extract_features
import os

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Load dataset
df = pd.read_csv("sample_inputs.csv")

# Extract features
X = [extract_features(text) for text in df["input_text"]]

# Encode labels (Benign=0, SQLI=1, XSS=2)
le = LabelEncoder()
y = le.fit_transform(df["label"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and label encoder
joblib.dump(model, "model/rf_model.pkl")
joblib.dump(le, "model/label_encoder.pkl")

print("✅ Model trained and saved successfully.")