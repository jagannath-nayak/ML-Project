import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from src.utils import load_object

# Page setup
st.set_page_config(page_title="📈 Training Metrics Dashboard", layout="wide")
st.title("📊 Model Training Metrics Dashboard")
st.markdown("Evaluate model performance on the test dataset.")

# Load test data
try:
    test_df = pd.read_csv("artifacts/test_data.csv")
    model = load_object("artifacts/model.pkl")
    preprocessor = load_object("artifacts/preprocessor.pkl")

    # Prepare features and target
    target_col = "math_score"
    X_test = test_df.drop(columns=[target_col])
    y_test = test_df[target_col]

    X_test_processed = preprocessor.transform(X_test)
    y_pred = model.predict(X_test_processed)

    # Metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    st.subheader("✅ Performance Summary")
    st.markdown(f"- **R² Score:** `{r2:.4f}`")
    st.markdown(f"- **MAE:** `{mae:.2f}`")
    st.markdown(f"- **RMSE:** `{rmse:.2f}`")

    st.divider()

    # Residual Plot
    st.subheader("📉 Residual Plot")
    residuals = y_test - y_pred
    fig_residual, ax1 = plt.subplots()
    ax1.scatter(y_pred, residuals, alpha=0.6)
    ax1.axhline(0, color='red', linestyle='--')
    ax1.set_xlabel("Predicted Math Score")
    ax1.set_ylabel("Residuals")
    ax1.set_title("Residuals vs Predictions")
    st.pyplot(fig_residual)

    # Predicted vs Actual Plot
    st.subheader("📌 Predicted vs Actual")
    fig_actual, ax2 = plt.subplots()
    ax2.scatter(y_test, y_pred, color="green", alpha=0.6)
    ax2.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    ax2.set_xlabel("Actual Math Score")
    ax2.set_ylabel("Predicted Math Score")
    ax2.set_title("Actual vs Predicted")
    st.pyplot(fig_actual)

    # Histogram of Residuals
    st.subheader("🔍 Distribution of Residuals")
    fig_hist, ax3 = plt.subplots()
    ax3.hist(residuals, bins=30, color="purple", alpha=0.7)
    ax3.set_title("Histogram of Residuals")
    ax3.set_xlabel("Residual (Actual - Predicted)")
    st.pyplot(fig_hist)

except Exception as e:
    st.error(f"⚠️ Error loading test data or model: {e}")
