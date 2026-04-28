import streamlit as st
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Certificates - Mica",
    page_icon="🏆",
    layout="wide"
)

# ---------- STYLE (DARK & ANIMATED) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

.stApp {
    background: linear-gradient(-45deg, #141e30, #243b55, #1f1c2c, #2c3e50);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
    font-family: 'Barlow', sans-serif;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    margin-top: 40px;
    margin-bottom: 40px;
    animation: fadeIn 1s ease;
}

.content-wrapper {
    max-width: 850px;
    margin: auto;
    padding: 20px;
    animation: fadeIn 1.2s ease;
}

h4 {
    color: #ffb199 !important; /* Orange-Pink accent */
    font-family: 'Barlow Condensed', sans-serif;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 0px !important;
}

p, div, span {
    color: #e0e0e0 !important;
    font-size: 1.05rem;
}

.cert-divider {
    margin-bottom: 40px;
    padding-bottom: 20px;
    border-bottom: 1px solid rgba(255, 177, 153, 0.2);
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
.stImage img {
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    transition: transform 0.3s ease;
}

.stImage img:hover {
    transform: scale(1.02);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🏆 CERTIFICATES</div>', unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

def certificate_item(img_path, title, description, caption_text):
    if os.path.exists(img_path):
        with st.container():
            c1, c2 = st.columns([1, 1.4], gap="large")
            with c1:
                st.image(img_path, caption=caption_text, use_container_width=True)
            with c2:
                st.markdown(f"#### {title}")
                st.write(description)
            # Layout spacing
            st.markdown('<div class="cert-divider"></div>', unsafe_allow_html=True)

certificate_item(
    "images/cert1.jpg", 
    "Getting Started with Cisco Packet Tracer", 
    "Introductory certification on network simulation, configuration, and visualization using Cisco’s powerful networking tool.",
    "Cisco Packet Tracer Credential"
)

certificate_item(
    "images/cert2.jpg", 
    "What a Machine Learning Engineer's Work Day Looks Like", 
    "Masterclass completion focused on the professional workflows, industry tools, and day-to-day responsibilities of a Machine Learning Engineer.",
    "ML Engineer Masterclass"
)

certificate_item(
    "images/cert3.png", 
    "How to Master AI & Machine Learning in 2026", 
    "Specialized session on navigating the Generative AI landscape, focusing on applied Machine Learning techniques and the Michigan Applied GenAI Specialization curriculum.",
    "AI & ML Masterclass"
)

st.markdown('</div>', unsafe_allow_html=True)