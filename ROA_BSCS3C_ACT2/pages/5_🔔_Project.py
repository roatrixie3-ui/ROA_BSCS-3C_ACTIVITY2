import streamlit as st

st.set_page_config(
    page_title="Projects - Novie Roa",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* 🌌 ANIMATED BACKGROUND */
.stApp {
    background: linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#00c9ff);
    background-size: 400% 400%;
    animation: bgmove 10s ease infinite;
    color: white;
}

@keyframes bgmove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ TITLE */
.title {
    text-align: center;
    font-size: 65px;
    color: #00ffff;
    text-shadow: 0 0 15px #00ffff, 0 0 35px #0088ff;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {opacity: 0.7;}
    to {opacity: 1;}
}

/* 🧊 FLOATING CARD */
.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(0,255,255,0.3);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 25px rgba(0,255,255,0.2);
    transition: 0.4s;
    animation: float 4s ease-in-out infinite;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 50px rgba(0,255,255,0.7);
}

/* 🌊 FLOAT EFFECT */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* 🔘 INPUT */
input {
    background: rgba(0,0,0,0.5) !important;
    color: white !important;
    border: 1px solid #00ffff !important;
    border-radius: 10px !important;
}

/* 🚀 BUTTON */
.stButton > button {
    background: linear-gradient(90deg, #00ffff, #0077ff);
    color: black;
    font-weight: bold;
    border-radius: 20px;
    padding: 10px 20px;
    border: none;
    box-shadow: 0 0 15px #00ffff;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px #00ffff;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------
st.markdown("<h1 class='title'>🚀 MY PROJECTS</h1>", unsafe_allow_html=True)

st.write("")

# ----------------------------
# PROJECT INTRO
# ----------------------------
st.markdown("""
<div class='card'>
<h2>💡 About My Projects</h2>
<p>These projects represent my journey as a Computer Science student.</p>
<p>I focus on building systems that are useful, modern, and user-friendly.</p>
<p>Each project reflects my skills in programming, design, and problem solving.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------
# PROJECT GRID
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
        <h3>💻 Student Management System</h3>
        <p>Manages student records, grades, and academic data efficiently.</p>
        <p><b>Tech:</b> Python, Database</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <h3>📊 Attendance Monitoring System</h3>
        <p>Tracks attendance digitally and generates reports automatically.</p>
        <p><b>Tech:</b> Python, File Handling</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h3>🌐 Portfolio Website</h3>
        <p>A futuristic personal portfolio built using Streamlit.</p>
        <p><b>Tech:</b> Python, Streamlit, CSS</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <h3>🧮 Calculator App</h3>
        <p>A simple calculator that performs basic arithmetic operations.</p>
        <p><b>Tech:</b> Python</p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# SUGGESTION BOX
# ----------------------------
st.write("")

st.markdown("""
<div class='card'>
<h2>💡 Suggest a New Project</h2>
<p>Share your ideas and help improve future systems.</p>
</div>
""", unsafe_allow_html=True)

project = st.text_input("Enter your project idea")

if st.button("🚀 Submit Idea"):
    if project:
        st.success(f"✨ Awesome idea: '{project}' added to innovation list!")
    else:
        st.error("Please enter a project idea first.")

# ----------------------------
# FOOTER
# ----------------------------
st.write("")
st.info("🚀 Keep building. Keep innovating. The future is yours.")