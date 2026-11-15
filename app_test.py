import streamlit as st, base64

st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

def get_bg():
    with open("bg.jpg","rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_bg()

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{bg}");
    background-size: cover; background-position: center; background-repeat: no-repeat;
}}
header, footer, [data-testid="stToolbar"] {{display:none !important;}}
.block-container {{max-width: 560px !important; padding-top: 380px !important;}}
div[data-testid="stTextInput"] label {{color:white !important; font-weight:800 !important;}}
div[data-testid="stTextInput"] > div {{background: rgba(255,255,255,0.12) !important; border:1.5px solid white !important; border-radius:18px !important; backdrop-filter: blur(5px);}}
div[data-testid="stTextInput"] input {{color:white !important; font-size:18px !important; text-align:center !important;}}
div[data-testid="stTextInput"] input::placeholder {{color:#cccccc !important;}}
div.stButton > button {{
    width:100% !important; height:65px !important; border-radius:50px !important;
    background: linear-gradient(90deg, #6b3a00, #d4af37) !important;
    color:white !important; font-size:26px !important; font-weight:900 !important; letter-spacing:4px !important;
    border:1px solid #ffe27a !important;
}}
</style>
""", unsafe_allow_html=True)

st.text_input("USERNAME", placeholder="Enter your username")
st.text_input("PASSWORD", type="password", placeholder="Enter your password")
if st.button("LOGIN"):
    st.success("Welcome - UQABOOT me Khush Amdeed 🦅")
