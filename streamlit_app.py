import streamlit as st

# Set page config
st.set_page_config(page_title="To My Favorite Person", layout="centered")

# Custom CSS for the "Alive" Interface
st.markdown("""
    <style>
    /* 1. Background Image Setup */
    .stApp {
        background: url("https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/valentine-2026/main/bg.jpg");
        background-size: cover;
        background-position: center;
    }

    /* 2. The Glass Container Design */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        margin: auto;
        margin-top: 100px;
        max-width: 550px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        animation: fadeIn 2s ease-in;
    }

    /* 3. Text Styling to match the Image */
    .title { color: white; font-family: 'Helvetica', sans-serif; font-size: 38px; font-weight: bold; margin-bottom: 5px; }
    .subtitle { color: white; font-size: 24px; margin-bottom: 15px; }
    .message { color: rgba(255, 255, 255, 0.8); font-size: 15px; line-height: 1.4; margin-bottom: 25px; }

    /* 4. Button Interface Styling */
    div.stButton > button {
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border: 1px solid white !important;
        border-radius: 10px !important;
        width: 140px;
        height: 45px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff4b6b !important;
        transform: scale(1.05);
    }

    /* 5. Animations to make it "Alive" */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>

    <div class="glass-card">
        <div class="title">To My Favorite Person...</div>
        <div class="subtitle">You're My Home.</div>
        <div class="message">
            You are the best thing that ever happened to me.<br>
            Every moment with you feels like a beautiful dream.<br>
            I love you more than words can express.
        </div>
        <div style="color: white; font-weight: bold; margin-bottom: 20px;">Forever yours.</div>
    </div>
    """, unsafe_allow_html=True)

# 3. Functional Buttons
st.write("") # Spacer
col1, col2 = st.columns([1, 1])

with col1:
    # Centering the button inside the column layout
    st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("Yes, Always"):
        st.balloons()
        st.snow()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.button("No"):
        st.toast("Error 404: 'No' is not an option! 😉")
