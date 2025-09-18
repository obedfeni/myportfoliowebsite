import streamlit as st
import os

st.set_page_config(page_title="Admin Dashboard", page_icon="⚙️", layout="wide")

# Hide Streamlit menu
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Functions
def save_uploaded_file(uploaded_file, category, title):
    os.makedirs(f"documents/{category}", exist_ok=True)
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    file_extension = os.path.splitext(uploaded_file.name)[1]
    file_path = f"documents/{category}/{safe_title}{file_extension}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Header
st.title("⚙️ Admin Dashboard")
st.markdown("Upload and manage your certificates and testimonials.")

# Upload Certificate Form
with st.expander("➕ Add Certificate"):
    with st.form("certificate_form", clear_on_submit=True):
        cert_title = st.text_input("Certificate Title")
        cert_file = st.file_uploader("Upload Certificate", type=['pdf', 'png', 'jpg', 'jpeg', 'docx'])
        cert_submit = st.form_submit_button("Save Certificate")
        if cert_submit and cert_file and cert_title:
            save_uploaded_file(cert_file, "certificates", cert_title)
            st.success(f"✅ {cert_title} added successfully!")

# Upload Testimonial Form
with st.expander("➕ Add Testimonial"):
    with st.form("testimonial_form", clear_on_submit=True):
        test_title = st.text_input("Testimonial Name/Source")
        test_file = st.file_uploader("Upload Testimonial", type=['pdf', 'png', 'jpg', 'jpeg', 'docx'])
        test_submit = st.form_submit_button("Save Testimonial")
        if test_submit and test_file and test_title:
            save_uploaded_file(test_file, "testimonials", test_title)
            st.success(f"🌟 {test_title} added successfully!")

st.info("Uploaded files are instantly available on your public portfolio page.")
