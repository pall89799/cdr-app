import streamlit as st, os
st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp {background: radial-gradient(circle at 50% 0%, #0b2a9e 0%, #071a6b 30%, #020a2e 65%, #000000 100%);}
header, footer, [data-testid="stToolbar"] {display:none !important;}
.block-container {max-width: 560px !important; margin: auto !important; padding-top: 10px !important;}

div[data-testid="stImage"] {display:flex !important; justify-content:center !important; width:100% !important;}
div[data-testid="stImage"] img {
    width: 260px !important; height: 260px !important;
    object-fit: cover !important;
    border-radius: 50% !important;
    border: 4px solid #e8b923 !important;
    box-shadow: 0 0 30px #ffcc00 !important;
    margin: auto !important;
}
div[data-testid="stTextInput"] label {color:white !important; font-weight:800 !important;}
div[data-testid="stTextInput"] > div {background: rgba(255,255,255,0.95) !important; border:2px solid #d4af37 !important; border-radius:18px !important;}
div[data-testid="stTextInput"] input {color:black !important; font-size:18px !important; text-align:center !important;}

/* LOGIN BUTTON - Picture jaisa */
div.stButton {display:flex !important; justify-content:center !important;}
div.stButton > button {
    width: 340px !important; height: 78px !important; border-radius: 50px !important;
    background: linear-gradient(90deg, #5a1a00, #8b2a00, #b33a00, #8b2a00, #5a1a00) !important;
    color:white !important; font-size:30px !important; font-weight:900 !important; letter-spacing:6px !important;
    border: 4px solid #e8b923 !important;
    box-shadow: 0 0 25px #ffcc00, 0 5px 15px rgba(0,0,0,0.5) !important;
}
div.stButton > button:hover {transform: scale(1.05) !important; box-shadow: 0 0 40px #ffcc00 !important;}
</style>
""", unsafe_allow_html=True)

if os.path.exists("eagle.png"):
    st.image("eagle.png")
elif os.path.exists("eagle.jpg"):
    st.image("eagle.jpg")
else:
    st.markdown('<div style="text-align:center; font-size:110px;">🦅</div>', unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#e8b923; font-size:58px; font-weight:900; margin:0; text-shadow:0 0 20px #ffcc00;">UQABOOT</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-weight:700;">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#d0d8ff;">Rawalpindi Region • Criminal Tracking</p>', unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Enter your username")
st.text_input("PASSWORD", type="password", placeholder="Enter your password")
if st.button("LOGIN"):
    st.success("Welcome - UQABOOT me Khush Amdeed 🦅")
