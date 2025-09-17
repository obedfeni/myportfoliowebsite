import streamlit as st
import base64
import os

# Page config (hide menu & footer)
st.set_page_config(page_title="Obed Feni | Portfolio", page_icon="📄", layout="wide")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Background & theme
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #e8f0ff, #ffffff);
        padding: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2c3e50;
    }
    .section {
        background-color: #ffffffcc;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }
    .section h2 {
        color: #1e3d7b;
        border-left: 4px solid #1e90ff;
        padding-left: 0.6rem;
        margin-bottom: 1rem;
    }
    .card {
        background: #f9fbff;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 3px 12px rgba(0,0,0,0.06);
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        background-color: #1e3d7b;
        color: white;
        padding: 1rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Functions
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

# Header
st.markdown('<div class="section">', unsafe_allow_html=True)
st.title("Obed Tenkorang Feni")
st.markdown("### 📂 Professional Portfolio")
st.markdown("Welcome to my portfolio. Browse my certificates, testimonials, and professional achievements below.")
st.markdown('</div>', unsafe_allow_html=True)

# Certificates
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📜 Certificates")
cert_folder = "documents/certificates"
if not os.path.exists(cert_folder) or not os.listdir(cert_folder):
    st.info("No certificates uploaded yet.")
else:
    for file in os.listdir(cert_folder):
        path = os.path.join(cert_folder, file)
        with st.expander(file.replace("_", " ").title()):
            if file.endswith(".pdf"):
                show_pdf(path)
            elif file.endswith((".png", ".jpg", ".jpeg")):
                st.image(path)
            create_download_button(path, f"⬇️ Download {file}")
st.markdown('</div>', unsafe_allow_html=True)

# Testimonials
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🌟 Testimonials")
test_folder = "documents/testimonials"
if not os.path.exists(test_folder) or not os.listdir(test_folder):
    st.info("No testimonials uploaded yet.")
else:
    for file in os.listdir(test_folder):
        path = os.path.join(test_folder, file)
        st.markdown(f"""
        <div class="card">
            <p><strong>{file.replace("_", " ").title()}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        create_download_button(path, f"⬇️ Download {file}")
st.markdown('</div>', unsafe_allow_html=True)

# Contact
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
st.markdown('<div class="footer">© 2025 Obed Feni — Professional Portfolio</div>', unsafe_allow_html=True)
