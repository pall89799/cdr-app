import streamlit as st
st.set_page_config(page_title="BTS Analyser", layout="wide")

# --- CDR = NEELA FIX, BTS = ORANGE FIX ---
if "mode" not in st.session_state:
    st.session_state.mode = "CDR"

active_color = "#1E6BFF" if st.session_state.mode == "CDR" else "#FF7A00"

st.markdown(f"""
<style>
/* Pehla button (CDR) hamesha NEELA */
div[data-testid="stVerticalBlock"] > div:nth-child(2) div[data-testid="stHorizontalBlock"] > div:nth-child(1) div[data-testid="stButton"] > button {{
    background: linear-gradient(90deg, #1E6BFF, #00C6FF) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    border: none !important;
    padding: 12px 20px !important;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.20) !important;
}}
/* Dusra button (BTS) hamesha ORANGE */
div[data-testid="stVerticalBlock"] > div:nth-child(2) div[data-testid="stHorizontalBlock"] > div:nth-child(2) div[data-testid="stButton"] > button {{
    background: linear-gradient(90deg, #FF7A00, #FFB800) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    border: none !important;
    padding: 12px 20px !important;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.20) !important;
}}
/* Login / Signup Button - Final */
div[data-testid="stTabs"] button[role="tab"] {{
    background-color: white !important;
    color: #1A2B4A !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    padding: 10px 22px !important;
    border-radius: 12px !important;
    border: 2px solid #D6E4FF !important;
    margin-right: 8px !important;
}}
div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {{
    background: linear-gradient(90deg, #1E6BFF, #FF7A00) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 5px 15px rgba(255,122,0,0.35) !important;
}}/* Jo Tab SELECT ho */
div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {{
    background-color: {active_color} !important;
    color: white !important;
    border: 1px solid {active_color} !important;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25) !important;
    transform: scale(1.05) !important;
}}
div[data-testid="stDateInput"] input,
div[data-testid="stTimeInput"] input {{
    background: linear-gradient(135deg, #e0f2fe, #ffffff) !important;
    border: 2px solid #38bdf8 !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 10px rgba(56,189,248,0.25) !important;
}}

div[data-testid="stCheckbox"] label {{
    background: linear-gradient(135deg, #f59e0b, #ef4444) !important;
    color: white !important;
    padding: 10px 16px !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 0 #991b1b, 0 8px 15px rgba(0,0,0,0.25) !important;
}}

div[data-testid="stFileUploader"] section {{
    background: linear-gradient(135deg, #fff7ed, #fef3c7) !important;
    border: 3px dashed #f97316 !important;
    border-radius: 16px !important;
    box-shadow: 0 6px 15px rgba(249,115,22,0.20) !important;
}}

div[data-testid="stFileUploader"] button {{
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    box-shadow: 0 5px 0 #14532d, 0 8px 15px rgba(0,0,0,0.25) !important;
}}
div[data-testid="stFileUploader"] button:hover {{
    transform: translateY(-2px) !important;
}}
/* --- Date / Start / End ke LABEL - rangin --- */
div[data-testid="stDateInput"] label p,
div[data-testid="stTimeInput"] label p {{
    color: #1d4ed8 !important;
    font-weight: 900 !important;
    font-size: 16px !important;
}}

/* --- Date / Start / End ke DABAY - zyada rangin --- */
div[data-testid="stDateInput"] div[data-baseweb="input"],
div[data-testid="stTimeInput"] div[data-baseweb="input"] {{
    background: linear-gradient(135deg, #dbeafe, #c4b5fd) !important;
    border: 2.5px solid #7c3aed !important;
    border-radius: 14px !important;
    box-shadow: 0 5px 0 #4c1d95, 0 8px 15px rgba(124,58,237,0.30) !important;
}}
div[data-testid="stDateInput"] input,
div[data-testid="stTimeInput"] input {{
    background: transparent !important;
    color: #1e1b4b !important;
    font-weight: 800 !important;
    font-size: 16px !important;
}}

/* --- Upload wala bara DABA - ab Purple / Pink --- */
div[data-testid="stFileUploader"] section {{
    background: linear-gradient(135deg, #fdf4ff, #fce7f3, #e0e7ff) !important;
    border: 3px solid #d946ef !important;
    border-radius: 18px !important;
    box-shadow: 0 6px 0 #a21caf, 0 10px 20px rgba(217,70,239,0.35) !important;
}}
div[data-testid="stFileUploader"] label p {{
    color: #a21caf !important;
    font-weight: 900 !important;
    font-size: 16px !important;
}}
/* --- LOGIN + SIGNUP FULL BEAUTIFUL --- */
.stApp {{
    background: linear-gradient(135deg, #E8F0FF 0%, #FFF2E6 100%) !important;
}}
.stTextInput input {{
    background-color: white !important;
    border-radius: 12px !important;
    border: 2px solid #D6E4FF !important;
    padding: 12px 15px !important;
    font-size: 16px !important;
}}
.stButton > button {{
    background: linear-gradient(90deg, #1E6BFF, #FF7A00) !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 12px 40px !important;
    border-radius: 12px !important;
    border: none !important;
    box-shadow: 0 5px 15px rgba(30,107,255,0.35) !important;
    width: 100% !important;
}}
/* Login / Signup Button - Final */
div[data-testid="stTabs"] button[role="tab"] {{
    background-color: white !important;
    color: #1A2B4A !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    padding: 10px 22px !important;
    border-radius: 12px !important;
    border: 2px solid #D6E4FF !important;
    margin-right: 8px !important;
}}
div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {{
    background: linear-gradient(90deg, #1E6BFF, #FF7A00) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 5px 15px rgba(255,122,0,0.35) !important;
}}
/* --- Oopar-Neeche Slide Bar --- */
::-webkit-scrollbar {{
    width: 14px !important;
    height: 14px !important;
}}
::-webkit-scrollbar-track {{
    background: #E8F0FF !important;
    border-radius: 10px !important;
}}
::-webkit-scrollbar-thumb {{
    background: linear-gradient(180deg, #1E6BFF, #FF7A00) !important;
    border-radius: 10px !important;
    border: 2px solid #E8F0FF !important;
}}
</style>
""", unsafe_allow_html=True)

from supabase import create_client
import random
import hashlib
from openpyxl.styles import PatternFill, Font, Alignment

SUPABASE_URL = "https://qctbnewntgzeagfdafgx.supabase.co"
SUPABASE_KEY = "sb_publishable_JvfMI_5erJ88oNY8Lvi1cw_30WNW4xx"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

ADMIN_MOBILE = "03000508387"

def hash_pass(p):
    return hashlib.sha256(p.encode()).hexdigest()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# ===== SIRF LOGIN + SIGNUP + APPROVAL, BAS =====
if not st.session_state.logged_in:
    st.title("🔐 CDR-BTS Login")
    tab1, tab2 = st.tabs(["Signup", "Login"])
    with tab1:
        name = st.text_input("Full Naam", key="s_name")
        mobile = st.text_input("Mobile Number", key="s_mobile")
        cnic = st.text_input("CNIC Number", key="s_cnic")
        password = st.text_input("Password", type="password", key="s_pass")
        if st.button("Create Account"):
            if not name or not mobile or not cnic or not password:
                st.error("Fill all Fileds")
            else:
                old = supabase.table("users").select("*").eq("mobile", mobile).execute()
                if old.data:
                    st.error("Is mobile se pehle se account bana hua hai")
                else:
                    device_code = f"D-{random.randint(100000,999999)}"
                    supabase.table("users").insert({
                        "name": name, "mobile": mobile, "cnic": cnic,
                        "password": hash_pass(password),
                        "device_code": device_code, "status": "pending"
                    }).execute()
                    st.success("Account ban gaya! Code Admin ko bhejo")
                    st.code(device_code)
    with tab2:
        l_mobile = st.text_input("Mobile Number", key="l_mobile")
        l_pass = st.text_input("Password", type="password", key="l_pass")
        if st.button("Login"):
            res = supabase.table("users").select("*").eq("mobile", l_mobile).execute()
            if not res.data:
                st.error("Account not found - Signup first")
            else:
                u = res.data[0]
                if u["password"] != hash_pass(l_pass):
                    st.error("Wrong Password")
                elif u["status"] != "approved":
                    st.error(f"Pending. Code {u['device_code']} Send to admin")
                else:
                    st.session_state.logged_in = True
                    st.session_state.user = u
                    st.rerun()
    st.stop()
# ===== ADMIN PANEL + PENDING EK LINE ME =====
user = st.session_state.user
if user["mobile"] == ADMIN_MOBILE:
    admin_left, pending_right = st.columns([1, 1.8])

    with admin_left:
        st.markdown("### 👑 ADMIN PANEL")
        st.write(f"Admin: {user['name']}")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

    with pending_right:
        pending = supabase.table("users").select("*").eq("status", "pending").execute()
        st.markdown("<h2 style='font-size:32px; color:#0B3D91; font-weight:bold;'>Pending Requests</h2>", unsafe_allow_html=True)
        if not pending.data:
            st.success("No pending")
        for p in pending.data:
            st.markdown(f"<p style='font-size:16px; font-weight:bold; margin-bottom:2px;'>{p['name']} | {p['mobile']}</p>", unsafe_allow_html=True)
            st.code(p['device_code'])
            c1, c2 = st.columns(2)
            with c1:
                if st.button(f"Approve {p['name']}", key=f"ap_{p['id']}"):
                    supabase.table("users").update({"status": "approved"}).eq("id", p['id']).execute()
                    st.rerun()
            with c2:
                if st.button(f"Reject {p['name']}", key=f"rj_{p['id']}", type="primary"):
                    supabase.table("users").delete().eq("id", p['id']).execute()
                    st.rerun()
else:
    st.write(f"User: {user['name']} | {user['mobile']}")

#if st.button("Logout"):
#   st.session_state.logged_in = False
#   st.session_state.user = None
#   st.rerun()

# ===== IS LINE KE NEECHE TUMHARA WOHI PURANA DASHBOARD HAI, 10 BUTTON WALA, USKO MAT CHERNA =====

# --- YAHAN SE TUMHARA PURANA CODE SHURU ---
import pandas as pd
import io
import base64
from datetime import date as dt_date

st.markdown("""
<style>
h1 a, h2 a, h3 a { display:none !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .stApp { background-color: #F2F4F7; }
    header { visibility: hidden; }
    .police-header {
        background: linear-gradient(90deg, #0B2C4A 0%, #123F66 70%, #0B2C4A 100%);
        padding: 16px 24px;
        border-radius: 0px 0px 12px 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 4px solid #C5A880;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .police-header h1 { color: white !important; font-size: 36px !important; margin: 0 !important; font-weight: 700; }
    .police-header p { color: #C5A880 !important; font-size: 13px !important; margin: 2px 0 0 0 !important; font-weight: 600; letter-spacing: 1px; }
    .header-right { text-align: right; color: white; font-size: 13px; }
    .header-badge { background: #C5A880; color: #0B2C4A; padding: 4px 12px; border-radius: 20px; font-weight: 700; font-size: 12px; }
    .stTabs [data-baseweb="tab-list"] { gap: 4px; background: white; padding: 8px; border-radius: 10px; }
    .stTabs [data-baseweb="tab"] { background: #EAF0F6; border-radius: 8px; padding: 8px 14px; font-weight: 600; color: #0B2C4A; font-size: 13px; }
    .stTabs [aria-selected="true"] { background: #0B2C4A !important; color: white !important; }
    .stDownloadButton button { background: #1A7F4B !important; color: white !important; border: none !important; border-radius: 8px !important; padding: 12px 24px !important; font-weight: 700 !important; font-size: 15px !important; width: 100%; }
    .stDownloadButton button:hover { background: #146638 !important; }
    [data-testid="stFileUploader"] { background: white; border: 2px dashed #0B2C4A; border-radius: 12px; padding: 12px; }
</style>
<div class="police-header">
    <div>
        <h1>🛡️ PUNJAB POLICE - CDR / BTS ANALYSIS SYSTEM</h1>
        <p>CRIMINAL TRACKING • CALL DETAIL RECORD • TOWER LOCATION</p>
    </div>
    <div class="header-right">
        <span class="header-badge">OFFICIAL USE ONLY</span><br><br>
        <span>Rawalpindi Region</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== 1. SAB SE OPER - URDU WALI PATTI =====
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu&display=swap" rel="stylesheet">
<div dir="rtl" lang="ur" style="background:#4a0000; color:white; padding:18px 10px 22px 10px; border-bottom:4px solid #FFC107; overflow:hidden; text-align:center;">
<marquee direction="right" scrollamount="5" style="font-family:'Noto Nastaliq Urdu', serif; font-size:22px; line-height:2.2;">
یہ سافٹ ویئر صرف قانون نافذ کرنے والے اداروں کے افسران کے لیےبنایاگیا ہے۔یہ کسی پرائیویٹ شخص کو فراہم نہیں کیا جاتا ۔رابطہ برائے ایڈمن &nbsp; • &nbsp; <span dir="ltr" style="font-family:Arial; font-size:20px;">03000508387ایم ایس قریشی</span>
</marquee>
</div>
""", unsafe_allow_html=True)


st.write("---")
st.write("Ufone / Jazz / Telenor / Zong - select Tab, select file, download")

if "mode" not in st.session_state:
    st.session_state.mode = "CDR"
c1, c2 = st.columns(2)
with c1:
    if st.button("📞 CDR ANALYSER", use_container_width=True, type="primary"):
        st.session_state.mode = "CDR"
        st.rerun()
with c2:
    if st.button("📡 BTS ANALYSER", use_container_width=True):
        st.session_state.mode = "BTS"
        st.rerun()
