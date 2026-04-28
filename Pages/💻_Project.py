import streamlit as st

st.set_page_config(
    page_title="My Projects",
    page_icon="💻",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

/* BACKGROUND (same style as your portfolio) */
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
    margin-top: 50px;
    animation: fadeIn 1s ease;
}

/* PROJECT GRID */
.project-container {
    max-width: 900px;
    margin: 40px auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

/* PROJECT CARD */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 25px;
    color: #e0e0e0;
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    transition: 0.3s ease;
    animation: fadeIn 1s ease;
}

/* HOVER EFFECT */
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 25px #ffb199, 0 0 40px #ff4d6d;
}

/* PROJECT TITLE */
.card h3 {
    color: #ffb199;
    margin-bottom: 10px;
}

/* FADE ANIMATION */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .title {
        font-size: 40px;
    }

    .card {
        padding: 20px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">💻 My Projects</div>', unsafe_allow_html=True)

# ---------- PROJECTS ----------
st.markdown("""
<div class="project-container">
    <div class="card">
        <h3>E-Attendance Navigator</h3>
        <p>Smart attendance system with automated reports and tracking features.</p>
    </div>
    <div class="card">
        <h3>SAOD Web App</h3>
        <p>A web platform that promotes local products and supports small businesses.</p>
    </div>
    <div class="card">
        <h3>Banking System</h3>
        <p>A simple banking system that handles transactions and basic analytics.</p>
    </div>
</div>
""", unsafe_allow_html=True)