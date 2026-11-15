import streamlit as st, os
st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp {background: radial-gradient(circle at 50% 0%, #0b2a9e 0%, #071a6b 30%, #020a2e 65%, #000000 100%);}
header, footer, [data-testid="stToolbar"] {display:none !important;}
.block-container {max-width: 560px !important; padding-top: 10px !important;}
div[data-testid="stTextInput"] label {color:white !important; font-weight:800 !important;}
div[data-testid="stTextInput"] > div {background: rgba(255,255,255,0.95) !important; border:2px solid #d4af37 !important; border-radius:18px !important;}
div[data-testid="stTextInput"] input {color:black !important; font-size:18px !important; text-align:center !important;}
div.stButton > button {
    width:100% !important; height:65px !important; border-radius:50px !important;
    background: linear-gradient(90deg, #6b3a00, #e8b923, #6b3a00) !important;
    color:white !important; font-size:26px !important; font-weight:900 !important; letter-spacing:4px !important;
}
</style>
""", unsafe_allow_html=True)

# پکچر چھوٹی کر کے بیچ میں
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if os.path.exists("eagle.png"):
        st.image("eagle.png", use_container_width=True)
    elif os.path.exists("eagle.jpg"):
        st.image("eagle.jpg", use_container_width=True)
    else:
        st.markdown('<div style="text-align:center; font-size:110px;">🦅</div>', unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#e8b923; font-size:58px; font-weight:900; margin:0; text-shadow:0 0 20px #ffcc00;">UQABOOT</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-weight:700;">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#d0d8ff;">Rawalpindi Region • Criminal Tracking</p>', unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Enter your username")
st.text_input("PASSWORD", type="password", placeholder="Enter your password")
if st.button("LOGIN"):
    st.success("Welcome - UQABOOT me Khush Amdeed 🦅")