class _HideTab:
    def __init__(self, real, show):
        self.real = real
        self.show = show
        self.ph = None
    def __enter__(self):
        if self.show:
            return self.real.__enter__()
        else:
            self.ph = st.empty()
            return self.ph.__enter__()
    def __exit__(self, *a):
        if self.show:
            return self.real.__exit__(*a)
        else:
            self.ph.__exit__(*a)
            self.ph.empty()
            return False

if st.session_state.mode == "BTS":
    _names = ["📱 UFONE", "📱 JAZZ", "📱 TELENOR", "📱 ZONG", "📱 ALL BTS"]
else:
    _names = ["📞 CDR UFONE", "📞 CDR JAZZ", "📞 CDR TELENOR", "📞 CDR ZONG", "📞 ALL CDR"]

if "sub_idx" not in st.session_state:
    st.session_state.sub_idx = 0

btn_bg = "#1E6BFF" if st.session_state.mode == "CDR" else "#FF7A00"

cols = st.columns(5)
for i, name in enumerate(_names):
    with cols[i]:
        if st.button(name, key=f"sub_{st.session_state.mode}_{i}", use_container_width=True):
            st.session_state.sub_idx = i
            st.rerun()

st.markdown(f"""
<style>
div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button {{
    background: {btn_bg} !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    border: none !important;
    padding: 10px 5px !important;
}}
</style>
""", unsafe_allow_html=True)

selected_tab = st.session_state.sub_idx
def clean_call_type(v):
    s = str(v).strip().upper()
    if "SMS" in s:
        if "OUT" in s:
            return "Out SMS"
        if "IN" in s:
            return "In SMS"
        return "SMS"
    if "GPRS" in s or "DATA" in s or "INTERNET" in s:
        return "GPRS"
    if "OUT" in s:
        return "Out Call"
    if "IN" in s:
        return "In Call"
    return str(v).strip()
def clean_number(num):
    s = str(num).strip()
    if s == "" or s.lower() == "nan":
        return ""
    # Jazz SMS wala B Party: 64030611391767 -> 3061139176
    if s.startswith("640") and len(s) == 14 and s[3] == "3" and s.endswith("7"):
        s = s[3:-1]
    # Jazz B Party: 3150414953414 -> 3150414953 (aakhir wale 3 extra kaat do)
    if len(s) == 13 and s.isdigit() and s.startswith("3") and s[:2] in ("30", "31", "32", "33", "34", "35"):
        s = s[:10]    
        
    # HEX: 4A415A5A203547 -> JAZZ 5G
    if any(c in "ABCDEFabcdef" for c in s) and len(s) % 2 == 0:
        try:
            decoded = bytes.fromhex(s).decode('ascii')
            if all(32 <= ord(c) <= 126 for c in decoded):
                return decoded.strip()
        except:
            pass
        return s

    if any(c.isalpha() for c in s):
        return s

    is_pak = s.startswith("+92") or s.startswith("92") or s.startswith("0") or s.startswith("092")

    # Telenor wala special case
    if s.startswith("0092"):
        s = s[4:]
    elif s.startswith("092"):
        if len(s) > 3 and s[3] == "3":
            # 0923... = Mobile, 092 kaato
            s = s[3:]
        else:
            # 0924... = Landline, sirf 0 kaato, 92 rehne do
            s = s[1:]
    elif s.startswith("+92"):
        s = s[3:]
    elif s.startswith("92") and len(s) > 10:
        s = s[2:]
    elif s.startswith("0"):
        s = s[1:]

    # Sirf Pakistani Mobile ko 10 digit par kaato
    if is_pak and len(s) > 10 and s.isdigit() and s.startswith("3"):
        s = s[:10]
    return s

def add_extra_columns(final, df_dt):
    final["_full_dt"] = df_dt
    grp = final.groupby("A Party")["_full_dt"]
    first_seen = grp.min()
    last_seen = grp.max()
    total_activity = grp.size()
    total_duration = final.groupby("A Party")["Duration"].sum()
    b_set = set(final["B Party"].astype(str).unique())
    final["First Seen"] = final["A Party"].map(first_seen).dt.strftime("%d-%m-%y %H:%M:%S")
    final["Last Seen"] = final["A Party"].map(last_seen).dt.strftime("%d-%m-%y %H:%M:%S")
    final["Total Activity"] = final["A Party"].map(total_activity)
    final["Total Duration"] = final["A Party"].map(total_duration)
    final["A Party in B Party"] = final["A Party"].apply(lambda x: "YES" if str(x) in b_set else "NO")
    final = final.drop(columns=["_full_dt"])
    return final[["Call Type","A Party","B Party","Date","Time","Duration","IMEI","LAC","Cell ID","First Seen","Last Seen","Total Activity","Total Duration","A Party in B Party","Network"]]

