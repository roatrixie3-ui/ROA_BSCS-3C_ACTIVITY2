import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="About Novie Roa",
    page_icon="👨‍💻",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Orbitron', sans-serif;
}

/* 🌌 ANIMATED BACKGROUND */
.stApp{
    background: linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#00c9ff,#00ffcc);
    background-size: 400% 400%;
    animation: bg 12s ease infinite;
    color:white;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* ✨ TITLE */
.title{
    text-align:center;
    font-size:65px;
    color:#00ffff;
    text-shadow:0 0 20px #00ffff, 0 0 40px #0088ff;
}

/* 🧊 BOX STYLE */
.box{
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(0,255,255,0.3);
    padding: 18px 20px;
    margin: 10px 0;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 15px rgba(0,255,255,0.2);
    transition: 0.3s;
}

.box:hover{
    transform: translateY(-5px);
    box-shadow: 0 0 35px rgba(0,255,255,0.6);
}

/* 🖼 IMAGE */
img{
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,255,255,0.4);
    transition: 0.4s;
}

img:hover{
    transform: scale(1.05);
    box-shadow: 0 0 45px #00ffff;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------
st.markdown("<h1 class='title'>👨‍💻 ABOUT ME</h1>", unsafe_allow_html=True)

# ----------------------------
# LAYOUT
# ----------------------------
col1, col2 = st.columns([1,2])

with col1:
    image = Image.open("ROA_BSCS3C_ACT2/pages/ROA_PICTURE2.jpg")
    st.image(image, use_container_width=True)

with col2:

    st.markdown("""
    <div class='box'>
    <h2>🚀 PERSONAL INFORMATION</h2>
    <p><b>Name:</b> Novie Roa</p>
    <p><b>Course:</b> Bachelor of Science in Computer Science</p>
    <p><b>Year:</b> 3rd Year College Student</p>
    <p><b>Address:</b> Maolingon, Mandaon, Masbate</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
    <h2>💡 ABOUT ME</h2>
    <p>I am a passionate Computer Science student who enjoys coding, designing, and building modern applications.</p>
    <p>I love turning ideas into real digital systems using technology.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
    <h2>🎯 GOALS</h2>
    <p>✔ Become a Software Engineer</p>
    <p>✔ Master Full Stack Development</p>
    <p>✔ Work in the tech industry</p>
    <p>✔ Build impactful systems</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
    <h2>⚡ SKILLS INTEREST</h2>
    <p>Python • Web Development • UI/UX • Database • AI</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
    <h2>🔥 MOTTO</h2>
    <p><i>"Code the future, build your destiny."</i></p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# FOOTER
# ----------------------------
st.write("")
st.success("✨ Futuristic profile structured in cyber boxes 🚀")
