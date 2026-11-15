import streamlit as st

st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #2b1a0e 0%, #1a1210 40%, #3a3a3a 75%, #0d0d0d 100%);
}
[data-testid="stHeader"], [data-testid="stToolbar"], footer {display:none !important;}
.block-container {max-width: 520px !important; padding-top: 10px !important; text-align:center;}

.eagle {font-size: 110px; line-height: 1; filter: drop-shadow(0 0 20px #d4af37); margin-bottom: -10px;}
.title {
    font-size: 58px !important; font-weight: 900 !important;
    color: #e8b923 !important; letter-spacing: 2px;
    text-shadow: 0 0 25px #ffcc00, 0 3px 0 #7a5a00;
    margin: 0px !important; line-height: 1.1;
}
.subtitle {color: white !important; font-size: 15px !important; font-weight: 600 !important; letter-spacing: 1px; margin-top: 8px;}
.subtitle2 {color: #f0e6d2 !important; font-size: 15px !important; margin-bottom: 25px;}

div[data-testid="stTextInput"] > div {background: white !important; border-radius: 10px !important; border: 2px solid #d4af37 !important;}
div[data-testid="stTextInput"] input {color: black !important; font-size: 17px !important; text-align: center;}
div[data-testid="stTextInput"] label {color: white !important; font-weight: 700 !important; font-size: 15px !important;}

div.stButton > button {
    width: 100% !important; height: 55px !important;
    background: linear-gradient(90deg, #8b5a00, #d4af37, #8b5a00) !important;
    color: white !important; font-size: 22px !important; font-weight: 900 !important;
    letter-spacing: 3px; border: 2px solid #ffe27a !important; border-radius: 12px !important;
    box-shadow: 0 5px 20px rgba(212,175,55,0.5);
}
div.stButton > button:hover {transform: scale(1.02);}
.footer {color: #d4af37; font-size: 13px; margin-top: 20px; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="eagle">🦅</div>', unsafe_allow_html=True)
st.markdown('<p class="title">UQABOOT</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle2">Rawalpindi Region • Criminal Tracking</p>', unsafe_allow_html=True)

user = st.text_input("USERNAME", placeholder="Username likhein")
pwd = st.text_input("PASSWORD", type="password", placeholder="Password likhein")

if st.button("LOGIN"):
    if user and pwd:
        st.success(f"Welcome {user} - UQABOOT me Khush Amdeed 🦅")
        st.balloons()
    else:
        st.warning("Pehle Username or Password likhein jaan!")

st.markdown('<p class="footer">🦅 UQABOOT - Punjab Police • Secure System 🦅</p>', unsafe_allow_html=True)
