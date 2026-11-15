import streamlit as st
import base64, os

st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

# Agar bg.jpg hai to wo lagao, nahi hai to gradient lagao - error kabhi nahi aye ga
bg_css = ""
if os.path.exists("bg.jpg"):
    with open("bg.jpg","rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    bg_css = f'background-image: url("data:image/jpg;base64,{b64}"); background-size: cover; background-position: center;'
else:
    bg_css = 'background: radial-gradient(circle at 50% 20%, #4a2c12 0%, #241407 35%, #111111 70%, #000000 100%);'

st.markdown(f"""
<style>
.stApp {{{bg_css}}}
header, footer, [data-testid="stToolbar"] {{display:none !important;}}
.block-container {{max-width: 560px !important; padding-top: 20px !important;}}
div[data-testid="stTextInput"] label {{color:white !important; font-weight:800 !important;}}
div[data-testid="stTextInput"] > div {{background: rgba(255,255,255,0.95) !important; border:2px solid #d4af37 !important; border-radius:18px !important;}}
div[data-testid="stTextInput"] input {{color:black !important; font-size:18px !important; text-align:center !important;}}
div.stButton > button {{
    width:100% !important; height:65px !important; border-radius:50px !important;
    background: linear-gradient(90deg, #6b3a00, #d4af37) !important;
    color:white !important; font-size:26px !important; font-weight:900 !important; letter-spacing:4px !important;
    border:1px solid #ffe27a !important;
}}
</style>
""", unsafe_allow_html=True)

# Agar bg.jpg nahi hai to upar Uqab + Title dikhao, agar hai to sirf input dikhao
if not os.path.exists("bg.jpg"):
    st.markdown('<div style="text-align:center; font-size:110px;">🦅</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#e8b923; font-size:62px; font-weight:900; margin:0; text-shadow:0 0 20px #ffcc00;">UQABOOT</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:white; font-weight:700;">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Enter your username")
st.text_input("PASSWORD", type="password", placeholder="Enter your password")
if st.button("LOGIN"):
    st.success("Welcome - UQABOOT me Khush Amdeed 🦅")
