import streamlit as st
import numpy as np

st.set_page_config(
    page_title="🎓 Student Placement Predictor",
    page_icon="🎯",
    layout="centered"
)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(120deg, #fdfbfb, #ebedee);
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    color: #6C63FF;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

/* Section Card */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #6C63FF, #8E8BFF);
    color: white;
    border-radius: 14px;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
    width: 100%;
}

/* Result box */
.result {
    background: linear-gradient(90deg, #E8EAF6, #F3E5F5);
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='main-title'>🎓 Student Placement Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Predict placement chances using AI 🤖</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 📚 Academic Inputs")

StudyHours = st.slider("📖 Study Hours per Day", 0, 12, 5)
Attendance = st.slider("📝 Attendance Percentage (%)", 50, 100, 75)
MockTestScore = st.slider("🧪 Mock Test Score", 0, 100, 60)
CodingSkill = st.slider("💻 Coding Skill Level (1–5)", 1, 5, 3)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 🚀 Prediction")

if st.button("✨ Predict Placement"):
    # Dummy logic (replace with ML model)
    if CodingSkill >= 3 and MockTestScore > 60:
        st.markdown("<div class='result'>🎉 High Chance of Placement!</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result'>⚠️ Needs More Practice – You Can Do It! 💪</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.sidebar.title("⚙️ Controls")
st.sidebar.info("Adjust values and click predict 🎯")

st.sidebar.markdown("### 💡 Tips")
st.sidebar.success("✔ Practice coding daily")
st.sidebar.warning("✔ Improve mock scores")
st.sidebar.info("✔ Maintain attendance")

