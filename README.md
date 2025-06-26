# Student Performance Navigator — End to End Machine Learning Project

Welcome to the **Student Performance Navigator**, an end-to-end machine learning project designed to predict student math scores, provide actionable insights, check model fairness, and deliver personalized academic feedback—all through an interactive web application.

---

## 🚀 Project Overview

This project covers the complete ML workflow:
- **Data Ingestion & Analysis:** Cleaning, exploring, and visualizing student performance data.
- **Feature Engineering:** Transforming raw data into meaningful features.
- **Model Training & Evaluation:** Building, tuning, and comparing multiple regression models (Linear Regression, Ridge, CatBoost, etc.) with robust metric reporting (R² score, MAE, RMSE).
- **Fairness & Bias Detection:** Evaluating model performance across demographic groups.
- **Deployment:** Interactive web applications using Streamlit and Flask for easy access to predictions and insights.
- **Explainability & Feedback:** LLM-powered explanations and actionable study plans for users.

---

## 🏗️ Project Structure

```
ML-Project/
├── app.py                          # Main Streamlit application (modular, multi-page)
├── application.py                  # Flask backend for web prediction
├── features/                       # Modular Streamlit feature pages (predictor, metrics, bias, etc.)
│   ├── 0-Score-Predictor.py
│   ├── 1-metrics_dashboard.py
│   ├── 2-feedback_generator.py
│   ├── 3-Bias-Detection.py
│   └── 4-student_assistant.py
├── notebook/
│   └── 2. MODEL TRAINING.ipynb     # Jupyter notebook for EDA, model training, and metric reporting
├── templates/                      # HTML templates for Flask app
│   ├── home.html
│   └── index.html
├── features/functions.py           # Utility functions (e.g., animation loaders)
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation (this file)
```

---

## ✨ Features

- **Score Predictor:** Instantly predict student math scores with a trained ML model.
- **Metrics Dashboard:** Visualize model accuracy and error distribution.
- **Bias Detection:** Analyze fairness across gender and ethnicity.
- **Feedback Generator:** Receive personalized, LLM-powered academic advice.
- **Student Assistant:** Ask questions about learning or the model.
- **No Coding Needed:** User-friendly interfaces built with Streamlit and Flask.
- **Model Comparison:** Supports Ridge, Linear, CatBoost, RandomForest, AdaBoost, XGBoost, Lasso, KNN, and Decision Tree regressors.

---

## 🔥 Model Performance

Top test set R² scores:
- **Ridge Regression:** 0.8806
- **Linear Regression:** 0.8804
- **CatBoosting Regressor:** 0.8516
- **Random Forest Regressor:** 0.8513

---

## 🛠️ Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/jagannath-nayak/ML-Project.git
   cd ML-Project
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```
4. **(Optional) Run the Flask app:**
   ```sh
   python application.py
   ```

---

## 📁 Folder/Component Overview

- `app.py`: Main entry point for Streamlit dashboard.
- `features/`: Modular feature pages (predictor, metrics, feedback, bias, assistant).
- `application.py`: Flask-based web prediction interface.
- `notebook/2. MODEL TRAINING.ipynb`: Data analysis, feature engineering, model training/evaluation.
- `templates/`: Web templates for Flask.
- `features/functions.py`: Utility and helper functions.

---

