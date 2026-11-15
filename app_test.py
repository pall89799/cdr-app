import streamlit as st
st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp {background: radial-gradient(circle at 50% 15%, #2a1a05 0%, #1a0f05 30%, #0d0d0d 65%, #000000 100%);}
header, footer, [data-testid="stToolbar"] {display:none !important;}
.block-container {max-width: 560px !important; padding-top: 10px !important;}
div[data-testid="stTextInput"] label {color:white !important; font-weight:800 !important;}
div[data-testid="stTextInput"] > div {background: rgba(255,255,255,0.95) !important; border:2px solid #d4af37 !important; border-radius:18px !important;}
div[data-testid="stTextInput"] input {color:black !important; font-size:18px !important; text-align:center !important;}
div.stButton > button {
    width:100% !important; height:65px !important; border-radius:50px !important;
    background: linear-gradient(90deg, #6b3a00, #e8b923, #6b3a00) !important;
    color:white !important; font-size:26px !important; font-weight:900 !important; letter-spacing:4px !important;
    border:1px solid #ffe27a !important;
}
</style>
""", unsafe_allow_html=True)

# YEHI WALA UQAB
st.image("eagle.png", use_container_width=True)
st.markdown('<h1 style="text-align:center; color:#e8b923; font-size:62px; font-weight:900; margin:0; text-shadow:0 0 20px #ffcc00;">UQABOOT</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-weight:700;">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#f0e6d2;">Rawalpindi Region • Criminal Tracking</p>', unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Enter your username")
st.text_input("PASSWORD", type="password", placeholder="Enter your password")
if st.button("LOGIN"):
    st.success("Welcome - UQABOOT me Khush Amdeed 🦅")
