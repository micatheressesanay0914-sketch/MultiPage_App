import streamlit as st

st.set_page_config(
    page_title="Contact Me",
    page_icon="📞",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

/* BACKGROUND */
.stApp {
    background: linear-gradient(-45deg, #141e30, #243b55, #1f1c2c, #2c3e50);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
    font-family: 'Barlow', sans-serif;
}

/* BACKGROUND ANIMATION */
@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* TITLE */
.title {
    text-align: center;
    font-size: 55px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    margin-top: 40px;
}

/* CENTER FORM + SMALL SIZE */
.block-container {
    max-width: 520px;
    padding-top: 10px;
}

/* INPUT BOX SMALL */
input, textarea {
    color: black !important;              /* FIX: BLACK TEXT */
    background: rgba(255,255,255,0.85) !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: 10px !important;
    padding: 8px !important;
    font-size: 14px !important;
}

/* PLACEHOLDER */
input::placeholder, textarea::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

/* FOCUS EFFECT */
input:focus, textarea:focus {
    box-shadow: 0 0 12px #ff4d6d !important;
    border: 1px solid #ff4d6d !important;
    outline: none !important;
}

/* LABELS */
label {
    color: #ffffff !important;
    font-size: 14px !important;
}

/* BUTTON */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ff4d6d, #ffb199);
    color: white;
    border: none;
    padding: 10px;
    font-weight: bold;
    border-radius: 10px;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px #ff4d6d;
}

/* SOCIAL */
.social {
    text-align: center;
    margin-top: 30px;
    color: #e0e0e0;
}

a {
    color: #ffb199 !important;
    text-decoration: none;
}

/* FADE */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .title {
        font-size: 38px;
    }

    .block-container {
        max-width: 95%;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">📞 Contact Me</div>', unsafe_allow_html=True)

# ---------- FORM ----------
name = st.text_input("Name", placeholder="Enter your name")
email = st.text_input("Email", placeholder="Enter your email")
message = st.text_area("Message", placeholder="Write your message...")

if st.button("Send Message"):
    if name and email and message:
        st.success("✅ Message sent successfully!")
    else:
        st.warning("⚠️ Please complete all fields.")

# ---------- SOCIAL ----------
st.markdown("""
<div class="social">

<h3 style="color:#ffb199;">🌐 Social Links</h3>

<p>
<a href="https://github.com/" target="_blank">GitHub</a><br>
<a href="https://facebook.com/" target="_blank">Facebook</a>
</p>

</div>
""", unsafe_allow_html=True)