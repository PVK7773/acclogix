
import streamlit as st
from pathlib import Path

# --- Config ---
st.set_page_config(page_title="ACCLOGIX MyHR Portal", layout="wide")

# --- Constants ---
LOGO_PATH = "static/company_logo.png"
HIKE_LETTER_PATH = "static/documents/Prakash_Hike_Letter.pdf"
PAYSLIP_PATH = "static/documents/Payslip_Apr_2025.pdf"
PENDING_PAYS = ["March 2025", "February 2025"]

# --- Sidebar Navigation ---
st.sidebar.image(LOGO_PATH, width=120)
st.sidebar.title("ACCLOGIX MyHR")
menu = st.sidebar.radio("Navigate", ["Dashboard", "My Documents", "Leave Application", "Payslip History", "Admin Panel", "Announcements"])

# --- Dummy Auth ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login_form():
    st.title("ACCLOGIX BUSINESS SERVICES PVT LTD – MyHR Portal")
    st.subheader("Employee Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email == "prakash@acclogix.com" and password == "welcome123":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

def dashboard():
    st.title("Employee Dashboard")
    st.markdown("### Welcome, Prakash V")
    st.markdown("**Designation:** Associate Officer")
    st.markdown("**Employee ID:** ACC008")
    st.markdown("**Joining Date:** 01-Apr-2019")
    st.markdown("**Current CTC:** ₹98,200")
    st.success("No pending HR actions at this time.")

def my_documents():
    st.title("📄 My Documents")
    with open(HIKE_LETTER_PATH, "rb") as f:
        st.download_button("Download Hike Letter (28-May-2025)", f, file_name="Prakash_Hike_Letter.pdf")

    with open(PAYSLIP_PATH, "rb") as f:
        st.download_button("Download Payslip (April 2025)", f, file_name="Payslip_Apr_2025.pdf")

def leave_application():
    st.title("📝 Leave Application Form")
    name = st.text_input("Employee Name", value="Prakash V")
    leave_type = st.selectbox("Leave Type", ["Casual Leave", "Sick Leave", "Earned Leave"])
    from_date = st.date_input("From Date")
    to_date = st.date_input("To Date")
    reason = st.text_area("Reason for Leave")
    if st.button("Submit Leave Request"):
        st.success("Leave request submitted successfully!")

def payslip_history():
    st.title("📊 Payslip History")
    st.markdown("Select any previous month to download payslips.")
    for month in PENDING_PAYS:
        st.download_button(f"Download Payslip - {month}", b"Sample Payslip Content", file_name=f"Payslip_{month.replace(' ', '_')}.pdf")

def admin_panel():
    st.title("🔐 Admin Upload Panel")
    st.markdown("Upload hike letters, payslips, or other documents for employees.")
    uploaded_file = st.file_uploader("Choose a file to upload", type=["pdf"])
    if uploaded_file:
        Path("static/admin_uploads").mkdir(parents=True, exist_ok=True)
        with open(f"static/admin_uploads/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"{uploaded_file.name} uploaded successfully!")

def announcements():
    st.title("📢 Announcements")
    st.info("📌 HR Portal v2.0 launched with new features.")
    st.info("📅 FY25 Leave Quota will reset on July 1st.")
    st.warning("🚨 Please submit June payslip upload requests by June 30th.")

# --- App Flow ---
if not st.session_state.logged_in:
    login_form()
else:
    if menu == "Dashboard":
        dashboard()
    elif menu == "My Documents":
        my_documents()
    elif menu == "Leave Application":
        leave_application()
    elif menu == "Payslip History":
        payslip_history()
    elif menu == "Admin Panel":
        admin_panel()
    elif menu == "Announcements":
        announcements()
