import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
gemini = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit setup
st.set_page_config(page_title="🧠 Feedback Generator", layout="centered")
st.title("🧠 AI-Powered Feedback Generator")
st.markdown("Get personalized academic feedback based on student profile and predicted score.")

# --------- INPUT FORM ----------
with st.form("feedback_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    race_ethnicity = st.selectbox("Race/Ethnicity", [
        "group A", "group B", "group C", "group D", "group E"
    ])
    parental_level_of_education = st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college", 
        "associate's degree", "bachelor's degree", "master's degree"
    ])
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.slider("Reading Score", 0, 100, 50)
    writing_score = st.slider("Writing Score", 0, 100, 50)
    predicted_math_score = st.slider("Predicted Math Score", 0, 100, 75)

    submitted = st.form_submit_button("Generate Feedback")

if submitted:
    try:
        prompt = f"""
        A student has the following academic and demographic profile:
        - Gender: {gender}
        - Race/Ethnicity: {race_ethnicity}
        - Parental Education: {parental_level_of_education}
        - Lunch: {lunch}
        - Test Preparation Course: {test_preparation_course}
        - Reading Score: {reading_score}
        - Writing Score: {writing_score}

        Their predicted math score is {predicted_math_score} out of 100.

        Based on this, generate 2–3 sentences of constructive, encouraging feedback on how the student can continue to improve academically. Keep it friendly and motivational.
        """

        response = gemini.generate_content(prompt)
        feedback = response.text.strip()

        st.subheader("📬 Personalized Academic Feedback")
        st.success(feedback)

    except Exception as e:
        st.error(f"⚠️ Failed to generate feedback: {e}")
