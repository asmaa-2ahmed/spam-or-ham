# main.py

import streamlit as st
from src.inference import predict_message

st.set_page_config(page_title="SMS Spam Classifier (BoW)", page_icon="📩")

st.title("📩 SMS Spam Classifier")
st.write("Enter an SMS message and the model will predict whether it's **Spam** or **Ham** (not spam).")

# Input box
user_input = st.text_area("✏️ Enter your message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:
        prediction, confidence = predict_message(user_input)
        label = "✅ Ham" if prediction == "ham" else "🚫 Spam"
        st.success(f"**Prediction:** {label}")
        st.info(f"**Confidence:** {confidence:.2f}")
