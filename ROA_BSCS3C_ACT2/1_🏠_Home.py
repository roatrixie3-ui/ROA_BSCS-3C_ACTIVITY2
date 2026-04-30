import streamlit as st

st.set_page_config(
    page_title="Novie Roa Portfolio",
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
    background: linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#00c9ff,#00ffcc);
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
    font-size: 70px;
    color: #00ffff;
    text-shadow: 0 0 20px #00ffff, 0 0 40px #0088ff;
    letter-spacing: 4px;
}

/* 🌟 SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #b3f0ff;
}

/* 🧊 BOX DESIGN (GLASS CARD) */
.box {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(0,255,255,0.3);
    padding: 20px;
    margin: 12px 0;
    border-radius: 18px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 20px rgba(0,255,255,0.2);
    transition: 0.4s;
    animation: float 4s ease-in-out infinite;
}

.box:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 40px rgba(0,255,255,0.7);
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* 🔘 BUTTON */
.stButton > button {
    background: linear-gradient(90deg, #00ffff, #0088ff);
    color: black;
    font-weight: bold;
    border-radius: 20px;
    padding: 10px 20px;
    border: none;
    box-shadow: 0 0 15px #00ffff;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px #00ffff;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------
st.markdown("<h1 class='title'>MY HOME</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>🚀 Futuristic Portfolio | BS Computer Science Student</p>", unsafe_allow_html=True)

# ----------------------------
# COLUMN LAYOUT
# ----------------------------
col1, col2 = st.columns([2,1])

with col1:

    st.markdown("""
    <div class='box'>
        <h2>👋 Welcome to My Digital Universe</h2>
        <p>Hi! I'm <b>Novie Roa</b>, a passionate 3rd Year BS Computer Science student.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
        <h3>💻 Specialization</h3>
        <p>Python Development • UI/UX Design • Web Applications</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
        <h3>🎯 My Goals</h3>
        <p>✔ Become a Professional Software Developer</p>
        <p>✔ Build impactful tech solutions</p>
        <p>✔ Master Full Stack Development</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
        <h3>⚡ Interests</h3>
        <p>Artificial Intelligence • Web Development • Cybersecurity • UI/UX Design</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("assets/ROA_PICTURE1.jpg", width=320, caption="Novie Roa")

# ----------------------------
# BUTTON
# ----------------------------
st.write("")

if st.button("✨ Activate Future Mode"):
    st.success("🚀 Future Mode Activated!")
    st.balloons()

# ----------------------------
# QUICK PROFILE BOX
# ----------------------------
st.write("")

st.markdown("""
<div class='box'>
<h2>📌 Quick Profile</h2>
<p>🎓 Course: Bachelor of Science in Computer Science</p>
<p>🏫 Year: 3rd Year College</p>
<p>🌍 Location: Philippines</p>
<p>💡 Motto: Code your future, build your destiny.</p>
</div>
""", unsafe_allow_html=True)