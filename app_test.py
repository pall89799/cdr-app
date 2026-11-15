import streamlit as st

st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp {background: radial-gradient(circle at 50% 20%, #4a2c12 0%, #241407 35%, #111111 70%, #000000 100%);}
header, footer, [data-testid="stToolbar"] {display:none !important;}
.block-container {max-width: 600px !important; padding-top: 0px !important;}
div[data-testid="stTextInput"] label {color:white !important; font-weight:800 !important;}
div[data-testid="stTextInput"] > div {background:#fff8e6 !important; border:2px solid #d4af37 !important; border-radius:12px !important;}
div[data-testid="stTextInput"] input {text-align:center !important; font-size:18px !important; color:black !important;}
div.stButton > button {
    width: 100% !important; height: 62px !important;
    background: linear-gradient(90deg, #6b3a00, #e8b923, #6b3a00) !important;
    color: white !important; font-size: 24px !important; font-weight: 900 !important;
    letter-spacing: 5px !important; border-radius: 14px !important;
    border: 2px solid #ffe27a !important;
}
</style>
""", unsafe_allow_html=True)

st.image("eagle.png", width=340)
st.markdown('<h1 style="text-align:center; color:#e8b923; font-size:62px; font-weight:900; margin:0; text-shadow:0 0 20px #ffcc00;">UQABOOT</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-weight:700;">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#f0e6d2;">Rawalpindi Region • Criminal Tracking</p>', unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Username likhein")
st.text_input("PASSWORD", type="password", placeholder="Password likhein")

if st.button("LOGIN"):
    st.success("Welcome - UQABOOT me Khush Amdeed 🦅")

st.markdown('<p style="text-align:center; color:#d4af37; font-weight:700;">🦅 UQABOOT - Punjab Police • Secure System 🦅</p>', unsafe_allow_html=True)
