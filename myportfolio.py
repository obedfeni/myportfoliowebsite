import streamlit as st
import base64
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="My Professional Portfolio",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for blue & white professional theme
st.markdown("""
<style>
    /* Global page style */
    .main {
        padding: 2rem;
        background: linear-gradient(135deg, #f0f7ff, #e6f0fa);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2c3e50;
    }

    /* Header */
    .header {
        text-align: center;
        padding: 2rem 0;
        border-bottom: 2px solid #e6eef5;
        margin-bottom: 2rem;
    }
    .header h1 {
        color: #1e3d7b;
        font-size: 2.8rem;
        margin-bottom: 0.3rem;
    }
    .header p {
        color: #4a6572;
        font-size: 1.1rem;
    }

    /* Section styling */
    .section {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .section h2 {
        color: #1e3d7b;
        border-left: 4px solid #1e90ff;
        padding-left: 0.6rem;
        margin-bottom: 1rem;
    }

    /* Cards */
    .card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }

    /* Buttons */
    .stDownloadButton button {
        width: 100%;
        background-color: #1e90ff !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px !important;
        padding: 0.6rem;
        transition: background-color 0.2s ease;
    }
    .stDownloadButton button:hover {
        background-color: #155d9c !important;
    }

    /* Links */
    a {
        color: #1e90ff;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: #1e3d7b;
        color: white;
        font-size: 0.9rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- Initialize session state ----------
if 'certificates' not in st.session_state:
    st.session_state.certificates = []
if 'testimonials' not in st.session_state:
    st.session_state.testimonials = []

# ---------- Functions ----------
def save_uploaded_file(uploaded_file, category, title):
    os.makedirs(f"documents/{category}", exist_ok=True)
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    file_extension = os.path.splitext(uploaded_file.name)[1]
    file_path = f"documents/{category}/{safe_title}{file_extension}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def create_download_button(file_path, button_text):
    with open(file_path, "rb") as file:
        st.download_button(
            label=button_text,
            data=file,
            file_name=os.path.basename(file_path),
            mime="application/octet-stream"
        )

# ---------- Header ----------
st.markdown('<div class="header">', unsafe_allow_html=True)
st.title("Obed Tenkorang Feni")
st.markdown("<p>Welcome to my professional portfolio. Explore my certificates, testimonials, and achievements.</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Sidebar Upload ----------
with st.sidebar:
    st.header("📤 Upload Documents")
    with st.expander("➕ Add Certificate"):
        with st.form("certificate_form"):
            cert_title = st.text_input("Certificate Title")
            cert_issuer = st.text_input("Issuing Organization")
            cert_date = st.date_input("Issue Date")
            cert_description = st.text_area("Description")
            cert_file = st.file_uploader("Upload Certificate", type=['pdf', 'doc', 'docx', 'png', 'jpg'])
            cert_submitted = st.form_submit_button("Save Certificate")
            if cert_submitted and cert_file and cert_title:
                file_path = save_uploaded_file(cert_file, "certificates", cert_title)
                st.session_state.certificates.append({
                    "title": cert_title,
                    "issuer": cert_issuer,
                    "date": cert_date.strftime("%Y-%m-%d"),
                    "description": cert_description,
                    "file_path": file_path
                })
                st.success("✅ Certificate added successfully!")

    with st.expander("➕ Add Testimonial"):
        with st.form("testimonial_form"):
            testimonial_name = st.text_input("Person's Name")
            testimonial_position = st.text_input("Position")
            testimonial_text = st.text_area("Testimonial Content")
            testimonial_date = st.date_input("Date Received")
            testimonial_file = st.file_uploader("Upload Document (optional)", type=['pdf', 'doc', 'docx', 'png', 'jpg'])
            testimonial_submitted = st.form_submit_button("Save Testimonial")
            if testimonial_submitted and testimonial_text:
                file_path = save_uploaded_file(testimonial_file, "testimonials", testimonial_name) if testimonial_file else None
                st.session_state.testimonials.append({
                    "name": testimonial_name,
                    "position": testimonial_position,
                    "text": testimonial_text,
                    "date": testimonial_date.strftime("%Y-%m-%d"),
                    "file_path": file_path
                })
                st.success("🌟 Testimonial added successfully!")

# ---------- Certificates Section ----------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📜 Certificates")
if not st.session_state.certificates:
    st.info("No certificates added yet. Use the sidebar to upload.")
else:
    for cert in st.session_state.certificates:
        with st.expander(f"{cert['title']} - {cert['issuer']} ({cert['date']})"):
            st.write(cert['description'])
            if cert['file_path'].endswith('.pdf'):
                show_pdf(cert['file_path'])
            elif cert['file_path'].endswith(('.png', '.jpg', '.jpeg')):
                st.image(cert['file_path'])
            create_download_button(cert['file_path'], f"⬇️ Download {cert['title']}")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Testimonials Section ----------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🌟 Testimonials")
if not st.session_state.testimonials:
    st.info("No testimonials added yet. Use the sidebar to upload.")
else:
    for testimonial in st.session_state.testimonials:
        st.markdown(f"""
        <div class="card">
            <p>“{testimonial['text']}”</p>
            <p><strong>{testimonial['name']}</strong><br>
            <em>{testimonial['position']}</em> — {testimonial['date']}</p>
        </div>
        """, unsafe_allow_html=True)
        if testimonial['file_path']:
            create_download_button(testimonial['file_path'], f"⬇️ Download {testimonial['name']}'s Testimonial")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Contact Section ----------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📞 Contact Information")
st.markdown("""
- **Email:** obedfeni@gmail.com  
- **Phone:** +233541468102  
- **LinkedIn:** [linkedin.com/in/obedfeni](https://linkedin.com/in/obedfeni)  
- **GitHub:** [github.com/obed_feni](https://github.com/obed_feni)  
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("© 2025 Obed Feni — Professional Portfolio. All rights reserved.")
st.markdown('</div>', unsafe_allow_html=True)
