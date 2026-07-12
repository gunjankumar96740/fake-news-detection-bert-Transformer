import streamlit as st
from predict import predict_news

# Page settings
st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered"
)

# Title
st.title("📰 Fake News Detection")
st.write("Enter a news article or headline below to check whether it is Fake or Real.")

# Input box
news = st.text_area(
    "Enter News",
    height=250,
    placeholder="Paste the news article here..."
)

# Predict button
if st.button("Predict"):

    if news.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            label, confidence = predict_news(news)

        if label == "Fake News":
            st.error(f"Prediction: {label}")
        else:
            st.success(f"Prediction: {label}")

        st.write(f"**Confidence:** {confidence:.2%}")