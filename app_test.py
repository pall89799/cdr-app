import streamlit as st

st.set_page_config(page_title="UQABOOT - Punjab Police", page_icon="🦅", layout="wide")

# --- UQABOOT DESIGN ---
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #0a0f1e, #000000); color: white; }
h1 { color: #FFD700 !important; text-align: center; font-size: 50px !important; }
.stButton > button {
    width: 100%; height: 65px; font-size: 20px !important; font-weight: bold !important;
    border-radius: 15px !important; color: white !important;
    background: linear-gradient(90deg, #0040FF, #00A2FF) !important;
    border: 2px solid #FFD700 !important;
}
.login-box { background: #1a1a1a; padding: 25px; border-radius: 15px; border: 2px solid #FFD700; max-width: 500px; margin: auto; }
.admin-box { background: #1a1a1a; padding: 15px; border-radius: 12px; border: 1px solid #FFD700; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🦅 UQABOOT 🦅</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM<br>Rawalpindi Region • Criminal Tracking</p>", unsafe_allow_html=True)

# --- LOGIN ---
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    mobile = st.text_input("Mobile Number")
    password = st.text_input("Password", type="password")
    if st.button("🔐 LOGIN"):
        if not mobile or not password:
            st.warning("Mobile aur Password likho jan!")
        else:
            st.session_state.login = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- ADMIN PANEL ---
    st.markdown("""
    <div class='admin-box'>
    <h3>👑 ADMIN PANEL</h3>
    <b>Admin:</b> Muhammad Saleem Qureshi<br>
    <b>Pending Requests:</b> Koi pending nahi hai ✅
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    # --- MAIN BUTTONS ---
    st.markdown("<h2 style='text-align:center; color:#FFD700;'>🔍 Select Analysis</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📡 BTS ANALYSER"):
            st.session_state.page = "bts"
    with c2:
        if st.button("📞 CDR ANALYSER"):
            st.session_state.page = "cdr"

    st.write("---")
    if st.session_state.get("page") == "bts":
        st.markdown("### 📡 BTS ANALYSER")
        st.file_uploader("BTS File Upload Karo", type=["csv","xlsx"])
        st.text_input("Number Likho - BTS")
        if st.button("🔍 BTS Check Karo"):
            st.success("BTS Test Chal Raha Hai Jan!")
    elif st.session_state.get("page") == "cdr":
        st.markdown("### 📞 CDR ANALYSER")
        st.file_uploader("CDR File Upload Karo", type=["csv","xlsx"])
        st.text_input("Number Likho - CDR")
        if st.button("🔍 CDR Check Karo"):
            st.success("CDR Test Chal Raha Hai Jan!")

    if st.button("🚪 LOGOUT"):
        st.session_state.login = False
        st.rerun()

# --- FOOTER ---
st.markdown("""
<div style='text-align:center; background:#8B0000; padding:12px; border-radius:10px; margin-top:30px;'>
<b>⚠️ UQABOOT - FOR OFFICIAL POLICE USE ONLY ⚠️</b>
</div>
""", unsafe_allow_html=True)
