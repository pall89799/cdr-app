import streamlit as st, os
st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp {background: radial-gradient(circle at 50% 0%, #0b2a9e 0%, #071a6b 30%, #020a2e 65%, #000000 100%);}
header, footer, [data-testid="stToolbar"] {display:none !important;}
.block-container {max-width: 560px !important; margin: auto !important; padding-top: 10px !important;}
div[data-testid="stTextInput"] label {color:white !important; font-weight:800 !important;}
div[data-testid="stTextInput"] > div {background: rgba(255,255,255,0.95) !important; border:2px solid #d4af37 !important; border-radius:18px !important;}
div[data-testid="stTextInput"] input {color:black !important; font-size:18px !important; text-align:center !important;}
div.stButton > button {
    width:100% !important; height:78px !important; border-radius:50px !important;
    background: linear-gradient(90deg, #5a1a00, #8b2a00, #b33a00, #8b2a00, #5a1a00) !important;
    color:white !important; font-size:30px !important; font-weight:900 !important; letter-spacing:6px !important;
    border: 4px solid #e8b923 !important;
    box-shadow: 0 0 25px #ffcc00 !important;
}
</style>
""", unsafe_allow_html=True)

# 1. PIC CENTER - columns se
p1, p2, p3 = st.columns([1, 2, 1])
with p2:
    if os.path.exists("eagle.png"):
        st.image("eagle.png", use_container_width=True)
    elif os.path.exists("eagle.jpg"):
        st.image("eagle.jpg", use_container_width=True)

st.markdown('<h1 style="text-align:center; color:#e8b923; font-size:58px; font-weight:900; margin:0; text-shadow:0 0 20px #ffcc00;">UQABOOT</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-weight:700;">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#d0d8ff;">Rawalpindi Region • Criminal Tracking</p>', unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Enter your username")
st.text_input("PASSWORD", type="password", placeholder="Enter your password")

# 2. BUTTON CENTER - columns se
b1, b2, b3 = st.columns([1, 2, 1])
with b2:
    if st.button("LOGIN"):
        st.success("Welcome - UQABOOT me Khush Amdeed 🦅")
