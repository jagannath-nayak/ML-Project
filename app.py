import streamlit as st
from features.functions import load_lottie_file
import streamlit_lottie as st_lottie

st.set_page_config(page_title="Student Performance Navigator", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

# Initialize session state variables
if 'all_predictions' not in st.session_state:
    st.session_state['all_predictions'] = []

def intro():
    st.header("🎓 Student Performance Navigator", divider='rainbow')

    with st.container(border=True):
        left_col, right_col = st.columns(2)
        with left_col:
            st.subheader("About the App", divider='rainbow')
            intro = '''
🎯 **Student Performance Navigator** is a predictive analytics tool designed to forecast student math scores and offer actionable insights. 

🔍 It combines predictive modeling, explainability, fairness analysis, and personalized recommendations to help educators and students make informed decisions.
            '''
            st.markdown(intro)

        with right_col:
            banner = load_lottie_file("animations/banner.json")
            st_lottie.st_lottie(banner, loop=True, width=500, height=400)

    with st.container(border=True):
        left_col, right_col = st.columns(2)
        with right_col:
            st.subheader("App Features ℹ️", divider='rainbow')
            features = [
                "🎯 **Student Score Predictor** – Instantly predict student math scores using ML.",
                "📉 **Metrics Dashboard** – Evaluate model accuracy and error distribution.",
                "⚖️ **Bias Detection** – Check fairness across gender and ethnicity.",
                "📊 **Feedback Generator** – Generate personalized academic advice (LLM-powered).",
                "📚 **Student Assistant** – Ask Gemini anything about learning or the model."
            ]
            for feat in features:
                st.markdown(f"🔹 {feat}")

        with left_col:
            feature_anim = load_lottie_file("animations/features.json")
            st_lottie.st_lottie(feature_anim, loop=True, width=500, height=400)

    with st.container(border=True):
        st.subheader("Why Use Student Performance Navigator? 🚀", divider='rainbow')
        left_col, right_col = st.columns(2)
        with left_col:
            benefits = [   
                "📈 Improve student outcomes by identifying weak areas.",
                "🧠 Interpret ML models with LLM explainability.",
                "⚖️ Promote ethical AI with fairness analysis.",
                "📚 Empower students with actionable study plans.",
                "🧾 Export reports for academic tracking and decision-making."
            ]
            for benefit in benefits:
                st.markdown(f"✅ {benefit}")

        with right_col:
            impact = load_lottie_file("animations/impact.json")
            st_lottie.st_lottie(impact, loop=True, width=500, height=350)

    with st.container(border=True):
        st.subheader("FAQs ❓", divider='rainbow')
        with st.expander("What is this app for?"):
            st.write("It predicts student math scores and provides interpretability, fairness checks, and improvement tips.")
        with st.expander("Do I need to code?"):
            st.write("No coding required! Just fill the form and explore insights.")
        with st.expander("What algorithm does it use?"):
            st.write("It uses a trained ML model (e.g., RandomForest, CatBoosting Regressor, Linear Regression, Decision Tree).")

    with st.container(border=True):
        st_lottie.st_lottie(load_lottie_file("animations/celebration.json"), speed=1.2, width=900, height=300)
        st.success("🎓 Explore different features from navigation bar leftside.")

# Navigation
pg = st.navigation([
    st.Page(title="Home", page=intro, icon="🏠"),
    st.Page(title="Score Predictor", page="features/0-Score-Predictor.py", icon="🎯"),
    st.Page(title="Metrics Dashboard", page="features/1-metrics_dashboard.py", icon="📉"),
    st.Page(title="Feedback Generator", page="features/2-feedback_generator.py", icon="📊"),
    st.Page(title="Bias Detection", page="features/3-Bias-Detection.py", icon="⚖️"),
    st.Page(title="Student Assistant", page="features/4-student_assistant.py", icon="📚"),
])
pg.run()
