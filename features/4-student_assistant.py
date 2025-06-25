import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load and configure Gemini
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Page setup
st.set_page_config(page_title="🧠 Ask Gemini", layout="centered")
st.title("🧠 Ask Gemini – Your Learning Assistant")

st.markdown("Ask anything about student learning, performance, or model behavior. Powered by Google Gemini.")

# Tabs for separation
tab1, tab2 = st.tabs(["💬 Ask a Learning Question", "🔍 Explain the Model"])

# 1. 🗨️ Ask Gemini — Freeform Assistant
with tab1:
    st.subheader("💬 Ask a Question")
    user_question = st.text_area("What would you like to ask about studying, math, or test prep?")
    
    if st.button("Ask Gemini"):
        if not user_question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                try:
                    response = model.generate_content(f"Student question: {user_question}")
                    st.success(response.text.strip())
                except Exception as e:
                    st.error(f"⚠️ Failed to generate response: {e}")

# 2. 🧠 Explain the Model to a Non-Technical User
with tab2:
    st.subheader("🔍 Explain the Math Prediction Model")
    st.markdown("This will generate a simple explanation for non-technical users (e.g. students or parents)")

    if st.button("Explain the Model"):
        explanation_prompt = """
        Explain to a non-technical parent or student how a machine learning model predicts a student's math score based on features like:
        - Reading and writing scores
        - Test preparation
        - Gender, race/ethnicity
        - Parental education
        - Lunch type (free/reduced or standard)

        The explanation should be friendly, simple, and easy to understand in 2–3 short paragraphs.
        """

        try:
            explanation = model.generate_content(explanation_prompt)
            st.info(explanation.text.strip())
        except Exception as e:
            st.error(f"⚠️ Could not generate explanation: {e}")
