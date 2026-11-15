import streamlit as st

st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp {background: radial-gradient(circle at 50% 20%, #4a2c12 0%, #241407 35%, #111111 70%, #000000 100%);}
header, footer, [data-testid="stToolbar"] {display:none !important;}
.block-container {max-width: 600px !important; padding-top: 5px !important;}
h1, p {text-align:center !important;}
div[data-testid="stTextInput"] label {color:white !important; font-weight:800 !important; text-align:left !important;}
div[data-testid="stTextInput"] > div {background:#fff8e6 !important; border:2px solid #d4af37 !important; border-radius:12px !important;}
div[data-testid="stTextInput"] input {text-align:center !important; font-size:18px !important; color:black !important;}

/* BUTTON KO BARA KARNE KE LIYE */
div.stButton {display:flex; justify-content:center;}
div.stButton > button {
    width: 420px !important; max-width: 95% !important; height: 62px !important;
    background: linear-gradient(90deg, #6b3a00, #e8b923, #6b3a00) !important;
    color: white !important; font-size: 24px !important; font-weight: 900 !important;
    letter-spacing: 5px !important; border-radius: 14px !important;
    border: 2px solid #ffe27a !important; margin-top: 10px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; font-size:130px; line-height:1;">🦅</div>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#e8b923; font-size:64px; font-weight:900; margin:0; text-shadow:0 0 20px #ffcc00;">UQABOOT</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:white; font-weight:700; font-size:16px; margin:5px;">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#f0e6d2; font-size:16px;">Rawalpindi Region • Criminal Tracking</p>', unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Username likhein")
st.text_input("PASSWORD", type="password", placeholder="Password likhein")

# Button ko beech me lane ke liye column
c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    login = st.button("LOGIN")

if login:
    st.success("Welcome - UQABOOT me Khush Amdeed 🦅")

st.markdown('<p style="color:#d4af37; font-weight:700; margin-top:15px;">🦅 UQABOOT - Punjab Police • Secure System 🦅</p>', unsafe_allow_html=True)
