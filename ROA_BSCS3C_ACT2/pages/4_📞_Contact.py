import streamlit as st

st.set_page_config(
    page_title="Contact - Novie Roa",
    page_icon="📩",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* 🌌 ANIMATED CYBER BACKGROUND */
.stApp {
    background: linear-gradient(-45deg,#000428,#004e92,#0f2027,#2c5364);
    background-size: 400% 400%;
    animation: bgmove 10s ease infinite;
    color: white;
}

@keyframes bgmove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ TITLE GLOW ANIMATION */
.title {
    text-align: center;
    font-size: 65px;
    color: #00ffff;
    text-shadow: 0 0 15px #00ffff, 0 0 35px #0088ff;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from {opacity: 0.7; transform: scale(1);}
    to {opacity: 1; transform: scale(1.03);}
}

/* 🧊 FLOATING CARD */
.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(0,255,255,0.3);
    padding: 30px;
    border-radius: 25px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 25px rgba(0,255,255,0.25);
    transition: 0.4s;
    animation: float 4s ease-in-out infinite;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 50px rgba(0,255,255,0.7);
}

/* 🌊 FLOAT ANIMATION */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* 🔘 INPUT DESIGN */
input, textarea {
    background: rgba(0,0,0,0.5) !important;
    color: white !important;
    border: 1px solid #00ffff !important;
    border-radius: 12px !important;
    box-shadow: 0 0 10px rgba(0,255,255,0.2);
}

/* 🚀 BUTTON */
.stButton > button {
    background: linear-gradient(90deg, #00ffff, #0077ff);
    color: black;
    font-weight: bold;
    border-radius: 25px;
    padding: 10px 25px;
    border: none;
    box-shadow: 0 0 15px #00ffff;
    transition: 0.3s;
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
st.markdown("<h1 class='title'>📩 CONTACT ME</h1>", unsafe_allow_html=True)

# ----------------------------
# LAYOUT
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
        <h2>📡 Let's Connect</h2>
        <p>Feel free to reach out for collaboration, projects, or tech discussions.</p>
        <p>🚀 I am always open to new opportunities and ideas.</p>
        <p>💡 Let’s build something amazing together!</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    name = st.text_input("👤 Your Name")
    email = st.text_input("📧 Your Email")
    message = st.text_area("💬 Your Message")

    if st.button("🚀 Send Message"):
        if name and email and message:
            st.success("✨ Message sent successfully! I will get back to you soon 🚀")
        else:
            st.error("⚠ Please fill out all fields.")

# ----------------------------
# FOOTER INFO
# ----------------------------
st.write("")

st.markdown("""
<div class='card'>
<h3>📞 Contact Details</h3>
<p>📧 Email: novie.roa@email.com</p>
<p>📱 Phone: 0912-345-6789</p>
<p>📍 Location: Philippines</p>
</div>
""", unsafe_allow_html=True)