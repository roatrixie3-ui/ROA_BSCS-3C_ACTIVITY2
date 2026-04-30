import streamlit as st
from PIL import Image

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Gallery - Novie Roa",
    page_icon="🖼️",
    layout="wide"
)

# ----------------------------
# FUTURISTIC DESIGN CSS
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* 🌌 Animated Background */
.stApp {
    background: linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#00c9ff);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ TITLE */
h1 {
    text-align: center;
    color: #00ffff;
    text-shadow: 0 0 15px #00ffff, 0 0 30px #0088ff;
    font-size: 55px;
}

/* 📌 CAPTION */
.caption {
    text-align: center;
    color: #b3f0ff;
    font-size: 18px;
}

/* 🧊 IMAGE HOVER EFFECT */
img {
    border-radius: 15px;
    transition: 0.4s;
    box-shadow: 0 0 15px rgba(0,255,255,0.3);
}

img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px #00ffff;
}

/* 🔘 RADIO BUTTON STYLE */
.stRadio > div {
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------
st.markdown("<h1>📸 MY FUTURISTIC GALLERY</h1>", unsafe_allow_html=True)
st.markdown("<p class='caption'>A collection of my memories, snapshots, and portfolio moments</p>", unsafe_allow_html=True)

st.divider()

# ----------------------------
# LOAD IMAGES
# ----------------------------
img1 = Image.open("ROA_BSCS3C_ACT2/pages/ROA_PICTURE1.jpg")
img2 = Image.open("ROA_BSCS3C_ACT2/pages/ROA_PICTURE2.jpg")
img3 = Image.open("assets/ROA_PICTURE3.jpg")
img4 = Image.open("assets/ROA_PICTURE4.jpg")
img5 = Image.open("assets/ROA_PICTURE5.jpg")
img6 = Image.open("assets/ROA_PICTURES6.jpg")  # FIXED

# ----------------------------
# VIEW MODE
# ----------------------------
view = st.radio("⚡ Choose View Mode:", ["Grid View", "Single Preview"])

# ----------------------------
# GRID VIEW
# ----------------------------
if view == "Grid View":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(img1, caption="Photo 1", use_container_width=True)
        st.image(img4, caption="Photo 4", use_container_width=True)

    with col2:
        st.image(img2, caption="Photo 2", use_container_width=True)
        st.image(img5, caption="Photo 5", use_container_width=True)

    with col3:
        st.image(img3, caption="Photo 3", use_container_width=True)
        st.image(img6, caption="Photo 6", use_container_width=True)

# ----------------------------
# SINGLE PREVIEW
# ----------------------------
else:
    selected = st.selectbox(
        "Select Image:",
        ["Photo 1","Photo 2","Photo 3","Photo 4","Photo 5","Photo 6"]
    )

    images = {
        "Photo 1": img1,
        "Photo 2": img2,
        "Photo 3": img3,
        "Photo 4": img4,
        "Photo 5": img5,
        "Photo 6": img6,
    }

    st.image(images[selected], use_container_width=True)

# ----------------------------
# FOOTER
# ----------------------------
st.divider()
st.success("🚀 More futuristic memories coming soon...")
