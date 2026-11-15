import streamlit as st
st.set_page_config(page_title="UQABOOT", page_icon="🦅", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #0B0B0B 0%, #2B1A0E 50%, #1A1A1A 100%); }
h1 { color: #D4AF37 !important; text-align: center; font-size: 65px !important; }
.stButton > button { background: linear-gradient(90deg, #8B5A2B, #D4AF37) !important; color: black !important; font-weight: bold; font-size: 20px; height: 55px; }
</style>
""", unsafe_allow_html=True)
st.markdown("<h1>🦅 UQABOOT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#C0A062; font-size:22px;'>Secure CDR Analysis Platform</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#A9A9A9;'>It's Paid Version</p>", unsafe_allow_html=True)
mobile = st.text_input("Mobile Number", placeholder="Enter mobile number")
password = st.text_input("Password", type="password", placeholder="Enter password")
if st.button("LOGIN"):
    if not mobile or not password:
        st.warning("Mobile aur Password likho jaan!")
    else:
        st.success("Login Check ho raha hai...")
st.markdown("<p style='text-align:center; color:#8B5A2B;'>© 2026 UQABOOT CDR Analysis System</p>", unsafe_allow_html=True)
