import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.utils import load_object
from sklearn.metrics import mean_absolute_error

st.set_page_config(page_title="⚖️ Bias Detection", layout="wide")
st.title("⚖️ Bias Detection")
st.markdown("Evaluate if the model under- or over-predicts for certain demographic groups.")

# ---------- Load model and data ----------
try:
    model = load_object("artifacts/model.pkl")
    preprocessor = load_object("artifacts/preprocessor.pkl")
    df = pd.read_csv("artifacts/test_data.csv")
    target_col = "math_score"

    X = df.drop(columns=[target_col])
    y_true = df[target_col]
    X_proc = preprocessor.transform(X)
    y_pred = model.predict(X_proc)

    df['prediction'] = y_pred
    df['residual'] = y_true - y_pred  # +ve = underprediction, -ve = overprediction

    st.checkbox("Show raw data", value=False, key="show_raw")

    if st.session_state.show_raw:
        st.dataframe(df.head())

    # -------- Group by Gender --------
    st.subheader("🧍 Bias by Gender")
    gender_stats = df.groupby('gender')[['math_score', 'prediction', 'residual']].mean().reset_index()

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        sns.barplot(data=gender_stats, x='gender', y='prediction', palette='Set2', ax=ax1)
        ax1.set_title("Average Predicted Score by Gender")
        ax1.set_ylabel("Predicted Math Score")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        sns.barplot(data=gender_stats, x='gender', y='residual', palette='coolwarm', ax=ax2)
        ax2.axhline(0, linestyle='--', color='black')
        ax2.set_title("Average Residual by Gender (True - Predicted)")
        ax2.set_ylabel("Residual")
        st.pyplot(fig2)

    # -------- Group by Race/Ethnicity --------
    st.subheader("🧑🏽‍🤝‍🧑🏽 Bias by Race/Ethnicity")
    race_stats = df.groupby('race_ethnicity')[['math_score', 'prediction', 'residual']].mean().reset_index()

    col3, col4 = st.columns(2)

    with col3:
        fig3, ax3 = plt.subplots()
        sns.barplot(data=race_stats, x='race_ethnicity', y='prediction', palette='Set3', ax=ax3)
        ax3.set_title("Average Predicted Score by Race/Ethnicity")
        ax3.set_ylabel("Predicted Math Score")
        ax3.set_xticklabels(ax3.get_xticklabels(), rotation=30)
        st.pyplot(fig3)

    with col4:
        fig4, ax4 = plt.subplots()
        sns.barplot(data=race_stats, x='race_ethnicity', y='residual', palette='coolwarm', ax=ax4)
        ax4.axhline(0, linestyle='--', color='black')
        ax4.set_title("Average Residual by Race/Ethnicity")
        ax4.set_ylabel("Residual")
        ax4.set_xticklabels(ax4.get_xticklabels(), rotation=30)
        st.pyplot(fig4)

except Exception as e:
    st.error(f"⚠️ Failed to load model or test data: {e}")
