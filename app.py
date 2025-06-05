
import streamlit as st
from pathlib import Path

# Set page config
st.set_page_config(page_title="ACCLOGIX MyHR Portal", layout="centered")

# --- Dummy authentication ---
def login(email, password):
    return email == "prakash@acclogix.com" and password == "welcome123"

# --- Main App ---
def main():
    st.title("ACCLOGIX BUSINESS SERVICES PVT LTD – MyHR Portal")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(email, password):
                st.session_state.logged_in = True
                st.success("Login successful!")
            else:
                st.error("Invalid credentials. Try again.")
    else:
        st.subheader("Welcome, Prakash V")
        st.markdown("**Designation:** Associate Officer")
        st.markdown("**Employee ID:** ACC008")
        st.markdown("---")
        st.markdown("### 📄 My Documents")

        hike_letter_path = Path("static/documents/Prakash_Hike_Letter.pdf")
        payslip_path = Path("static/documents/Payslip_Apr_2025.pdf")

        with open(hike_letter_path, "rb") as f:
            st.download_button("Download Hike Letter (28-May-2025)", f, file_name=hike_letter_path.name)

        with open(payslip_path, "rb") as f:
            st.download_button("Download Payslip (April 2025)", f, file_name=payslip_path.name)

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
