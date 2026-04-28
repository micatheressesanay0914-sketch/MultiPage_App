import streamlit as st

st.set_page_config(
    page_title="Skills",
    page_icon="🧠",
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
    font-size: 60px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    margin-top: 40px;
    animation: fadeIn 1s ease;
}

/* CLEAN CONTENT (NO BOX / NO CARD) */
.content {
    max-width: 700px;
    margin: auto;
    padding: 20px;
    animation: fadeIn 1s ease;
}

/* HEADINGS ONLY */
h3 {
    color: #ffb199 !important;
    margin-top: 25px;
}

/* TEXT */
p, div, span {
    color: #e0e0e0 !important;
}

/* PROGRESS BAR */
.stProgress > div > div > div {
    background: linear-gradient(135deg, #ff4d6d, #ffb199);
}

/* FADE */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .title {
        font-size: 40px;
    }

    .content {
        padding: 10px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">🧠 Skills</div>', unsafe_allow_html=True)

# ---------- CONTENT ----------
st.markdown('<div class="content">', unsafe_allow_html=True)

st.subheader("💻 Programming Skills")

st.write("Python")
st.progress(80)

st.write("JavaScript")
st.progress(70)

st.write("PHP")
st.progress(75)

st.subheader("🎨 Design Skills")

st.write("Canva / UI Design")
st.progress(85)

st.subheader("🛠 Tools")

st.write("• GitHub")
st.write("• VS Code")
st.write("• Streamlit")

st.markdown('</div>', unsafe_allow_html=True)