import streamlit as st
import base64
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Mica Theresse Sanay | Portfolio",
    page_icon="💼",
    layout="wide"
)

# ---------- LOAD IMAGE FUNCTION ----------
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_base64 = get_base64_image("images/mica.jpg")

# ---------- CUSTOM CSS STYLES ----------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

/* Dynamic Background */
.stApp {{
    background: linear-gradient(-45deg, #141e30, #243b55, #1f1c2c, #2c3e50);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
}}

@keyframes bgMove {{
    0% {{background-position: 0% 50%;}}
    50% {{background-position: 100% 50%;}}
    100% {{background-position: 0% 50%;}}
}}

/* Hero Section Styling */
.hero-container {{
    text-align: center;
    padding-top: 60px;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

/* PROFILE IMAGE - PERFECT CIRCLE FIX */
.profile-img {{
    width: 220px;
    height: 220px;
    aspect-ratio: 1 / 1;        /* Sinisiguro na square ang ratio */
    border-radius: 50%;         /* Ginagawang bilog ang square */
    border: 6px solid #ffb199;
    object-fit: cover;          /* Hindi maba-banat ang image */
    object-position: center top; 
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    position: relative;
    z-index: 10;
    margin-bottom: -110px;      /* Offset para pumatong sa banner */
    transition: transform 0.3s ease;
    background-color: #243b55;   /* Fallback color habang naglo-load */
}}

.profile-img:hover {{
    transform: scale(1.08);
}}

.banner-wrapper {{
    width: 85%;
    max-width: 900px;
    margin: 0 auto;
    padding: 130px 30px 60px 30px;
    border-radius: 25px;
    text-align: center;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 25px 70px rgba(0,0,0,0.5);
    animation: fadeIn 1.2s ease;
}}

@keyframes fadeIn {{
    from {{opacity: 0; transform: translateY(30px);}}
    to {{opacity: 1; transform: translateY(0);}}
}}

.banner-headline {{
    font-size: clamp(35px, 8vw, 70px);
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
}}

.intro {{
    max-width: 750px;
    margin: 0 auto;
    text-align: center;
    color: #e0e0e0;
    font-size: 20px;
    line-height: 1.8;
    font-family: 'Barlow', sans-serif;
}}

.highlight {{
    color: #ffb199;
    font-weight: 700;
}}

/* Mobile Responsiveness */
@media (max-width: 768px) {{
    .profile-img {{
        width: 160px;
        height: 160px;
        margin-bottom: -80px;
    }}
    .banner-wrapper {{
        padding-top: 100px;
        width: 95%;
    }}
    .intro {{
        font-size: 16px;
    }}
}}
</style>
""", unsafe_allow_html=True)

# ---------- RENDER INTERFACE ----------

# Main Hero UI
st.markdown(f"""
<div class="hero-container">
    <img src="data:image/jpeg;base64,{img_base64}" class="profile-img" alt="Mica's Profile">
    <div class="banner-wrapper">
        <div class="banner-headline">
            Mica Theresse V. Sanay
        </div>
        <div class='intro'>
            Hello! I am a <span class='highlight'>BS Computer Science student</span> passionate about building modern applications and exploring new technologies.
            <br><br>
            I enjoy designing clean user interfaces and developing functional systems using Python and web technologies.
            <br>
            Feel free to explore my portfolio and see my work.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Add some breathing room at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
