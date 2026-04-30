import streamlit as st

st.set_page_config(
    page_title="Skills - Novie Roa",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* 🌌 FUTURISTIC BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    background-size: 400% 400%;
    animation: bg 10s ease infinite;
    color: white;
}

@keyframes bg {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ TITLE */
.title {
    text-align: center;
    font-size: 60px;
    color: #00ffff;
    text-shadow: 0 0 15px #00ffff, 0 0 30px #0088ff;
    margin-bottom: 30px;
}

/* 🧊 CARD */
.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(0,255,255,0.3);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(0,255,255,0.2);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 35px rgba(0,255,255,0.6);
}

/* 📊 PROGRESS STYLE */
.skill-label {
    margin-top: 15px;
    font-weight: bold;
    color: #b3f0ff;
}

.stProgress > div > div > div {
    background: linear-gradient(90deg, #00ffff, #0077ff);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>⚡ MY SKILLS</h1>", unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns(2)

skills = {
    "Python": 90,
    "HTML/CSS": 85,
    "Java": 80,
    "Database Management": 75,
    "UI/UX Design": 88,
    "Problem Solving": 92
}

with col1:
    st.markdown("""
    <div class='card'>
        <h2>💻 Technical Skills</h2>
        <p>These are my core programming and development skills.</p>
    </div>
    """, unsafe_allow_html=True)

    for skill, value in list(skills.items())[:3]:
        st.markdown(f"<p class='skill-label'>⚡ {skill}</p>", unsafe_allow_html=True)
        st.progress(value)

with col2:
    st.markdown("""
    <div class='card'>
        <h2>🚀 Advanced Skills</h2>
        <p>Skills that represent my creativity and logical thinking.</p>
    </div>
    """, unsafe_allow_html=True)

    for skill, value in list(skills.items())[3:]:
        st.markdown(f"<p class='skill-label'>⚡ {skill}</p>", unsafe_allow_html=True)
        st.progress(value)

st.write("")

st.success("Keep learning. Keep coding. Keep growing 🚀")