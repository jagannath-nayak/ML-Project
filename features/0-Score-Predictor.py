import streamlit as st
import pandas as pd
import pdfkit
import tempfile
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit App Setup
st.set_page_config(page_title="Student Score Predictor", layout="centered")
st.title("🎓 Student Score Predictor")
st.markdown("Fill in the details below to predict the student's performance.")

# --------- INPUT FORM ----------
with st.form("prediction_form"):
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
    reading_score = st.slider("Reading Score", min_value=0, max_value=100, value=50)
    writing_score = st.slider("Writing Score", min_value=0, max_value=100, value=50)

    submitted = st.form_submit_button("Predict")

if submitted:
    try:
        # Step 1: Wrap inputs into CustomData
        input_data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        pred_df = input_data.get_data_as_data_frame()

        # Step 2: Predict using selected model version
        pipeline = PredictPipeline()
        result = pipeline.predict(pred_df)
        prediction = round(result[0], 2)

        # Step 3: Output result
        st.success(f"🏆 The predicted math score is: **{prediction:.2f}**")

        # Step 4: Create report
        report_df = pred_df.copy()
        report_df["Predicted Math Score"] = prediction
        st.subheader("📄 Prediction Report")
        st.dataframe(report_df)

        # Step 5: Download CSV
        csv = report_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", data=csv, file_name="score_prediction.csv", mime='text/csv')

    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")
