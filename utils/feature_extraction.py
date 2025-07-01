#  feature_extraction.py
import re

def extract_features(text):
    features = {}
    text = str(text).lower()

    features["length"] = len(text)
    features["quote_count"] = text.count("'") + text.count('"')
    features["semicolon_count"] = text.count(";")
    features["angle_brackets"] = text.count("<") + text.count(">")
    features["script_count"] = len(re.findall(r"<script>", text))
    features["sql_keywords"] = sum([1 for word in ["select", "drop", "union", "insert", "update", "delete", "from", "--"] if word in text])
    features["xss_keywords"] = sum([1 for word in ["script", "alert", "onerror", "onload", "<iframe"] if word in text])
    features["special_char_ratio"] = sum([1 for c in text if not c.isalnum() and c != " "]) / (len(text) + 1)

    return list(features.values())