def download_section(final, filename):
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from openpyxl.utils import get_column_letter
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        final.to_excel(writer, index=False, sheet_name="Cleaned")
        ws = writer.sheets["Cleaned"]
        if len(final) > 0 and len(final.columns) > 0:
            last_col = get_column_letter(len(final.columns))
            last_row = len(final) + 1
            tab = Table(displayName="CleanedTable", ref=f"A1:{last_col}{last_row}")
            tab.tableStyleInfo = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
            ws.add_table(tab)
        ws.freeze_panes = "A2"
        ws.sheet_properties.pageSetUpPr.fitToPage = True
    st.download_button(label="📥 Cleaned Excel (XLSX) Download Karo", data=output.getvalue(), file_name=filename, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    st.dataframe(final)

def parse_telenor_date(x):
    s = str(x).strip()
    for fmt in ("%d-%m-%y %H:%M:%S", "%d-%m-%y %H:%M", "%d-%m-%Y %H:%M:%S", "%d-%m-%Y %H:%M", "%y-%m-%d %H:%M", "%d/%m/%Y %H:%M", "%d/%m/%y %H:%M"):
        try: return pd.to_datetime(s, format=fmt)
        except: continue
    return pd.to_datetime(s, errors="coerce", dayfirst=True)

def parse_ufone_df(df):
    df.columns = [c.strip() for c in df.columns]
    dt = pd.to_datetime(df["CALL_START_TIME"], errors="coerce")
    final = pd.DataFrame()
    # Ufone file UTF-16 hoti hai, isliye naam se column pakro
    typ = df["CALL_TYPE_NAME"].astype(str).str.strip().str.lower() if "CALL_TYPE_NAME" in df.columns else df.iloc[:, 3].astype(str).str.strip().str.lower()
    direc = df["CALL_INBOUND_OUTBOUND_DESC"].astype(str).str.strip().str.lower() if "CALL_INBOUND_OUTBOUND_DESC" in df.columns else df.iloc[:, 12].astype(str).str.strip().str.lower()
    _ct = []
    for _t, _d in zip(typ.tolist(), direc.tolist()):
        if "sms" in _t:
            _ct.append("In SMS" if ("incoming" in _d or "inbound" in _d) else "Out SMS")
        elif "voice" in _t or "call" in _t:
            _ct.append("In Call" if ("incoming" in _d or "inbound" in _d) else "Out Call")
        elif "data" in _t or "internet" in _t or "gprs" in _t:
            _ct.append("Data In" if ("incoming" in _d or "inbound" in _d) else "Data Out")
        else:
            _ct.append("Out Call")
    final["Call Type"] = _ct        
    final["A Party"] = df["A_NUMBER"].apply(clean_number)
    final["B Party"] = df["B_NUMBER"].apply(clean_number)
    final["Date"] = dt.dt.strftime("%d-%m-%y")
    final["Time"] = dt.dt.strftime("%H:%M:%S")
    final["Duration"] = pd.to_numeric(df["CALL_DURATION"], errors="coerce").fillna(0).astype(int)
    final["IMEI"] = df["IMEI"]
    cell = df["CELL_ID"].astype(str).str.strip()
    final["LAC"] = cell.str[:5]
    final["Cell ID"] = cell.str[5:]
    final["Network"] = "UFONE"
    final["_dt"] = dt
    return final

def parse_jazz_df(df):
    df.columns = [c.strip() for c in df.columns]
    raw = pd.to_numeric(df["Date And Time"], errors="coerce")
    dt_text = pd.to_datetime(df["Date And Time"], errors="coerce")
    dt_num = pd.to_datetime(raw, origin="1899-12-30", unit="D", errors="coerce")
    is_num = raw.notna()
    dt = dt_num.where(is_num, dt_text)
    def jazz_lac_cell(cell_val):
        s = str(cell_val).strip()
        lac_hex = s[:4][::-1]; cell_hex = s[4:8][::-1]
        try: lac = int(lac_hex, 16)
        except: lac = ""
        try: cellid = int(cell_hex, 16)
        except: cellid = ""
        return lac, cellid
    lac_list=[]; cell_list=[]
    for v in df["Cell ID"]:
        l,c = jazz_lac_cell(v); lac_list.append(l); cell_list.append(c)
    final = pd.DataFrame()
    final["Call Type"] = df["Call Type"].apply(clean_call_type)
    final["A Party"] = df["A-Party"].apply(clean_number)
    final["B Party"] = df["B-Party"].apply(clean_number)
    final["Date"] = dt.dt.strftime("%d-%m-%y")
    final["Time"] = dt.dt.strftime("%H:%M:%S")
    final["Duration"] = pd.to_numeric(df["Duration"], errors="coerce").fillna(0).astype(int)
    final["IMEI"] = df["IMEI"]; final["LAC"] = lac_list; final["Cell ID"] = cell_list; final["Network"] = "JAZZ"; final["_dt"] = dt
    return final

def parse_telenor_df(df):
    df.columns = [c.strip() for c in df.columns]
    df = df.dropna(subset=["MSISDN"]); df = df[df["MSISDN"].astype(str).str.strip() != ""]
    dt = df["CALL_START_DT_TM"].apply(parse_telenor_date)
    tmp = pd.DataFrame()
    ind = df["INBOUND_OUTBOUND_IND"].astype(str).str.strip()
    direction = ind.map({"0": "INTERNET", "1": "OUTGOING", "2": "INCOMING"}).fillna(ind)
    real_type = df["CALL_TYPE"].astype(str).str.strip().str.upper() if "CALL_TYPE" in df.columns else pd.Series(["CALL"]*len(df))
    merged=[]
    for d,t in zip(direction, real_type):
        if t=="GPRS" or d=="INTERNET": merged.append("GPRS")
        elif d=="INCOMING" and t=="CALL": merged.append("In Call")
        elif d=="OUTGOING" and t=="CALL": merged.append("Out Call")
        elif d=="INCOMING" and t=="SMS": merged.append("In SMS")
        elif d=="OUTGOING" and t=="SMS": merged.append("Out SMS")
        elif d=="INCOMING": merged.append("In Call")
        elif d=="OUTGOING": merged.append("Out Call")
        else: merged.append("Out Call")
    tmp["Call Type"]=merged; tmp["A Party"]=df["MSISDN"].apply(clean_number)
    tmp["B Party"]=df["CALL_DIALED_NUM"].apply(clean_number) if "CALL_DIALED_NUM" in df.columns else df["CALL_ORIG_NUM"].apply(clean_number)
    tmp["Date"]=dt.dt.strftime("%d-%m-%y"); tmp["Time"]=dt.dt.strftime("%H:%M:%S")
    tmp["Duration"]=pd.to_numeric(df["Call_Network_Volume"], errors="coerce").fillna(0).astype(int)
    tmp["IMEI"]=df["IMEI"]; tmp["LAC"]=df["Lac_Id"]; tmp["Cell ID"]=df["Site_Id"]; tmp["Network"]="TELENOR"; tmp["_dt"]=dt
    return tmp

def parse_zong_df(df):
    df.columns = [c.strip() for c in df.columns]
    dt = pd.to_datetime(df["STRT_TM"], errors="coerce")
    final = pd.DataFrame()
    dir_col = df["DIR_FLG"].astype(str).str.strip().str.lower()
    final["Call Type"] = dir_col.map({"incomming":"In Call","incoming":"In Call","outgoing":"Out Call","outcomming":"Out Call"}).fillna("Out Call")
    final["A Party"]=df["DLG_NO"].apply(clean_number); final["B Party"]=df["DLD_NO"].apply(clean_number)
    final["Date"]=dt.dt.strftime("%d-%m-%y"); final["Time"]=dt.dt.strftime("%H:%M:%S")
    _cols = {str(c).strip().upper(): str(c).strip() for c in df.columns}
    _min_col = None; _sec_col = None
    for k,v in _cols.items():
        if "MIN" in k and "MINUTE" in k:
            _min_col = v
        if k == "SEC" or "SECOND" in k:
            _sec_col = v
    if _min_col is not None and _sec_col is not None:
        _m = pd.to_numeric(df[_min_col], errors="coerce").fillna(0)
        _s = pd.to_numeric(df[_sec_col], errors="coerce").fillna(0)
        final["Duration"] = (_m*60 + _s).astype(int)
    else:
        final["Duration"]=pd.to_numeric(df["DRTN"], errors="coerce").fillna(0).astype(int)
    imei_1 = df["CLD_IMIE"].astype(str).str.strip() if "CLD_IMIE" in df.columns else ""
    imei_2 = df["CLG_IMEI"].astype(str).str.strip() if "CLG_IMEI" in df.columns else ""
    merged_imei=[]
    for a,b in zip(imei_1, imei_2):
        if str(a).strip() != "" and str(a).lower() != "nan": merged_imei.append(str(a).strip())
        elif str(b).strip() != "" and str(b).lower() != "nan": merged_imei.append(str(b).strip())
        else: merged_imei.append("")
    final["IMEI"]=merged_imei; final["LAC"]=df["LAC_ID"]; final["Cell ID"]=df["CELL_ID"]; final["Network"]="ZONG"; final["_dt"]=dt
    return final

def detect_network(df, filename=""):
    cols=[str(c).strip().upper() for c in df.columns]
    if "CALL_START_TIME" in cols and "A_NUMBER" in cols: return "UFONE"
    if "DATE AND TIME" in cols and "A-PARTY" in cols: return "JAZZ"
    if "CALL_START_DT_TM" in cols and "MSISDN" in cols: return "TELENOR"
    if "STRT_TM" in cols and "DLG_NO" in cols: return "ZONG"
    lname=filename.lower()
    if "ufone" in lname: return "UFONE"
    if "jazz" in lname or "mobilink" in lname: return "JAZZ"
    if "telenor" in lname: return "TELENOR"
    if "zong" in lname: return "ZONG"
    return "UNKNOWN"

# ===== CDR UFONE - CELL ID HALF-HALF - LAC + CID - LOCK - NA CHHERNA =====
def split_cell_id_half(v):
    s = str(v).strip()
    if s == "" or s.lower() == "nan" or s == "0":
        return "", ""
    if s.endswith(".0"):
        s = s[:-2]
    s = "".join([c for c in s if c.isdigit()])
    if len(s) < 2:
        return "", s
    h = len(s) // 2
    return s[:h], s[h:]

def read_cdr_ufone_file(f):
    lname = f.name.lower()
    f.seek(0)
    if lname.endswith(".csv"):
        try:
            return pd.read_csv(f, dtype=str, encoding="utf-8")
        except:
            f.seek(0)
            return pd.read_csv(f, dtype=str, encoding="latin1")
    elif lname.endswith(".xlsx") or lname.endswith(".xls"):
        xls = pd.ExcelFile(f)
        for sh in xls.sheet_names:
            try:
                tmp = pd.read_excel(f, sheet_name=sh, dtype=str, nrows=2)
                cols = [str(c).strip().upper() for c in tmp.columns]
                if "A NUMBER" in cols or "A" in cols:
                    return pd.read_excel(f, sheet_name=sh, dtype=str)
            except:
                continue
        return pd.read_excel(f, sheet_name=0, dtype=str)
    return None

def build_cdr_ufone_output(raw_df):
    raw = raw_df.copy()
    raw.columns = [str(c).strip() for c in raw.columns]
    cmap = {str(c).strip().upper(): str(c).strip() for c in raw.columns}
    def col(*names):
        for n in names:
            if n.upper() in cmap:
                return cmap[n.upper()]
        return None
    cIMEI = col("IMEI"); cA = col("A Number","A"); cB = col("B Number","B")
    cSTART = col("Start Time"); cTYPE = col("Type"); cDIR = col("Direction"); cLOC = col("Location","LOC")
    cCELL = col("Cell Id","Cell ID","CID")
    cLAT = col("Latitude","LAT"); cLNG = col("Longitude","LNG"); cDUR = col("Duration","DUR")
    df = pd.DataFrame()
    df["A Party"] = raw[cA].apply(clean_number) if cA else ""
    df["B Party"] = raw[cB].apply(clean_number) if cB else ""
    _type = raw[cTYPE].astype(str).str.strip().str.upper() if cTYPE else pd.Series([""]*len(raw))
    _dir = raw[cDIR].astype(str).str.strip().str.upper() if cDIR else pd.Series([""]*len(raw))
    calltypes = []
    for t, d in zip(_type, _dir):
        if t == "VOICE" and d == "INCOMING":
            calltypes.append("IC")
        elif t == "VOICE" and d == "OUTGOING":
            calltypes.append("OG")
        elif t == "SMS" and d == "INCOMING":
            calltypes.append("ISMS")
        elif t == "SMS" and d == "OUTGOING":
            calltypes.append("OSMS")
        elif t == "DATA":
            calltypes.append("DATA")
        else:
            calltypes.append(t)
    df["Call Type"] = calltypes
    _dt = pd.to_datetime(raw[cSTART], errors="coerce") if cSTART else pd.Series([pd.NaT]*len(raw))
    df["Date"] = _dt.dt.strftime("%Y-%m-%d")
    df["Time"] = _dt.dt.strftime("%H:%M:%S")
    df["Duration"] = pd.to_numeric(raw[cDUR], errors="coerce").fillna(0).astype(int) if cDUR else 0
    lac_list = []; cid_list = []
    if cCELL:
        for v in raw[cCELL]:
            l, c = split_cell_id_half(v)
            lac_list.append(l); cid_list.append(c)
    else:
        lac_list = [""]*len(raw); cid_list = [""]*len(raw)
    df["LAC"] = lac_list
    df["CID"] = cid_list
    df["IMEI"] = raw[cIMEI].astype(str).str.strip() if cIMEI else ""
    df["Location"] = raw[cLOC].astype(str).str.strip() if cLOC else ""
    df["LAT"] = raw[cLAT].astype(str).str.strip() if cLAT else ""
    df["LNG"] = raw[cLNG].astype(str).str.strip() if cLNG else ""
    df["_dt"] = _dt
    df["_dur_min"] = df["Duration"] / 60.0
    cdr_data = df[["Call Type","A Party","B Party","Date","Time","Duration","IMEI","LAC","CID","Location","LAT","LNG"]].copy()
    summ_base = df[df["Call Type"] != "DATA"].copy()
    summ_rows = []
    for (a,b), g in summ_base.groupby(["A Party","B Party"]):
        summ_rows.append({
            "A": a, "B": b,
            "IC": int((g["Call Type"]=="IC").sum()),
            "ISMS": int((g["Call Type"]=="ISMS").sum()),
            "OG": int((g["Call Type"]=="OG").sum()),
            "OSMS": int((g["Call Type"]=="OSMS").sum()),
            "Total": len(g),
            "IC (Seconds)": int(round(g.loc[g["Call Type"]=="IC","_dur_min"].sum()*60)),
            "OG (Seconds)": int(round(g.loc[g["Call Type"]=="OG","_dur_min"].sum()*60)),
            "Total Seconds": int(round(g["_dur_min"].sum()*60)),
            "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "",
            "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "",
            "Total Days": int(g["Date"].nunique()),
        })
    summary = pd.DataFrame(summ_rows).sort_values("Total", ascending=False) if summ_rows else pd.DataFrame(columns=["A","B","IC","ISMS","OG","OSMS","Total","IC (Seconds)","OG (Seconds)","Total Seconds","First Call","Last Call","Total Days"])
    loc_base = df[df["Call Type"] != "DATA"].copy()
    loc_rows = []
    for loc, g in loc_base.groupby("Location"):
        loc_rows.append({
            "Location": loc,
            "IC": int((g["Call Type"]=="IC").sum()),
            "ISMS": int((g["Call Type"]=="ISMS").sum()),
            "OG": int((g["Call Type"]=="OG").sum()),
            "OSMS": int((g["Call Type"]=="OSMS").sum()),
            "Total": len(g),
            "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "",
            "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "",
            "T_Locations": int(g["Location"].nunique()),
            "T_Days": int(g["Date"].nunique()),
        })
    loc_sum = pd.DataFrame(loc_rows).sort_values("Total", ascending=False) if loc_rows else pd.DataFrame(columns=["Location","IC","ISMS","OG","OSMS","Total","First Call","Last Call","T_Locations","T_Days"])
    imei_rows = []
    for imei, g in df.groupby("IMEI"):
        _nd = g[g["Call Type"] != "DATA"]
        imei_rows.append({
            "IMEI": imei,
            "OG": int((g["Call Type"]=="OG").sum()),
            "ISMS": int((g["Call Type"]=="ISMS").sum()),
            "IC": int((g["Call Type"]=="IC").sum()),
            "OSMS": int((g["Call Type"]=="OSMS").sum()),
            "Total": len(_nd),
            "Total Duration": int(g["Duration"].sum()),
            "First Use": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "",
            "Last Use": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "",
            "Days Used": int(g["Date"].nunique()),
        })
    imei_sum = pd.DataFrame(imei_rows).sort_values("Total", ascending=False) if imei_rows else pd.DataFrame(columns=["IMEI","OG","ISMS","IC","OSMS","Total","Total Duration","First Use","Last Use","Days Used"])
    night = df.copy()
    _t = pd.to_datetime(night["Time"], errors="coerce")
    night["_hour"] = _t.dt.hour + _t.dt.minute/60
    night = night[(night["_hour"] >= 2) & (night["_hour"] < 8)]
    if len(night) > 0:
        night_rows = []
        for (d, loc, lac, cid), g in night.groupby(["Date","Location","LAC","CID"]):
            night_rows.append({
                "Date": d, "Location": loc, "LAC": lac, "CID": cid,
                "Night Count": len(g),
                "First Call": g["Time"].min(), "Last Call": g["Time"].max(),
                "Total Locations": int(g["Location"].nunique()),
            })
        night_sum = pd.DataFrame(night_rows).sort_values(["Date","Night Count"], ascending=[True, False])
    else:
        night_sum = pd.DataFrame([{"Date":"No record 02:00-08:00","Location":"","LAC":"","CID":"","Night Count":0,"First Call":"","Last Call":"","Total Locations":0}])
    return raw, cdr_data, summary, loc_sum, imei_sum, night_sum

# ===== CDR JAZZ - NAYA - UFONE JAISE 6 SHEETS =====
def decode_jazz_bparty(v):
    s = str(v).strip()
    if s == "" or s.lower() == "nan":
        return ""
    # Agar Hex me naam hai - jaise 4A617A7A = Jazz, 53455454494E47 = SETTING - to decode karo
    # Sirf tab jab length even hai, sab Hex chars hain, aur decode hone ke baad sab printable letters hain
    try:
        if len(s) % 2 == 0 and len(s) >= 4 and all(c in "0123456789ABCDEFabcdef" for c in s):
            b = bytes([int(s[i:i+2], 16) for i in range(0, len(s), 2)])
            txt = b.decode("ascii", errors="strict")
            if all(32 <= ord(ch) <= 126 for ch in txt) and any(ch.isalpha() for ch in txt):
                return txt.strip()
    except:
        pass
    # Warna number hai - 92 / 0 hatao
    return clean_number(s)

def jazz_cdr_lac_cid(cell_val):
    s = str(cell_val).strip().upper()
    if s == "" or s.lower() == "nan":
        return "", ""
    # 7 digit ho to aage 0 laga ke 8 karo
    if len(s) < 8:
        s = s.zfill(8)
    s = s[:8]
    # Jazz BTS wala ulta formula - pehle 4 ulta = LAC, baad wale 4 ulta = CID
    lac_hex = s[:4][::-1]
    cell_hex = s[4:8][::-1]
    try: lac = int(lac_hex, 16)
    except: lac = ""
    try: cid = int(cell_hex, 16)
    except: cid = ""
    return lac, cid

def parse_jazz_site_location(v):
    s = str(v).strip()
    if s == "" or s.lower() == "nan" or s == "?":
        return "?", "", ""
    parts = s.split("|")
    loc = parts[0].strip()
    lat = parts[1].strip() if len(parts) > 1 else ""
    lng = parts[2].strip() if len(parts) > 2 else ""
    return loc, lat, lng

def read_cdr_jazz_file(f):
    lname = f.name.lower()
    f.seek(0)
    if lname.endswith(".csv"):
        try:
            return pd.read_csv(f, dtype=str, encoding="utf-8")
        except:
            f.seek(0)
            return pd.read_csv(f, dtype=str, encoding="latin1")
    elif lname.endswith(".xlsx") or lname.endswith(".xls"):
        xls = pd.ExcelFile(f)
        for sh in xls.sheet_names:
            try:
                tmp = pd.read_excel(f, sheet_name=sh, dtype=str, nrows=2)
                cols = [str(c).strip().upper() for c in tmp.columns]
                if "APARTY" in cols or "A PARTY" in cols:
                    return pd.read_excel(f, sheet_name=sh, dtype=str)
            except:
                continue
        return pd.read_excel(f, sheet_name=0, dtype=str)
    return None

def build_cdr_jazz_output(raw_df):
    raw = raw_df.copy()
    raw.columns = [str(c).strip() for c in raw.columns]
    cmap = {str(c).strip().upper(): str(c).strip() for c in raw.columns}
    def col(*names):
        for n in names:
            if n.upper() in cmap:
                return cmap[n.upper()]
        return None
    cCALL = col("CallType","Call Type"); cA = col("Aparty","A Party","A"); cB = col("BParty","B Party","B")
    cDT = col("Datetime","DateTime"); cDUR = col("Duration","DUR")
    cCELL = col("cellid","Cell Id","Cell ID"); cIMEI = col("Imei","IMEI"); cSITE = col("SiteLocation","Site Location")
    df = pd.DataFrame()
    df["A Party"] = raw[cA].apply(clean_number) if cA else ""
    df["B Party"] = raw[cB].apply(decode_jazz_bparty) if cB else ""
    # CallType - InComing = IC, Outgoing = OG, Incoming SMS = ISMS, Outgoing SMS = OSMS
    _ct = raw[cCALL].astype(str).str.strip() if cCALL else pd.Series([""]*len(raw))
    calltypes = []
    for t in _ct:
        tl = t.strip().lower()
        if tl == "incoming sms":
            calltypes.append("ISMS")
        elif tl == "outgoing sms":
            calltypes.append("OSMS")
        elif tl == "incoming":
            calltypes.append("IC")
        elif tl == "outgoing":
            calltypes.append("OG")
        else:
            calltypes.append(t)
    df["Call Type"] = calltypes
    _dt = pd.to_datetime(raw[cDT], errors="coerce") if cDT else pd.Series([pd.NaT]*len(raw))
    df["Date"] = _dt.dt.strftime("%Y-%m-%d")
    df["Time"] = _dt.dt.strftime("%H:%M:%S")
    df["Duration"] = pd.to_numeric(raw[cDUR], errors="coerce").fillna(0).astype(int) if cDUR else 0
    lac_list = []; cid_list = []
    if cCELL:
        for v in raw[cCELL]:
            l, c = jazz_cdr_lac_cid(v)
            lac_list.append(l); cid_list.append(c)
    else:
        lac_list = [""]*len(raw); cid_list = [""]*len(raw)
    df["LAC"] = lac_list
    df["CID"] = cid_list
    df["IMEI"] = raw[cIMEI].astype(str).str.strip() if cIMEI else ""
    loc_list = []; lat_list = []; lng_list = []
    if cSITE:
        for v in raw[cSITE]:
            lo, la, ln = parse_jazz_site_location(v)
            loc_list.append(lo); lat_list.append(la); lng_list.append(ln)
    else:
        loc_list = [""]*len(raw); lat_list = [""]*len(raw); lng_list = [""]*len(raw)
    df["Location"] = loc_list
    df["LAT"] = lat_list
    df["LNG"] = lng_list
    df["_dt"] = _dt
    df["_dur_min"] = df["Duration"] / 60.0
    # CDR Data - Ufone jaisi 12 column
    cdr_data = df[["Call Type","A Party","B Party","Date","Time","Duration","IMEI","LAC","CID","Location","LAT","LNG"]].copy()
    # Summary - Ufone jaisa - DATA column nahi, Total Locations nahi
    summ_base = df[df["Call Type"] != "DATA"].copy()
    summ_rows = []
    for (a,b), g in summ_base.groupby(["A Party","B Party"]):
        summ_rows.append({
            "A": a, "B": b,
            "IC": int((g["Call Type"]=="IC").sum()),
            "ISMS": int((g["Call Type"]=="ISMS").sum()),
            "OG": int((g["Call Type"]=="OG").sum()),
            "OSMS": int((g["Call Type"]=="OSMS").sum()),
            "Total": len(g),
            "IC (Seconds)": round(g.loc[g["Call Type"]=="IC","_dur_min"].sum()*60, 2),
            "OG (Seconds)": round(g.loc[g["Call Type"]=="OG","_dur_min"].sum()*60, 2),
            "Total Seconds": round(g["_dur_min"].sum()*60, 2),
            "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "",
            "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "",
            "Total Days": int(g["Date"].nunique()),
        })
    summary = pd.DataFrame(summ_rows).sort_values("Total", ascending=False) if summ_rows else pd.DataFrame(columns=["A","B","IC","ISMS","OG","OSMS","Total","IC (Seconds)","OG (Seconds)","Total Seconds","First Call","Last Call","Total Days"])
    # Location Summary - DATA column nahi
    loc_base = df[df["Call Type"] != "DATA"].copy()
    loc_rows = []
    for loc, g in loc_base.groupby("Location"):
        loc_rows.append({
            "Location": loc,
            "IC": int((g["Call Type"]=="IC").sum()),
            "ISMS": int((g["Call Type"]=="ISMS").sum()),
            "OG": int((g["Call Type"]=="OG").sum()),
            "OSMS": int((g["Call Type"]=="OSMS").sum()),
            "Total": len(g),
            "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "",
            "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "",
            "T_Locations": int(g["Location"].nunique()),
            "T_Days": int(g["Date"].nunique()),
        })
    loc_sum = pd.DataFrame(loc_rows).sort_values("Total", ascending=False) if loc_rows else pd.DataFrame(columns=["Location","IC","ISMS","OG","OSMS","Total","First Call","Last Call","T_Locations","T_Days"])
    # IMEI Summary - Ufone jaisa
    imei_rows = []
    for imei, g in df.groupby("IMEI"):
        _nd = g[g["Call Type"] != "DATA"]
        imei_rows.append({
            "IMEI": imei,
            "OG": int((g["Call Type"]=="OG").sum()),
            "ISMS": int((g["Call Type"]=="ISMS").sum()),
            "IC": int((g["Call Type"]=="IC").sum()),
            "OSMS": int((g["Call Type"]=="OSMS").sum()),
            "Total": len(_nd),
            "Total Duration": int(g["Duration"].sum()),
            "First Use": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "",
            "Last Use": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "",
            "Days Used": int(g["Date"].nunique()),
        })
    imei_sum = pd.DataFrame(imei_rows).sort_values("Total", ascending=False) if imei_rows else pd.DataFrame(columns=["IMEI","OG","ISMS","IC","OSMS","Total","Total Duration","First Use","Last Use","Days Used"])
    # Night Stay - 2am to 8am - First Call / Last Call / Total Locations
    night = df.copy()
    _t = pd.to_datetime(night["Time"], errors="coerce")
    night["_hour"] = _t.dt.hour + _t.dt.minute/60
    night = night[(night["_hour"] >= 2) & (night["_hour"] < 8)]
    if len(night) > 0:
        night_rows = []
        for (d, loc, lac, cid), g in night.groupby(["Date","Location","LAC","CID"]):
            night_rows.append({
                "Date": d, "Location": loc, "LAC": lac, "CID": cid,
                "Night Count": len(g),
                "First Call": g["Time"].min(), "Last Call": g["Time"].max(),
                "Total Locations": int(g["Location"].nunique()),
            })
        night_sum = pd.DataFrame(night_rows).sort_values(["Date","Night Count"], ascending=[True, False])
    else:
        night_sum = pd.DataFrame([{"Date":"No record 02:00-08:00","Location":"","LAC":"","CID":"","Night Count":0,"First Call":"","Last Call":"","Total Locations":0}])
    return raw, cdr_data, summary, loc_sum, imei_sum, night_sum

# ==================== TAB 1 - UFONE BTS - .txt ====================
if selected_tab == 0 and st.session_state.mode == "BTS":
    st.subheader("Ufone - .txt files")
    uploaded_files = st.file_uploader("Upload Ufone .txt files", type=["txt"], accept_multiple_files=True, key="ufone")
    if uploaded_files:
        all_dfs=[]
        for uploaded in uploaded_files:
            try: df=pd.read_csv(uploaded, sep="\t", encoding="utf-16", dtype=str)
            except: uploaded.seek(0); df=pd.read_csv(uploaded, sep="\t", encoding="utf-8", dtype=str)
            df.columns=[c.strip() for c in df.columns]; all_dfs.append(df)
        df=pd.concat(all_dfs, ignore_index=True); dt=pd.to_datetime(df["CALL_START_TIME"], errors="coerce")
        final=pd.DataFrame(); final["Call Type"]=[("In SMS" if ("INCOMING" in str(_d).upper() or "INBOUND" in str(_d).upper()) else "Out SMS") if "SMS" in str(_t).upper() else ("In Call" if ("INCOMING" in str(_d).upper() or "INBOUND" in str(_d).upper()) else "Out Call") if ("VOICE" in str(_t).upper() or "CALL" in str(_t).upper()) else ("Data In" if ("INCOMING" in str(_d).upper() or "INBOUND" in str(_d).upper()) else "Data Out") if ("DATA" in str(_t).upper() or "INTERNET" in str(_t).upper() or "GPRS" in str(_t).upper()) else "Out Call" for _t, _d in zip(df["CALL_TYPE_NAME"].astype(str), df["CALL_INBOUND_OUTBOUND_DESC"].astype(str))]; final["A Party"]=df["A_NUMBER"].apply(clean_number); final["B Party"]=df["B_NUMBER"].apply(clean_number); final["Date"]=dt.dt.strftime("%d-%m-%y"); final["Time"]=dt.dt.strftime("%H:%M:%S"); final["Duration"]=pd.to_numeric(df["CALL_DURATION"], errors="coerce").fillna(0).astype(int); final["IMEI"]=df["IMEI"]; cell=df["CELL_ID"].astype(str).str.strip(); final["LAC"]=cell.str[:5]; final["Cell ID"]=cell.str[5:]; final["Network"]="UFONE"; final=add_extra_columns(final, dt)
        st.success(f"Done! {len(uploaded_files)} files, Total {len(final)} calls, {final['A Party'].nunique()} alag numbers")
        download_section(final, "Ufone_Cleaned.xlsx")

# ==================== TAB 2 - JAZZ BTS ====================
if selected_tab == 1 and st.session_state.mode == "BTS":
    st.subheader("Jazz - .xlsx files")
    uploaded_jazz = st.file_uploader("Upload Jazz .xlsx files", type=["xlsx","xls"], accept_multiple_files=True, key="jazz")
    if uploaded_jazz:
        all_dfs=[]
        for uploaded in uploaded_jazz:
            df=pd.read_excel(uploaded, dtype=str); df.columns=[c.strip() for c in df.columns]; all_dfs.append(df)
        df=pd.concat(all_dfs, ignore_index=True); raw=pd.to_numeric(df["Date And Time"], errors="coerce"); dt=pd.to_datetime(raw, unit="D", origin="1899-12-30", errors="coerce").combine_first(pd.to_datetime(df["Date And Time"], errors="coerce"))
        def jazz_lac_cell(cell_val):
            s=str(cell_val).strip(); lac_hex=s[:4][::-1]; cell_hex=s[4:8][::-1]
            try: lac=int(lac_hex,16)
            except: lac=""
            try: cellid=int(cell_hex,16)
            except: cellid=""
            return lac,cellid
        lac_list=[]; cell_list=[]
        for v in df["Cell ID"]:
            l,c=jazz_lac_cell(v); lac_list.append(l); cell_list.append(c)
        final=pd.DataFrame(); final["Call Type"]=[("In SMS" if "INCOMING" in str(_t).upper() else "Out SMS") if "SMS" in str(_t).upper() else ("In Call" if "INCOMING" in str(_t).upper() else "Out Call") for _t in df["Call Type"].astype(str)]; final["A Party"]=df["A-Party"].apply(clean_number); final["B Party"]=df["B-Party"].apply(clean_number); final["Date"]=dt.dt.strftime("%d-%m-%y"); final["Time"]=dt.dt.strftime("%H:%M:%S"); final["Duration"]=pd.to_numeric(df["Duration"], errors="coerce").fillna(0).astype(int); final["IMEI"]=df["IMEI"]; final["LAC"]=lac_list; final["Cell ID"]=cell_list; final["Network"]="JAZZ"; final=add_extra_columns(final, dt)
        st.success(f"Done! {len(uploaded_jazz)} files, Total {len(final)} calls, {final['A Party'].nunique()} alag numbers")
        download_section(final, "Jazz_Cleaned.xlsx")

# ==================== TAB 3 - TELENOR BTS ====================
if selected_tab == 2 and st.session_state.mode == "BTS":
    st.subheader("Telenor - .csv files")
    uploaded_telenor = st.file_uploader("Upload Telenor Incoming + Outgoing .csv files", type=["csv"], accept_multiple_files=True, key="telenor")
    if uploaded_telenor:
        all_final=[]
        for uploaded in uploaded_telenor:
            df=pd.read_csv(uploaded, dtype=str); df.columns=[c.strip() for c in df.columns]; df=df.dropna(subset=["MSISDN"]); df=df[df["MSISDN"].astype(str).str.strip()!=""]; dt=df["CALL_START_DT_TM"].apply(parse_telenor_date); tmp=pd.DataFrame(); ind=df["INBOUND_OUTBOUND_IND"].astype(str).str.strip(); direction=ind.map({"0":"INTERNET","1":"OUTGOING","2":"INCOMING"}).fillna(ind); real_type=df["CALL_TYPE"].astype(str).str.strip().str.upper() if "CALL_TYPE" in df.columns else pd.Series(["CALL"]*len(df)); merged=[]
            for d,t in zip(direction, real_type):
                if t=="GPRS" or d=="INTERNET": merged.append("GPRS")
                elif d=="INCOMING" and t=="CALL": merged.append("In Call")
                elif d=="OUTGOING" and t=="CALL": merged.append("Out Call")
                elif d=="INCOMING" and t=="SMS": merged.append("In SMS")
                elif d=="OUTGOING" and t=="SMS": merged.append("Out SMS")
                elif d=="INCOMING": merged.append("In "+t.title())
                elif d=="OUTGOING": merged.append("Out "+t.title())
                else: merged.append(t.title())
            tmp["Call Type"]=merged; tmp["A Party"]=df["MSISDN"].apply(clean_number); tmp["B Party"]=df["CALL_DIALED_NUM"].apply(clean_number) if "CALL_DIALED_NUM" in df.columns else df["CALL_ORIG_NUM"].apply(clean_number); tmp["Date"]=dt.dt.strftime("%d-%m-%y"); tmp["Time"]=dt.dt.strftime("%H:%M:%S"); tmp["Duration"]=pd.to_numeric(df["Call_Network_Volume"], errors="coerce").fillna(0).astype(int); tmp["IMEI"]=df["IMEI"]; tmp["LAC"]=df["Lac_Id"]; tmp["Cell ID"]=df["Site_Id"]; tmp["Network"]="TELENOR"; tmp["_dt"]=dt; all_final.append(tmp)
        final=pd.concat(all_final, ignore_index=True); dt_all=final["_dt"]; final=final.drop(columns=["_dt"]); final=add_extra_columns(final, dt_all)
        st.success(f"Done! {len(uploaded_telenor)} files, Total {len(final)} calls, {final['A Party'].nunique()} alag numbers")
        download_section(final, "Telenor_Cleaned.xlsx")

# ==================== TAB 4 - ZONG BTS ====================
if selected_tab == 3 and st.session_state.mode == "BTS":
    st.subheader("Zong - .xlsx files")
    uploaded_zong = st.file_uploader("Upload Zong .xlsx files", type=["xlsx","xls"], accept_multiple_files=True, key="zong")
    if uploaded_zong:
        all_dfs=[]
        for uploaded in uploaded_zong:
            df=pd.read_excel(uploaded, dtype=str); df.columns=[c.strip() for c in df.columns]; all_dfs.append(df)
        df=pd.concat(all_dfs, ignore_index=True); dt=pd.to_datetime(df["STRT_TM"], errors="coerce"); final=pd.DataFrame(); dir_col=df["DIR_FLG"].astype(str).str.strip().str.lower(); final["Call Type"]=dir_col.map({"incomming":"In Call","incoming":"In Call","outgoing":"Out Call","outcomming":"Out Call"}).fillna(df["DIR_FLG"]); final["A Party"]=df["DLG_NO"].apply(clean_number); final["B Party"]=df["DLD_NO"].apply(clean_number); final["Date"]=dt.dt.strftime("%d-%m-%y"); final["Time"]=dt.dt.strftime("%H:%M:%S")
        _cols = {str(c).strip().upper(): str(c).strip() for c in df.columns}
        _min_col = None; _sec_col = None
        for k,v in _cols.items():
            if "MIN" in k and "MINUTE" in k:
                _min_col = v
            if k == "SEC" or "SECOND" in k:
                _sec_col = v
        if _min_col is not None and _sec_col is not None:
            _m = pd.to_numeric(df[_min_col], errors="coerce").fillna(0)
            _s = pd.to_numeric(df[_sec_col], errors="coerce").fillna(0)
            final["Duration"] = (_m*60 + _s).astype(int)
        else:
            final["Duration"]=pd.to_numeric(df["DRTN"], errors="coerce").fillna(0).astype(int)
        imei_1=df["CLD_IMIE"].astype(str).str.strip() if "CLD_IMIE" in df.columns else ""; imei_2=df["CLG_IMEI"].astype(str).str.strip() if "CLG_IMEI" in df.columns else ""; merged_imei=[]
        for a,b in zip(imei_1, imei_2):
            if str(a).strip() != "" and str(a).lower() != "nan": merged_imei.append(str(a).strip())
            elif str(b).strip() != "" and str(b).lower() != "nan": merged_imei.append(str(b).strip())
            else: merged_imei.append("")
        final["IMEI"]=merged_imei; final["LAC"]=df["LAC_ID"]; final["Cell ID"]=df["CELL_ID"]; final["Network"]="ZONG"; final=add_extra_columns(final, dt)
        st.success(f"Done! {len(uploaded_zong)} files, Total {len(final)} calls, {final['A Party'].nunique()} alag numbers")
        download_section(final, "Zong_Cleaned.xlsx")

# ==================== TAB 5 - ALL BTS ====================
if selected_tab == 4 and st.session_state.mode == "BTS":
    st.subheader("All BTS")
    st.info("Ufone + Jazz + Telenor + Zong Upload all files together")
    c1,c2,c3,c4=st.columns(4)
    with c1: filter_date=st.date_input("Date - BTS", value=dt_date(2026,10,22))
    with c2: start_time=st.time_input("Start Time", value=pd.to_datetime("00:00").time())
    with c3: end_time=st.time_input("End Time", value=pd.to_datetime("23:59").time())
    with c4: use_filter=st.checkbox("Date + Time Filter Lagao", value=False)
    uploaded_all=st.file_uploader("Upload All BTS files - txt / xlsx / csv", type=["txt","xlsx","xls","csv"], accept_multiple_files=True, key="all_bts")
    if uploaded_all:
        all_final=[]
        for uploaded in uploaded_all:
            fname=uploaded.name; lname=fname.lower()
            try:
                if lname.endswith(".txt"):
                    try: uploaded.seek(0); df_raw=pd.read_csv(uploaded, sep="\t", encoding="utf-16", dtype=str)
                    except: uploaded.seek(0); df_raw=pd.read_csv(uploaded, sep="\t", encoding="utf-8", dtype=str)
                elif lname.endswith(".csv"): uploaded.seek(0); df_raw=pd.read_csv(uploaded, dtype=str)
                else: uploaded.seek(0); df_raw=pd.read_excel(uploaded, dtype=str)
            except Exception as e: st.warning(f"{fname} nahi khuli: {e}"); continue
            df_raw.columns=[c.strip() for c in df_raw.columns]; net=detect_network(df_raw, fname)
            if net=="UFONE":
                _tmp = parse_ufone_df(df_raw)
                _tmp["A Party"] = _tmp["A Party"].astype(str).str.lstrip("0").str.replace(r"^92", "", regex=True)
                all_final.append(_tmp)
            elif net=="JAZZ": all_final.append(parse_jazz_df(df_raw))
            elif net=="TELENOR": all_final.append(parse_telenor_df(df_raw))
            elif net=="ZONG": all_final.append(parse_zong_df(df_raw))
            else: st.warning(f"{fname} - Network pehchana nahi gaya, skip kar diya")
        if all_final:
            merged=pd.concat(all_final, ignore_index=True); total_before=len(merged)
            if use_filter:
                mask=(merged["_dt"].dt.date==filter_date)&(merged["_dt"].dt.time>=start_time)&(merged["_dt"].dt.time<=end_time); merged=merged[mask]; st.success(f"Filter Laga! Pura: {total_before} | Filter ke baad: {len(merged)}")
            else: st.success(f"Done! {len(uploaded_all)} files, Total {len(merged)} calls")
            if len(merged)>0:
                dt_all=merged["_dt"]; final=merged.drop(columns=["_dt"]); final=add_extra_columns(final, dt_all); st.dataframe(final.groupby("Network").agg(Total_Calls=("Call Type","count")).reset_index()); download_section(final, "All_BTS_Merged.xlsx")

# ================= TAB 6 - CDR UFONE - LOCK - NA CHHERNA =================
if selected_tab == 0 and st.session_state.mode == "CDR":
    st.subheader("CDR - Ufone - Standardized")
    st.info("Ufone CDR Raw - .xlsx / .csv")
    up = st.file_uploader("Upload Ufone CDR Raw - .xlsx / .csv", type=["xlsx","xls","csv"], accept_multiple_files=True, key="cdr_ufone")
    if up:
        raws=[]
        for f in up:
            d = read_cdr_ufone_file(f)
            if d is not None:
                d.columns=[str(c).strip() for c in d.columns]
                raws.append(d)
        if raws:
            raw_all = pd.concat(raws, ignore_index=True)
            raw_out, cdr_data, summary, loc_sum, imei_sum, night_sum = build_cdr_ufone_output(raw_all)
            st.success(f"Done! Total {len(cdr_data)} rows | Summary  {len(summary)} unique B numbers")
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                raw_out.to_excel(writer, index=False, sheet_name="Raw Data")
                cdr_data.to_excel(writer, index=False, sheet_name="CDR Data")
                summary.to_excel(writer, index=False, sheet_name="Summary")
                loc_sum.to_excel(writer, index=False, sheet_name="Location Summary")
                imei_sum.to_excel(writer, index=False, sheet_name="IMEI Summary")
                night_sum.to_excel(writer, index=False, sheet_name="Night Stay")
            st.download_button(label="📥 CDR Ufone Standardized Download the Excel file - 6 Sheets - No Addresses", data=output.getvalue(), file_name="Ufone_CDR_Standardized.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            st.write("**Preview - CDR Data**"); st.dataframe(cdr_data.head(20))
            c1,c2,c3 = st.columns(3)
            with c1: st.write("**Summary by Numbers**"); st.dataframe(summary)
            with c2: st.write("**Summary by Location**"); st.dataframe(loc_sum)
            with c3: st.write("**IMEI Summary**"); st.dataframe(imei_sum)
            st.write("**Night Stay (02:00 - 08:00)**"); st.dataframe(night_sum)

# ================= TAB 7 - CDR JAZZ - NAYA - UFONE JAISA =================
if selected_tab == 1 and st.session_state.mode == "CDR":
    st.subheader("CDR - Jazz - Standardized")
    st.info("Jazz CDR Raw - .xlsx / .csv")
    upj = st.file_uploader("Upload Jazz CDR Raw - .xlsx / .csv", type=["xlsx","xls","csv"], accept_multiple_files=True, key="cdr_jazz")
    if upj:
        raws=[]
        for f in upj:
            d = read_cdr_jazz_file(f)
            if d is not None:
                d.columns=[str(c).strip() for c in d.columns]
                raws.append(d)
        if raws:
            raw_all = pd.concat(raws, ignore_index=True)
            raw_out, cdr_data, summary, loc_sum, imei_sum, night_sum = build_cdr_jazz_output(raw_all)
            st.success(f"Done! Total {len(cdr_data)} rows | Summary  {len(summary)} unique B numbers")
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                raw_out.to_excel(writer, index=False, sheet_name="Raw Data")
                cdr_data.to_excel(writer, index=False, sheet_name="CDR Data")
                summary.to_excel(writer, index=False, sheet_name="Summary")
                loc_sum.to_excel(writer, index=False, sheet_name="Location Summary")
                imei_sum.to_excel(writer, index=False, sheet_name="IMEI Summary")
                night_sum.to_excel(writer, index=False, sheet_name="Night Stay")
            st.download_button(label="📥 CDR Jazz Standardized Download the Excel file - 6 Sheets - No Addresses", data=output.getvalue(), file_name="Jazz_CDR_Standardized.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            st.write("**Preview - CDR Data**"); st.dataframe(cdr_data.head(20))
            c1,c2,c3 = st.columns(3)
            with c1: st.write("**Summary by Numbers**"); st.dataframe(summary)
            with c2: st.write("**Summary by Locations**"); st.dataframe(loc_sum)
            with c3: st.write("**IMEI Summary**"); st.dataframe(imei_sum)
            st.write("**Night Stay (02:00 - 08:00)**"); st.dataframe(night_sum)

# ===== CDR TELENOR - SIRF TELENOR - BTS / UFONE / JAZZ / ZONG KO HATH NAHI =====
def clean_telenor_id(v):
    s = str(v).strip()
    if s == "" or s.lower() == "nan":
        return ""
    # 504.0 -> 504 , 25062.0 -> 25062
    if s.endswith(".0"):
        s = s[:-2]
    return s

def decode_telenor_bparty(v):
    s = str(v).strip()
    if s == "" or s.lower() == "nan":
        return ""
    # Naam - Telenorx waisa hi
    if any(ch.isalpha() for ch in s):
        return s
    # International - 00 se shuru - waisa hi - 00966568874167
    if s.startswith("00"):
        return s
    # Chhota code - 6 ya kam - waisa hi - 5120 , 7879 , 92345
    if len(s) <= 6:
        return s
    # 92 wala - 923418937944 -> 3418937944
    if s.startswith("+92"):
        return s[3:]
    if s.startswith("92") and len(s) == 12:
        return s[2:]
    # Asal mobile - 11 digit 0 se - 031... -> 31...
    if len(s) == 11 and s.startswith("0"):
        return s[1:]
    return s

def read_cdr_telenor_file(f):
    f.seek(0)
    name = getattr(f, "name", "").lower()
    if name.endswith(".csv"):
        parsed = pd.read_csv(f, dtype=str)
    else:
        parsed = pd.read_excel(f, dtype=str)
    parsed.columns = [str(c).strip() for c in parsed.columns]
    return parsed, parsed

def build_cdr_telenor_output(raw_df):
    raw = raw_df.copy()
    raw.columns = [str(c).strip() for c in raw.columns]
    cmap = {str(c).strip().upper(): str(c).strip() for c in raw.columns}
    def col(*ns):
        for n in ns:
            if n.upper() in cmap:
                return cmap[n.upper()]
        return None
    cA = col("MSISDN")
    cB = col("call_org_num")
    cC = col("CALL_DIALED_NUM")
    cH = col("INBOUND_OUTBOUND_IND")
    cO = col("CALL_TYPE")
    cStart = col("CALL_START_DT_TM")
    cEnd = col("CALL_END_DT_TM")
    cVol = col("Call_Network_Volume")
    cLAC = col("Lac_Id")
    cCID = col("Site_Id")
    cIMEI = col("IMEI")
    cLoc = col("location")
    cLAT = col("lat")
    cLNG = col("longitude")
    df = pd.DataFrame()
    df["A Party"] = raw[cA].apply(decode_telenor_bparty) if cA else ""
    b_list = []
    for i, row in raw.iterrows():
        h = str(row[cH]).strip().upper() if cH else ""
        if h == "INCOMING":
            b_list.append(decode_telenor_bparty(row[cB]) if cB else "")
        else:
            b_list.append(decode_telenor_bparty(row[cC]) if cC else "")
    df["B Party"] = b_list
    ct = []
    for i, row in raw.iterrows():
        h = str(row[cH]).strip().upper() if cH else ""
        o = str(row[cO]).strip().upper() if cO else ""
        if h == "INCOMING" and o == "SMS":
            ct.append("ISMS")
        elif h == "INCOMING" and o == "CALL":
            ct.append("IC")
        elif h == "OUTGOING" and o == "SMS":
            ct.append("OSMS")
        elif h == "OUTGOING" and o == "CALL":
            ct.append("OG")
        else:
            ct.append(o)
    df["Call Type"] = ct
    dt = pd.to_datetime(raw[cStart], errors="coerce") if cStart else pd.Series([pd.NaT]*len(raw))
    df["Date"] = dt.dt.strftime("%Y-%m-%d")
    df["Time"] = dt.dt.strftime("%H:%M:%S")
    if cStart and cEnd:
        dt_end = pd.to_datetime(raw[cEnd], errors="coerce")
        dur = (dt_end - dt).dt.total_seconds()
        dur = dur.fillna(0).clip(lower=0).astype(int)
    elif cVol:
        dur = pd.to_numeric(raw[cVol], errors="coerce").fillna(0).astype(int)
    else:
        dur = pd.Series([0]*len(raw))
    df["Duration"] = dur
    df["LAC"] = raw[cLAC].apply(clean_telenor_id) if cLAC else ""
    df["CID"] = raw[cCID].apply(clean_telenor_id) if cCID else ""
    df["IMEI"] = raw[cIMEI].astype(str).str.strip() if cIMEI else ""
    df["IMEI"] = df["IMEI"].replace("nan", "")
    df["Location"] = raw[cLoc].astype(str).str.strip() if cLoc else ""
    df["Location"] = df["Location"].replace("nan", "")
    df["LAT"] = raw[cLAT].astype(str).str.strip() if cLAT else ""
    df["LAT"] = df["LAT"].replace("nan", "")
    df["LNG"] = raw[cLNG].astype(str).str.strip() if cLNG else ""
    df["LNG"] = df["LNG"].replace("nan", "")
    df["_dt"] = dt
    df["_dur_min"] = df["Duration"] / 60.0
    cdr_data = df[["Call Type","A Party","B Party","Date","Time","Duration","IMEI","LAC","CID","Location","LAT","LNG"]].copy()
    base = df[df["Call Type"] != "DATA"].copy()
    sr = []
    for (a,b), g in base.groupby(["A Party","B Party"]):
        sr.append({"A": a, "B": b, "IC": int((g["Call Type"]=="IC").sum()), "ISMS": int((g["Call Type"]=="ISMS").sum()), "OG": int((g["Call Type"]=="OG").sum()), "OSMS": int((g["Call Type"]=="OSMS").sum()), "Total": len(g), "IC (Seconds)": round(g.loc[g["Call Type"]=="IC","_dur_min"].sum()*60, 2), "OG (Seconds)": round(g.loc[g["Call Type"]=="OG","_dur_min"].sum()*60, 2), "Total Seconds": round(g["_dur_min"].sum()*60, 2), "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "", "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "", "Total Days": int(g["Date"].nunique())})
    summary = pd.DataFrame(sr).sort_values("Total", ascending=False) if sr else pd.DataFrame(columns=["A","B","IC","ISMS","OG","OSMS","Total","IC (Seconds)","OG (Seconds)","Total Seconds","First Call","Last Call","Total Days"])
    lr = []
    for loc, g in base.groupby("Location"):
        lr.append({"Location": loc, "IC": int((g["Call Type"]=="IC").sum()), "ISMS": int((g["Call Type"]=="ISMS").sum()), "OG": int((g["Call Type"]=="OG").sum()), "OSMS": int((g["Call Type"]=="OSMS").sum()), "Total": len(g), "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "", "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "", "T_Locations": int(g["Location"].nunique()), "T_Days": int(g["Date"].nunique())})
    loc_sum = pd.DataFrame(lr).sort_values("Total", ascending=False) if lr else pd.DataFrame(columns=["Location","IC","ISMS","OG","OSMS","Total","First Call","Last Call","T_Locations","T_Days"])
    ir = []
    for imei, g in df.groupby("IMEI"):
        nd = g[g["Call Type"] != "DATA"]
        ir.append({"IMEI": imei, "OG": int((g["Call Type"]=="OG").sum()), "ISMS": int((g["Call Type"]=="ISMS").sum()), "IC": int((g["Call Type"]=="IC").sum()), "OSMS": int((g["Call Type"]=="OSMS").sum()), "Total": len(nd), "Total Duration": int(g["Duration"].sum()), "First Use": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "", "Last Use": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "", "Days Used": int(g["Date"].nunique())})
    imei_sum = pd.DataFrame(ir).sort_values("Total", ascending=False) if ir else pd.DataFrame(columns=["IMEI","OG","ISMS","IC","OSMS","Total","Total Duration","First Use","Last Use","Days Used"])
    night = df.copy()
    tt = pd.to_datetime(night["Time"], errors="coerce")
    night["_hour"] = tt.dt.hour + tt.dt.minute/60
    night = night[(night["_hour"] >= 2) & (night["_hour"] < 8)]
    if len(night) > 0:
        nr = []
        for (d, loc, lac, cid), g in night.groupby(["Date","Location","LAC","CID"]):
            nr.append({"Date": d, "Location": loc, "LAC": lac, "CID": cid, "Night Count": len(g), "First Call": g["Time"].min(), "Last Call": g["Time"].max(), "Total Locations": int(g["Location"].nunique())})
        night_sum = pd.DataFrame(nr).sort_values(["Date","Night Count"], ascending=[True, False])
    else:
        night_sum = pd.DataFrame([{"Date": "No record 02:00-08:00", "Location": "", "LAC": "", "CID": "", "Night Count": 0, "First Call": "", "Last Call": "", "Total Locations": 0}])
    return raw, cdr_data, summary, loc_sum, imei_sum, night_sum

# ===== TAB 8 - CDR TELENOR =====
if selected_tab == 2 and st.session_state.mode == "CDR":
    st.subheader("CDR - Telenor - Standardized")
    st.info("Telenor CDR Raw")
    up = st.file_uploader("Upload Telenor CDR - .csv / .xlsx", type=["csv","xlsx","xls"], accept_multiple_files=True, key="cdr_telenor")
    if up:
        raws = []
        pars = []
        for f in up:
            disp, par = read_cdr_telenor_file(f)
            raws.append(disp)
            pars.append(par)
        if pars:
            raw_all = pd.concat(pars, ignore_index=True)
            raw_disp = pd.concat(raws, ignore_index=True)
            raw_out, cdr_data, summary, loc_sum, imei_sum, night_sum = build_cdr_telenor_output(raw_all)
            st.success(f"Done! Total {len(cdr_data)} rows | Summary  {len(summary)} unique B numbers")
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                raw_disp.to_excel(writer, index=False, sheet_name="Raw Data")
                cdr_data.to_excel(writer, index=False, sheet_name="CDR Data")
                summary.to_excel(writer, index=False, sheet_name="Summary")
                loc_sum.to_excel(writer, index=False, sheet_name="Location Summary")
                imei_sum.to_excel(writer, index=False, sheet_name="IMEI Summary")
                night_sum.to_excel(writer, index=False, sheet_name="Night Stay")
                blue_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
            st.download_button(label="📥 CDR Telenor Standardized Download the Excel file - 6 Sheets", data=output.getvalue(), file_name="Telenor_CDR_Standardized.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            st.write("**Preview - CDR Data**")
            st.dataframe(cdr_data.head(20))
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("**Summary**")
                st.dataframe(summary)
            with c2:
                st.write("**Location Summary**")
                st.dataframe(loc_sum)
            with c3:
                st.write("**IMEI Summary**")
                st.dataframe(imei_sum)
            st.write("**Night Stay (02:00 - 08:00)**")
            st.dataframe(night_sum)

# ===== oper hath ni lgaya sirf CDR ZONG wala codr paste kia he - CDR ZONG =====

def decode_zong_bparty(v):
    s = str(v).strip()
    if s == "" or s.lower() == "nan":
        return ""
    # International - 00 se shuru - waisa hi
    if s.startswith("00"):
        return s
    # Hex decode - jaise 656173797061697361 -> easypaisa
    try:
        if len(s) % 2 == 0 and len(s) >= 4 and all(c in "0123456789ABCDEFabcdef" for c in s):
            b = bytes([int(s[i:i+2], 16) for i in range(0, len(s), 2)])
            txt = b.decode("ascii", errors="strict")
            if all(32 <= ord(ch) <= 126 for ch in txt) and any(ch.isalpha() for ch in txt):
                return txt.strip()
    except:
        pass
    # Chhota code - 6 ya us se kam digit - 0 samet waisa hi - 08558, 0347, 911
    if len(s) <= 6:
        return s
    # Asal mobile - 11 digit aur 0 se shuru - 0 hatao - 03115191560 -> 3115191560
    if len(s) == 11 and s.startswith("0"):
        return s[1:]
    # 92 wala - 923185040750 -> 3185040750
    if s.startswith("+92"):
        return s[3:]
    if s.startswith("92") and len(s) == 12:
        return s[2:]
    # Baaki sab waisa hi - lambi codes, landline, 00 wala
    return s

def parse_zong_cdr_date(x):
    s = str(x).strip()
    for fmt in ("%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M", "%d/%m/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return pd.to_datetime(s, format=fmt)
        except:
            continue
    return pd.to_datetime(s, errors="coerce")

def read_cdr_zong_file(f):
    f.seek(0)
    tmp = pd.read_excel(f, dtype=str, header=None)
    hidx = None
    for i, row in tmp.iterrows():
        vals = [str(x).strip().upper() for x in row.tolist()]
        if "CALL_TYPE" in vals:
            hidx = i
            break
    if hidx is None:
        hidx = 5
    f.seek(0)
    parsed = pd.read_excel(f, dtype=str, header=hidx)
    return tmp, parsed

def build_cdr_zong_output(raw_df):
    raw = raw_df.copy()
    raw.columns = [str(c).strip() for c in raw.columns]
    cmap = {str(c).strip().upper(): str(c).strip() for c in raw.columns}
    def col(*ns):
        for n in ns:
            if n.upper() in cmap:
                return cmap[n.upper()]
        return None
    cCALL = col("CALL_TYPE", "Call Type")
    cA = col("MSISDN", "A Party", "A")
    cB = col("BNUMBER", "B Party", "B")
    cDT = col("STRT_TM", "Datetime")
    cMINS = col("MINS")
    cSECS = col("SECS")
    cLAC = col("LAC_ID", "LAC")
    cCELL = col("CELL_ID", "CID")
    cIMEI = col("IMEI")
    cSITE = col("SITE_ADDRESS", "Location")
    cLNG = col("LNG")
    cLAT = col("LAT")
    df = pd.DataFrame()
    df["A Party"] = raw[cA].apply(clean_number) if cA else ""
    df["B Party"] = raw[cB].apply(decode_zong_bparty) if cB else ""
    ct = []
    for t in (raw[cCALL].astype(str).str.strip() if cCALL else pd.Series([""]*len(raw))):
        tl = t.strip().lower()
        if tl == "sms - incoming":
            ct.append("ISMS")
        elif tl == "sms - outgoing":
            ct.append("OSMS")
        elif tl == "call - incoming":
            ct.append("IC")
        elif tl == "call - outgoing":
            ct.append("OG")
        else:
            ct.append(t)
    df["Call Type"] = ct
    dt = raw[cDT].apply(parse_zong_cdr_date) if cDT else pd.Series([pd.NaT]*len(raw))
    df["Date"] = dt.dt.strftime("%Y-%m-%d")
    df["Time"] = dt.dt.strftime("%H:%M:%S")
    mins = pd.to_numeric(raw[cMINS], errors="coerce").fillna(0) if cMINS else 0
    secs = pd.to_numeric(raw[cSECS], errors="coerce").fillna(0) if cSECS else 0
    df["Duration"] = (mins*60+secs).astype(int)
    # LAC / CID - as it is - koi formula nahi
    df["LAC"] = raw[cLAC].astype(str).str.strip() if cLAC else ""
    df["CID"] = raw[cCELL].astype(str).str.strip() if cCELL else ""
    df["IMEI"] = raw[cIMEI].astype(str).str.strip() if cIMEI else ""
    df["Location"] = raw[cSITE].astype(str).str.strip() if cSITE else ""
    df["Location"] = df["Location"].replace("nan", "")
    df["LAT"] = raw[cLAT].astype(str).str.strip() if cLAT else ""
    df["LAT"] = df["LAT"].replace("nan", "")
    df["LNG"] = raw[cLNG].astype(str).str.strip() if cLNG else ""
    df["LNG"] = df["LNG"].replace("nan", "")
    df["_dt"] = dt
    df["_dur_min"] = df["Duration"] / 60.0
    cdr_data = df[["Call Type","A Party","B Party","Date","Time","Duration","IMEI","LAC","CID","Location","LAT","LNG"]].copy()
    # Summary - Ufone / Jazz jaisa - DATA nahi, Total Locations nahi
    base = df[df["Call Type"] != "DATA"].copy()
    sr = []
    for (a,b), g in base.groupby(["A Party","B Party"]):
        sr.append({"A": a, "B": b, "IC": int((g["Call Type"]=="IC").sum()), "ISMS": int((g["Call Type"]=="ISMS").sum()), "OG": int((g["Call Type"]=="OG").sum()), "OSMS": int((g["Call Type"]=="OSMS").sum()), "Total": len(g), "IC (Seconds)": round(g.loc[g["Call Type"]=="IC","_dur_min"].sum()*60, 2), "OG (Seconds)": round(g.loc[g["Call Type"]=="OG","_dur_min"].sum()*60, 2), "Total Seconds": round(g["_dur_min"].sum()*60, 2), "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "", "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "", "Total Days": int(g["Date"].nunique())})
    summary = pd.DataFrame(sr).sort_values("Total", ascending=False) if sr else pd.DataFrame(columns=["A","B","IC","ISMS","OG","OSMS","Total","IC (Seconds)","OG (Seconds)","Total Seconds","First Call","Last Call","Total Days"])
    # Location Summary - DATA nahi
    lr = []
    for loc, g in base.groupby("Location"):
        lr.append({"Location": loc, "IC": int((g["Call Type"]=="IC").sum()), "ISMS": int((g["Call Type"]=="ISMS").sum()), "OG": int((g["Call Type"]=="OG").sum()), "OSMS": int((g["Call Type"]=="OSMS").sum()), "Total": len(g), "First Call": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "", "Last Call": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "", "T_Locations": int(g["Location"].nunique()), "T_Days": int(g["Date"].nunique())})
    loc_sum = pd.DataFrame(lr).sort_values("Total", ascending=False) if lr else pd.DataFrame(columns=["Location","IC","ISMS","OG","OSMS","Total","First Call","Last Call","T_Locations","T_Days"])
    # IMEI Summary - Ufone jaisa
    ir = []
    for imei, g in df.groupby("IMEI"):
        nd = g[g["Call Type"] != "DATA"]
        ir.append({"IMEI": imei, "OG": int((g["Call Type"]=="OG").sum()), "ISMS": int((g["Call Type"]=="ISMS").sum()), "IC": int((g["Call Type"]=="IC").sum()), "OSMS": int((g["Call Type"]=="OSMS").sum()), "Total": len(nd), "Total Duration": int(g["Duration"].sum()), "First Use": g["_dt"].min().strftime("%Y-%m-%d") if pd.notna(g["_dt"].min()) else "", "Last Use": g["_dt"].max().strftime("%Y-%m-%d") if pd.notna(g["_dt"].max()) else "", "Days Used": int(g["Date"].nunique())})
    imei_sum = pd.DataFrame(ir).sort_values("Total", ascending=False) if ir else pd.DataFrame(columns=["IMEI","OG","ISMS","IC","OSMS","Total","Total Duration","First Use","Last Use","Days Used"])
    # Night Stay - 2am to 8am
    night = df.copy()
    tt = pd.to_datetime(night["Time"], errors="coerce")
    night["_hour"] = tt.dt.hour + tt.dt.minute/60
    night = night[(night["_hour"] >= 2) & (night["_hour"] < 8)]
    if len(night) > 0:
        nr = []
        for (d, loc, lac, cid), g in night.groupby(["Date","Location","LAC","CID"]):
            nr.append({"Date": d, "Location": loc, "LAC": lac, "CID": cid, "Night Count": len(g), "First Call": g["Time"].min(), "Last Call": g["Time"].max(), "Total Locations": int(g["Location"].nunique())})
        night_sum = pd.DataFrame(nr).sort_values(["Date","Night Count"], ascending=[True, False])
    else:
        night_sum = pd.DataFrame([{"Date": "No record 02:00-08:00", "Location": "", "LAC": "", "CID": "", "Night Count": 0, "First Call": "", "Last Call": "", "Total Locations": 0}])
    return raw, cdr_data, summary, loc_sum, imei_sum, night_sum

# ===== TAB 9 - CDR ZONG =====
if selected_tab == 3 and st.session_state.mode == "CDR":
    st.subheader("CDR - Zong - Standardized")
    st.info("Zong CDR")
    up = st.file_uploader("Upload Zong CDR Raw - .xlsx / .csv", type=["xlsx","xls","csv"], accept_multiple_files=True, key="cdr_zong")
    if up:
        raws = []
        pars = []
        for f in up:
            disp, par = read_cdr_zong_file(f)
            raws.append(disp)
            par.columns = [str(c).strip() for c in par.columns]
            pars.append(par)
        if pars:
            raw_all = pd.concat(pars, ignore_index=True)
            raw_disp = pd.concat(raws, ignore_index=True)
            raw_out, cdr_data, summary, loc_sum, imei_sum, night_sum = build_cdr_zong_output(raw_all)
            st.success(f"Done! Total {len(cdr_data)} rows | Summary  {len(summary)} unique B numbers")
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                raw_disp.to_excel(writer, index=False, sheet_name="Raw Data")
                cdr_data.to_excel(writer, index=False, sheet_name="CDR Data")
                summary.to_excel(writer, index=False, sheet_name="Summary")
                loc_sum.to_excel(writer, index=False, sheet_name="Location Summary")
                imei_sum.to_excel(writer, index=False, sheet_name="IMEI Summary")
                night_sum.to_excel(writer, index=False, sheet_name="Night Stay")
            st.download_button(label="📥 CDR Zong Standardized Download the Excel file - 6 Sheets", data=output.getvalue(), file_name="Zong_CDR_Standardized.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            st.write("**Preview - CDR Data**")
            st.dataframe(cdr_data.head(20))
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("**Summary by Numbers**")
                st.dataframe(summary)
            with c2:
                st.write("**Summary by Location**")
                st.dataframe(loc_sum)
            with c3:
                st.write("**IMEI Summary**")
                st.dataframe(imei_sum)
            st.write("**Night Stay (02:00 - 08:00)**")
            st.dataframe(night_sum)

# ===== TAB 10 - ALL CDR - MASTER FILE - FINAL - THEEK WALA =====

# Sheet 1 - Master File | Sheet 2 - Common A Party | Sheet 3 - Common B Party | Sheet 4 - Common IMEI | Sheet 5 - Common Location
# 12 Columns - Call Type | A Party | B Party | Date | Time | Duration | IMEI | LAC | CID | Location | LAT | LNG
# No NETWORK Column, Sirf CDR Code, BTS Wala Kuch Nahi

if selected_tab == 4 and st.session_state.mode == "CDR":
    st.subheader("📞 ALL CDR - Master File - 5 Sheets")
    st.info("Ufone + Jazz + Telenor + Zong CDR Master File - 5 Sheets in One.")

    all_cdr_files = st.file_uploader("Upload All CDR Files - xlsx / xls / csv", type=["xlsx", "xls", "csv"], accept_multiple_files=True, key="all_cdr_master")

    import re as _re

    # --- A Party / B Party se 92 / 0 utarne wala purana formula ---
    def _clean_num(x):
        s = str(x).strip() if x is not None else ""
        if s.lower() in ["", "nan", "none"]:
            return ""
        if len(s) == 15 and s.isdigit():
            return s
        if len(s) == 14 and s.isdigit():
            return s    
        if any(c.isalpha() for c in s):
            return s
        if s.startswith("0092"):
            s = s[4:]
        elif s.startswith("+92"):
            s = s[3:]
        elif s.startswith("92") and len(s) > 10:
            s = s[2:]
        elif s.startswith("0") and len(s) > 10:
            s = s[1:]
        if s.startswith("640") and len(s) >= 13:
            s = s[3:13]
        elif s.startswith("380") and len(s) >= 13:
            s = s[3:13]
        if s.startswith("2") and len(s) == 11:
            s = s[1:]
        if len(s) > 10:
            mm = _re.search(r"3\d{9}", s)
            if mm:
                s = mm.group(0)
            elif len(s) > 11:
                mm2 = _re.search(r"03\d{9}", s)
                if mm2:
                    s = mm2.group(0)
                else:
                    s = s[-11:]
        return s

    def _make_call_type(raw_type, direction=""):
        t = str(raw_type).strip().lower()
        d = str(direction).strip().lower()
        if "data" in t or "gprs" in t or "data" in d: return "Data"
        if "sms" in t:
            if "incoming" in t or "incomming" in t or d in ["incoming", "incomming"]:
                return "In SMS"
            if "outgoing" in t or "outcomming" in t or "out" in t or "out" in d:
                return "Out SMS"
            return "In SMS"
        if "call" in t or "voice" in t:
            if "incoming" in t or "incomming" in t or d in ["incoming", "incomming"]:
                return "In Call"
            if "outgoing" in t or "outcomming" in t or "out" in t or "out" in d or d in ["outgoing", "outcomming"]:
                return "Out Call"
            return "In Call"
        if t in ["incoming", "incomming", "in"]:
            return "In Call"
        if t in ["outgoing", "outcomming", "out"]:
            return "Out Call"
        if d in ["outgoing", "outcomming", "1"]:
            return "Out Call"
        if d in ["incoming", "incomming", "2"]:
            return "In Call"
        if d in ["internet", "0", "gprs"]:
            return "Data"
        return "In Call"

    def _read_cdr_file(f):
        lname = f.name.lower()
        f.seek(0)
        if lname.endswith(".csv"):
            try:
                df_raw = pd.read_csv(f, dtype=str, header=None, encoding="utf-8")
            except:
                f.seek(0)
                df_raw = pd.read_csv(f, dtype=str, header=None, encoding="latin1")
        elif lname.endswith(".txt"):
            try:
                f.seek(0)
                df_raw = pd.read_csv(f, dtype=str, header=None, encoding="utf-16", sep="\t")
            except:
                f.seek(0)
                df_raw = pd.read_csv(f, dtype=str, header=None, encoding="utf-8", sep="\t", errors="ignore")       
        else:
            try:
                df_raw = pd.read_excel(f, dtype=str, header=None, sheet_name=0)
            except:
                f.seek(0)
                df_raw = pd.read_excel(f, dtype=str, header=None)
        h_row = 0
        for i in range(min(20, len(df_raw))):
            row = " ".join([str(x).lower() for x in df_raw.iloc[i].values])
            hits = sum([1 for kw in ["call_type", "calltype", "msisdn", "strt_tm", "bnumber", "aparty", "bparty", "a number", "call_org_num"] if kw in row])
            if hits >= 2:
                h_row = i
                break
        df = df_raw.iloc[h_row:].copy()
        df.columns = [str(x).strip() for x in df.iloc[0].values]
        df = df[1:].reset_index(drop=True)
        df = df.dropna(how="all")
        return df

    def _detect_cdr_network(df, filename):
        name = filename.lower()
        if "_ufone" in name or "ufone" in name:
            return "UFONE"
        if "_zong" in name or "zong" in name:
            return "ZONG"
        if "_jazz" in name or "jazz" in name or "mobilink" in name:
            return "JAZZ"
        if "_telenor" in name or "telenor" in name:
            return "TELENOR"
        cols = [str(c).strip().lower() for c in df.columns]
        colset = set(cols)
        if "strt_tm" in colset and "bnumber" in colset:
            return "ZONG"
        if "aparty" in colset and "sitelocation" in colset:
            return "JAZZ"
        if "a number" in colset and "cell sector" in colset:
            return "UFONE"
        if "msisdn" in colset and "start time" in colset:
            return "UFONE"    
        if "call_dialed_num" in colset and "call_start_dt_tm" in colset:
            return "TELENOR"
        if "sitelocation" in colset or "longitude and latitude" in colset:
            return "JAZZ"
        if "call_type" in colset and "msisdn" in colset:
            return "ZONG"
        if "call_org_num" in colset:
            return "TELENOR"
        return "UNKNOWN"

    # ---------- ZONG CDR ----------
    def _parse_zong_cdr(df):
        dt = pd.to_datetime(df["STRT_TM"], format="%m/%d/%Y %H:%M:%S", errors="coerce")
        dt = dt.fillna(pd.to_datetime(df["STRT_TM"], errors="coerce", dayfirst=True))
        out = pd.DataFrame()
        out["Call Type"] = df["CALL_TYPE"].apply(lambda x: _make_call_type(x))
        out["A Party"] = df["MSISDN"].apply(_clean_num)
        out["B Party"] = df["BNUMBER"].apply(_clean_num)
        out["Date"] = dt.dt.strftime("%d-%m-%y")
        out["Time"] = dt.dt.strftime("%H:%M:%S")
        mins = pd.to_numeric(df["MINS"], errors="coerce").fillna(0)
        secs = pd.to_numeric(df["SECS"], errors="coerce").fillna(0)
        out["Duration"] = (mins * 60 + secs).astype(int)
        out["IMEI"] = df["IMEI"].apply(_clean_num) if "IMEI" in df.columns else ""
        out["LAC"] = df["LAC_ID"].apply(_clean_num) if "LAC_ID" in df.columns else ""
        out["CID"] = df["CELL_ID"].apply(_clean_num) if "CELL_ID" in df.columns else ""
        out["Location"] = df["SITE_ADDRESS"].apply(_clean_num) if "SITE_ADDRESS" in df.columns else ""
        out["LAT"] = df["LAT"].apply(_clean_num) if "LAT" in df.columns else ""
        out["LNG"] = df["LNG"].apply(_clean_num) if "LNG" in df.columns else ""
        return out
    
    #--------def_jazz_hex------
    def _jazz_hex_all_cdr(v):
        s = str(v).strip().upper()
        if not s or s == "NAN":
            return "", ""
        lac_hex = s[:4][::-1]
        cell_hex = s[4:8][::-1]
        try:
            lac = int(lac_hex, 16)
        except:
            lac = ""
        try:
            cellid = int(cell_hex, 16)
        except:
            cellid = ""
        return lac, cellid
    # ---------- JAZZ CDR ----------
    def _jazz_call_type(v):
        s = str(v).strip().upper()
        if "SMS" in s:
            if "OUT" in s:
                return "Out SMS"
            if "IN" in s:
                return "In SMS"
            return "SMS"
        if "OUT" in s:
            return "Out Call"
        if "IN" in s:
            return "In Call"
        return s.title()
    def _parse_jazz_cdr(df):
        dt = pd.to_datetime(df["Datetime"], errors="coerce")
        out = pd.DataFrame()
        out["Call Type"] = df["CallType"].apply(lambda x: _make_call_type(x))
        out["A Party"] = df["Aparty"].apply(_clean_num)
        out["B Party"] = df["BParty"].apply(_clean_num)
        out["Date"] = dt.dt.strftime("%d-%m-%y")
        out["Time"] = dt.dt.strftime("%H:%M:%S")
        out["Duration"] = pd.to_numeric(df["Duration"], errors="coerce").fillna(0).astype(int)
        out["IMEI"] = df["Imei"].apply(_clean_num) if "Imei" in df.columns else ""
        _lac_cid = [_jazz_hex_all_cdr(v) for v in df["cellid"]] if "cellid" in df.columns else [("", "")] * len(df)
        out["LAC"] = [x[0] for x in _lac_cid]
        out["CID"] = [x[1] for x in _lac_cid]
        locs, lats, lngs = [], [], []
        for v in df["SiteLocation"].astype(str):
            parts = [p.strip() for p in v.split("|")]
            if len(parts) >= 3:
                locs.append(parts[0])
                lats.append(parts[1])
                lngs.append(parts[2])
            elif len(parts) == 2:
                locs.append(parts[0])
                lats.append(parts[1])
                lngs.append("")
            else:
                locs.append(v.strip())
                lats.append("")
                lngs.append("")
        out["Location"] = locs
        out["LAT"] = lats
        out["LNG"] = lngs
        return out
    def _ufone_call_type(t, d):
        t = str(t).strip().upper()
        d = str(d).strip().upper()
        suf = "out" if "OUT" in d else "in" if "IN" in d else ""
        if "DATA" in t or "INTERNET" in t or "GPRS" in t:
            return ("Data " + suf).strip()
        if "SMS" in t:
            return ("SMS " + suf).strip()
        if "VOICE" in t or "CALL" in t or "MOC" in t or "MTC" in t:
            return ("Call " + suf).strip()
        return (t.title() + " " + suf).strip()
    def _ufone_split_cellid(v):
        s = str(v).strip()
        if not s or s == "NAN":
            return "", ""
        s = s.split(".")[0]
        n = len(s)
        half = n // 2
        return s[:half], s[half:]
    # ---------- UFONE CDR ----------
    def _parse_ufone_cdr(df):
        _dt_col = next((c for c in ["Start Time", "StartTime", "Date Time", "Datetime", "Call Time", "Date"] if c in df.columns), None)
        dt = pd.to_datetime(df[_dt_col], errors="coerce", dayfirst=True, format="mixed") if _dt_col is not None else pd.Series(pd.NaT, index=df.index)
        out = pd.DataFrame()
        type_col = next((c for c in df.columns if "TYPE" in str(c).upper()), df.columns[3])
        dir_col = next((c for c in df.columns if "INBOUND" in str(c).upper() or "OUTBOUND" in str(c).upper() or "DIRECTION" in str(c).upper()), df.columns[12])
        out["Call Type"] = [_make_call_type(str(t).lower(), str(d).lower()) for t, d in zip(df[type_col].astype(str), df[dir_col].astype(str))]
        out["A Party"] = df["A Number"].apply(_clean_num)
        out["B Party"] = df["B Number"].apply(_clean_num)
        out["Date"] = dt.dt.strftime("%d-%m-%y")
        out["Time"] = dt.dt.strftime("%H:%M:%S")
        out["Duration"] = pd.to_numeric(df["Duration"], errors="coerce").fillna(0).astype(int)
        out["IMEI"] = df["IMEI"].apply(_clean_num) if "IMEI" in df.columns else ""
        _lac_cid = [_ufone_split_cellid(v) for v in df["Cell Id"]] if "Cell Id" in df.columns else [("", "")] * len(df)
        out["LAC"] = [x[0] for x in _lac_cid]
        out["CID"] = [x[1] for x in _lac_cid]
        out["Location"] = df["Location"] if "Location" in df.columns else ""
        out["LAT"] = df["Latitude"].apply(_clean_num) if "Latitude" in df.columns else ""
        out["LNG"] = df["Longitude"].apply(_clean_num) if "Longitude" in df.columns else ""
        return out

    # ---------- TELENOR CDR ----------
    def _parse_telenor_cdr(df):
        dt = pd.to_datetime(df["CALL_START_DT_TM"].astype(str).str.strip(), errors="coerce", dayfirst=True, format="mixed")
        out = pd.DataFrame()
        ctypes = []
        for ind, ct in zip(df["INBOUND_OUTBOUND_IND"].astype(str), df["CALL_TYPE"].astype(str) if "CALL_TYPE" in df.columns else ["CALL"]*len(df)):
            ctypes.append(_make_call_type(ct, ind))
        out["Call Type"] = ctypes
        out["A Party"] = df["MSISDN"].apply(_clean_num)
        b_list = []
        for d, o in zip(df["CALL_DIALED_NUM"].astype(str) if "CALL_DIALED_NUM" in df.columns else [""]*len(df), df["call_org_num"].astype(str) if "call_org_num" in df.columns else [""]*len(df)):
            b_list.append(_clean_num(d) if _clean_num(d) != "" else _clean_num(o))
        out["B Party"] = b_list
        out["Date"] = dt.dt.strftime("%d-%m-%y")
        out["Time"] = dt.dt.strftime("%H:%M:%S")
        out["Duration"] = pd.to_numeric(df["Call_Network_Volume"], errors="coerce").fillna(0).astype(int)
        out["IMEI"] = df["IMEI"].apply(_clean_num) if "IMEI" in df.columns else ""
        out["LAC"] = df["Lac_Id"].apply(_clean_num) if "Lac_Id" in df.columns else ""
        out["CID"] = df["Site_Id"].apply(_clean_num) if "Site_Id" in df.columns else ""
        out["Location"] = df["location"].apply(_clean_num) if "location" in df.columns else ""
        out["LAT"] = df["lat"].apply(_clean_num) if "lat" in df.columns else ""
        out["LNG"] = df["longitude"].apply(_clean_num) if "longitude" in df.columns else ""
        return out

    if all_cdr_files:
        all_final = []
        for f in all_cdr_files:
            try:
                df_raw = _read_cdr_file(f)
                net = _detect_cdr_network(df_raw, f.name)
                if net == "ZONG":
                    clean = _parse_zong_cdr(df_raw)
                elif net == "JAZZ":
                    clean = _parse_jazz_cdr(df_raw)
                elif net == "UFONE":
                    clean = _parse_ufone_cdr(df_raw)
                elif net == "TELENOR":
                    clean = _parse_telenor_cdr(df_raw)
                else:
                    st.warning(f"{f.name} - Network nahi pehchana gaya, skip kar diya")
                    continue
                clean = clean[["Call Type", "A Party", "B Party", "Date", "Time", "Duration", "IMEI", "LAC", "CID", "Location", "LAT", "LNG"]]
                # Common ke liye andar hi andar file ka naam - Master Sheet me nahi jayega
                clean["_File"] = f.name
                clean["_Net"] = net
                all_final.append(clean)
                # Start-End Date nikalna
                try:
                    _clean_date = clean["Date"].astype(str).str.strip().str.replace(r'[./]', '-', regex=True)
                    if str(net).upper() in ["ZONG", "JAZZ"]:
                        _dates = pd.to_datetime(_clean_date, errors="coerce", format="%m-%d-%y").dropna()
                    else:
                        _dates = pd.to_datetime(_clean_date, errors="coerce", format="%d-%m-%y").dropna()
                    _s = _dates.min().strftime("%m-%d-%Y") if len(_dates) else "?"
                    _e = _dates.max().strftime("%m-%d-%Y") if len(_dates) else "?"
                except:
                    _s = _e = "?"
                st.success(f"✅ {f.name} -> {net} - {len(clean)} rows | {_s} to {_e}")
            except Exception as e:
                st.error(f"❌ {f.name} me masla: {e}")

        if all_final:
            full = pd.concat(all_final, ignore_index=True)
            full = full[full["A Party"].astype(str).str.strip() != ""]
            master = full.drop(columns=["_File", "_Net"])

            st.success(f"🎯 Master File Ready: {len(master)} rows - 5 Sheets")
            # --- Operator Summary Table ---
            _net_counts = full.drop_duplicates(subset=["_File"])["_Net"].value_counts()
            _zong = int(_net_counts.get("ZONG", 0))
            _ufone = int(_net_counts.get("UFONE", 0))
            _telenor = int(_net_counts.get("TELENOR", 0))
            _jazz = int(_net_counts.get("JAZZ", 0))
            _total = _zong + _ufone + _telenor + _jazz
            st.html(f"""
    <style>
            .op-table {{ width:100%; border-collapse:separate; border-spacing:0; overflow:hidden; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); }}
            .op-table th {{ background:linear-gradient(90deg,#0f2027,#203a43,#2c5364); color:white; padding:14px; text-align:center; font-size:18px; }}
            .op-table td {{ padding:13px 14px; font-size:16px; font-weight:600; border-bottom:1px solid #eee; }}
            .op-table tr:last-child td {{ border-bottom:none; }}
            .badge {{ padding:6px 14px; border-radius:20px; color:white; font-size:14px; }}
    </style>
            <table class="op-table">
              <tr><th>Network</th><th style="text-align:center;">Total CDRs</th></tr>
              <tr><td>🟢 <span class="badge" style="background:#00a651;">ZONG</span> &nbsp; Zong Total CDRs</td><td style="text-align:center;">{_zong:,}</td></tr>
              <tr style="background:#f8f9fa;"><td>🟠 <span class="badge" style="background:#ff6600;">UFONE</span> &nbsp; Ufone Total CDRs</td><td style="text-align:center;">{_ufone:,}</td></tr>
              <tr><td>🔵 <span class="badge" style="background:#0070d1;">TELENOR</span> &nbsp; Telenor Total CDRs</td><td style="text-align:center;">{_telenor:,}</td></tr>
              <tr style="background:#f8f9fa;"><td>🔴 <span class="badge" style="background:#e30613;">JAZZ</span> &nbsp; Jazz Total CDRs</td><td style="text-align:center;">{_jazz:,}</td></tr>
              <tr style="background:#eef2f7;"><td><b>⭐ TOTAL</b></td><td style="text-align:center;"><b>{_total:,}</b></td></tr>
    </table>
    """)

            # ---------- Sheet 2 - Common A Party ----------
            g_a = full.groupby("A Party").agg(
                Total_Calls=("A Party", "count"),
                Alag_Files=("_File", "nunique"),
                Alag_B_Party=("B Party", "nunique"),
                Files=("_File", lambda x: ", ".join(sorted(set(x.astype(str)))[:5])),
                Networks=("_Net", lambda x: ", ".join(sorted(set(x.astype(str))))),
                First_Date=("Date", "min"),
                Laste_Date=("Date", "max"),
                Total_Duration=("Duration", "sum")
            ).reset_index()
            all_b_set = set(full["B Party"].dropna().astype(str).str.strip())
            common_a = g_a[g_a["A Party"].astype(str).str.strip().isin(all_b_set)].sort_values("Total_Calls", ascending=False)
            # Interlink - A_As_B_Party 
            common_a["Common A Party (intralink)"] = common_a["A Party"].apply(lambda a_num: ", ".join(sorted(set(full[full["A Party"].astype(str).str.replace(" ", "").str[-10:] == str(a_num).replace(" ", "")[-10:]]["B Party"].astype(str).str.replace(" ", "").str[-10:]) & set(full["A Party"].astype(str).str.replace(" ", "").str[-10:]) - {str(a_num).replace(" ", "")[-10:]})))
            df_b = full[full["B Party"].astype(str).str.strip() != ""]; g_b = df_b.groupby("B Party").agg(Total_Calls=("B Party", "count"), Alag_A_Party=("A Party", "nunique"), Alag_Files=("_File", "nunique"), A_Party_List=("A Party", lambda x: ", ".join(sorted(set(x.astype(str)))[:6])), Files=("_File", lambda x: ", ".join(sorted(set(x.astype(str)))[:5])), Networks=("_Net", lambda x: ", ".join(sorted(set(x.astype(str))))), Pehli_Date=("Date", "min"), Aakhri_Date=("Date", "max"), Total_Duration=("Duration", "sum")).reset_index(); common_b = g_b[(g_b["Alag_A_Party"] >= 2) | (g_b["Alag_Files"] >= 2)].sort_values("Total_Calls", ascending=False)
            # ---------- Sheet 4 - Common IMEI ----------
            df_i = full[full["IMEI"].astype(str).str.strip() != ""]
            g_i = df_i.groupby("IMEI").agg(
                Total_Calls=("IMEI", "count"),
                Total_Distinct_A_Parties=("A Party", "nunique"),
                Total_A_Parties=("_File", "nunique"),
                A_Party_List=("A Party", lambda x: ", ".join(sorted(set(x.astype(str)))[:6])),
                Files=("_File", lambda x: ", ".join(sorted(set(x.astype(str)))[:5])),
                Networks=("_Net", lambda x: ", ".join(sorted(set(x.astype(str))))),
                First_Date=("Date", "min"),
                Last_Date=("Date", "max")
            ).reset_index()
            common_i = g_i[g_i["Total_Distinct_A_Parties"] >= 2].sort_values("Total_Calls", ascending=False)

            # ---------- Sheet 5 - Common Location - Same LAT+LNG + Same Date ----------
            df_l = full[(full["LAT"].astype(str).str.strip() != "") & (full["LNG"].astype(str).str.strip() != "")].copy()
            df_l["LAT_R"] = pd.to_numeric(df_l["LAT"], errors="coerce").round(4)
            df_l["LNG_R"] = pd.to_numeric(df_l["LNG"], errors="coerce").round(4)
            df_l = df_l.dropna(subset=["LAT_R", "LNG_R"])
            g_l = df_l.groupby(["LAT_R", "LNG_R", "Date"]).agg(
                Total_Calls=("LAT_R", "count"),
                Alag_A_Party=("A Party", "nunique"),
                A_Party_List=("A Party", lambda x: ", ".join(sorted(set(x.astype(str)))[:6])),
                Location=("Location", "first"),
                LAT=("LAT", "first"),
                LNG=("LNG", "first"),
                First_Time=("Time", "min"),
                Last_Time=("Time", "max")
            ).reset_index()
            common_l = g_l[g_l["Alag_A_Party"] >= 2].sort_values("Total_Calls", ascending=False)
            common_l = common_l[["Date", "Location", "LAT", "LNG", "Alag_A_Party", "A_Party_List", "Total_Calls", "First_Time", "Last_Time"]]

            # Screen pe 5ro ka chhota hisaab dikhao
            st.write(f"**Sheet 1 - Master File:** {len(master)} rows")
            st.write(f"**Sheet 2 - Common A Party:** {len(common_a)}")
            st.write(f"**Sheet 3 - Common B Party:** {len(common_b)}")
            st.write(f"**Sheet 4 - Common IMEI:** {len(common_i)}")
            st.write(f"**Sheet 5 - Common Location:** {len(common_l)} - Same Jagah + Same Date pe 2+ bande")
            st.dataframe(master.head(10), use_container_width=True)
            st.dataframe(common_l.head(10), use_container_width=True)

            # ---------- Download - 5 Sheets ----------
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                master.to_excel(writer, index=False, sheet_name="Master File")
                common_a.to_excel(writer, index=False, sheet_name="Common A Party")
                common_b.to_excel(writer, index=False, sheet_name="Common B Party")
                common_i.to_excel(writer, index=False, sheet_name="Common IMEI")
                common_l.to_excel(writer, index=False, sheet_name="Common Location")
                blue_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
            st.download_button("📥 Master File Download Karo - 5 Sheets", data=output.getvalue(), file_name="Master_File_All_CDR.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
