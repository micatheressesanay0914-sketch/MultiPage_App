import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Mica Theresse Sanay | Portfolio",
    page_icon="✨",
    layout="wide"
)

# 1. Global Theme and Floating Bubbles (CSS/JS Injection)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&display=swap');

    /* Main App Background */
    .stApp {
        background-color: #FDF0F5;
        font-family: 'Fredoka', sans-serif;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #F7D9E3 !important;
        border-right: 5px solid #B19CD9;
    }
    
    /* Sidebar Text/Labels */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #7B61FF !important;
        font-weight: 600;
        font-size: 18px;
    }

    h1, h2 {
        color: #B19CD9 !important;
    }

    h3 {
        color: #7B61FF !important;
    }
            
    .main .block-container {
        padding-top: 5rem;
        z-index: 1;
    }

    /* Bubbles Animation */
    .bubbles-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        overflow: hidden;
        pointer-events: none; 
    }

    .bubble {
        position: absolute;
        bottom: -150px;
        background: rgba(255, 183, 206, 0.4);
        border-radius: 50%;
        opacity: 0.6;
        animation: float 15s infinite ease-in;
    }

    .bubble:nth-child(even) {
        background: rgba(177, 156, 217, 0.4);
    }

    @keyframes float {
        0% { transform: translateY(0) translateX(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.6; }
        50% { transform: translateY(-50vh) translateX(50px) rotate(180deg); }
        90% { opacity: 0.6; }
        100% { transform: translateY(-120vh) translateX(-20px) rotate(360deg); opacity: 0; }
    }

    /* Hero Text & Image Styling */
    .hero-text h1 {
        font-family: 'Fredoka', sans-serif !important;
        color: #B19CD9 !important;
        font-size: 75px !important; 
        margin-bottom: -10px !important;
        font-weight: 600 !important;
        line-height: 1.1;
    }

    .profile-container {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }

    .stImage img {
        border-radius: 50px 50px 100px 100px !important;
        border: 8px solid #B19CD9 !important;
        box-shadow: 15px 15px 0px #FFB7CE !important;
        width: 380px !important;
        transition: 0.4s ease-in-out;
    }
    
    .stImage img:hover {
        transform: rotate(-3deg) scale(1.05);
    }
    </style>

    <div class="bubbles-container">
        <div class="bubble" style="width: 60px; height: 60px; left: 5%; animation-delay: 0s;"></div>
        <div class="bubble" style="width: 100px; height: 100px; left: 15%; animation-delay: 2s;"></div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    st.markdown("## 🎀 Navigation")
    page = st.radio("Go to:", ["Home", "Projects", "About Me", "Contact"])
    
    st.markdown("---")
    st.markdown("### 💻 Tech Stack")
    st.info("Python • Streamlit • CSS")
    
    st.markdown("### ✨ Socials")
    st.write("🔗 [LinkedIn](#)")
    st.write("🐙 [GitHub](#)")

# --- MAIN CONTENT ---
if page == "Home":
    col1, col2 = st.columns([1.2, 1], gap="large")

    with col1:
        st.markdown('<div class="hero-text">', unsafe_allow_html=True)
        st.markdown("<h1>Hi, I'm Mica Theresse Sanay</h1>", unsafe_allow_html=True)
        st.markdown("<h3>Bachelor of Science in Computer Science</h3>", unsafe_allow_html=True)
        st.markdown("<p>I am a BS Computer Science student passionate about building modern applications and exploring new technologies.</p>", unsafe_allow_html=True)
        
        if st.button("Contact Me"):
            st.toast("Let's get in touch!", icon="✉️")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        # Ensure the path to your image is correct
        st.image("images/mica.png")
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "Projects":
    st.title("My Projects")
    st.write("Coming soon! I'm currently working on some exciting new tech.")
