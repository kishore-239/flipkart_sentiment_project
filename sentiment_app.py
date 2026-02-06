import streamlit as st
import pickle
import re

# --------------------
# Load trained model
# --------------------
with open("sentiment_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# --------------------
# Text cleaning
# --------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"read more", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# --------------------
# Streamlit UI
# --------------------
st.set_page_config(page_title="Flipkart Sentiment Analysis", layout="centered")

st.title(" Flipkart Review Sentiment Analysis")
st.write("Enter a Flipkart product review to predict sentiment.")

review = st.text_area("✍️ Enter Review")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        cleaned_review = clean_text(review)
        vector = vectorizer.transform([cleaned_review])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")
