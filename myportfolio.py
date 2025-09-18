import streamlit as st
import os
import base64

st.set_page_config(page_title="Obed Feni - Portfolio", page_icon="📄", layout="wide")

# Hide Streamlit menu & footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Functions
def list_files(category):
    folder = f"documents/{category}"
    if not os.path.exists(folder):
        return []
    return [os.path.join(folder, f) for f in os.listdir(folder)]

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def create_download_button(file_path, button_text):
    with open(file_path, "rb") as file:
        st.download_button(
            label=button_text,
            data=file,
            file_name=os.path.basename(file_path),
            mime="application/octet-stream"
        )

# Custom styling
st.markdown("""
<style>
    .main {
        background-color: #f0f6ff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2c3e50;
    }
    .header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    .header h1 {
        color: #1e3d7b;
        font-size: 2.5rem;
    }
    .header p {
        color: #4a6572;
        font-size: 1.1rem;
    }
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
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: #1e3d7b;
        color: white;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">', unsafe_allow_html=True)
st.title("Obed Tenkorang Feni")
st.markdown("<p>Welcome to my professional portfolio. Explore my certificates, testimonials, and achievements.</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Certificates Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📜 Certificates")
cert_files = list_files("certificates")
if not cert_files:
    st.info("No certificates available yet.")
else:
    for file in cert_files:
        filename = os.path.basename(file)
        st.subheader(filename)
        if file.endswith(".pdf"):
            show_pdf(file)
        elif file.endswith((".png", ".jpg", ".jpeg")):
            st.image(file, use_container_width=True)
        create_download_button(file, f"⬇️ Download {filename}")
st.markdown('</div>', unsafe_allow_html=True)

# Testimonials Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🌟 Testimonials")
test_files = list_files("testimonials")
if not test_files:
    st.info("No testimonials available yet.")
else:
    for file in test_files:
        filename = os.path.basename(file)
        st.subheader(filename)
        if file.endswith(".pdf"):
            show_pdf(file)
        elif file.endswith((".png", ".jpg", ".jpeg")):
            st.image(file, use_container_width=True)
        create_download_button(file, f"⬇️ Download {filename}")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📞 Contact Information")
st.markdown("""
- **Email:** obedfeni23@gmail.com  
- **Phone:** +233541468102  
- **LinkedIn:** [linkedin.com/in/obedfeni](https://linkedin.com/in/obedfeni)  
- **GitHub:** [github.com/obed_feni](https://github.com/obed_feni)  
""")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("© 2025 Obed Feni — Professional Portfolio. All rights reserved.")
st.markdown('</div>', unsafe_allow_html=True)
