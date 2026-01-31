import streamlit as st
import base64
from pathlib import Path
import os

# Page configuration
st.set_page_config(
    page_title="Feni Obed Tenkorang | Electrical Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for blue and white professional theme
def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        * { font-family: 'Inter', sans-serif; }
        
        .main {
            background: linear-gradient(135deg, #ffffff 0%, #f0f4f8 100%);
        }
        
        .hero-section {
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            padding: 4rem 2rem;
            border-radius: 20px;
            margin-bottom: 3rem;
            color: white;
            text-align: center;
            box-shadow: 0 20px 40px rgba(30, 58, 138, 0.2);
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, #ffffff, #bfdbfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
            font-weight: 300;
            opacity: 0.9;
            margin-bottom: 1rem;
        }
        
        .hero-contact {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
        }
        
        .hero-contact-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1rem;
            opacity: 0.9;
        }
        
        .section-header {
            color: #1e3a8a;
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #3b82f6;
            display: inline-block;
        }
        
        .info-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            border-left: 4px solid #3b82f6;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15);
        }
        
        .card-title {
            color: #1e3a8a;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        .card-subtitle {
            color: #3b82f6;
            font-size: 1rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        
        .card-date {
            color: #6b7280;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .card-description {
            color: #374151;
            line-height: 1.6;
        }
        
        .card-description ul {
            margin: 0;
            padding-left: 1.2rem;
        }
        
        .card-description li {
            margin-bottom: 0.5rem;
        }
        
        .skill-badge {
            display: inline-block;
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            margin: 0.25rem;
            font-size: 0.9rem;
            font-weight: 500;
            box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
        }
        
        .download-btn {
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(30, 58, 138, 0.2);
        }
        
        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(30, 58, 138, 0.3);
        }
        
        .contact-link {
            color: #3b82f6;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }
        
        .contact-link:hover {
            color: #1e3a8a;
        }
        
        .footer {
            text-align: center;
            padding: 2rem;
            color: #6b7280;
            border-top: 1px solid #e5e7eb;
            margin-top: 3rem;
        }
        
        .nav-container {
            background: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            display: flex;
            justify-content: center;
            gap: 2rem;
            position: sticky;
            top: 1rem;
            z-index: 100;
            flex-wrap: wrap;
        }
        
        .nav-link {
            color: #1e3a8a;
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            transition: all 0.3s ease;
        }
        
        .nav-link:hover {
            background: #eff6ff;
            color: #3b82f6;
        }
        
        .cert-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            border-top: 3px solid #3b82f6;
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .cert-card:hover {
            transform: translateY(-3px);
        }
        
        .cert-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .cert-title {
            color: #1e3a8a;
            font-weight: 600;
            font-size: 1rem;
        }
        
        .cert-issuer {
            color: #6b7280;
            font-size: 0.9rem;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        @media (max-width: 768px) {
            .hero-title { font-size: 2rem; }
            .hero-subtitle { font-size: 1.2rem; }
            .section-header { font-size: 1.5rem; }
            .hero-contact { flex-direction: column; gap: 0.5rem; }
        }
    </style>
    """, unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    """Generate download link for binary files"""
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}" class="download-btn">📄 Download {file_label}</a>'
        return href
    except Exception as e:
        return f'<p style="color: red;">Error loading file: {str(e)}</p>'

def show_documents():
    """Display downloadable documents section"""
    st.markdown('<h2 class="section-header">📚 Educational Documents & Certificates</h2>', unsafe_allow_html=True)
    
    documents_path = Path("assets/documents")
    
    if not documents_path.exists():
        st.warning("Documents folder not found. Please create 'assets/documents' directory and upload your CV, certificates, and academic documents.")
        st.info("Supported files: PDF, DOCX, JPG, PNG")
        return
    
    documents = list(documents_path.glob("*"))
    supported_extensions = {'.pdf', '.docx', '.doc', '.jpg', '.jpeg', '.png'}
    documents = [d for d in documents if d.suffix.lower() in supported_extensions]
    
    if not documents:
        st.info("No documents found. Please add your files to the 'assets/documents' folder.")
        return
    
    cols = st.columns(min(len(documents), 2))
    
    for idx, doc in enumerate(documents):
        with cols[idx % 2]:
            file_size = doc.stat().st_size / 1024
            size_str = f"{file_size:.1f} KB" if file_size < 1024 else f"{file_size/1024:.1f} MB"
            
            st.markdown(f"""
            <div class="info-card">
                <div class="card-title">📄 {doc.stem.replace('_', ' ').title()}</div>
                <div class="card-description" style="margin-bottom: 1rem;">
                    Type: {doc.suffix.upper()[1:]} • Size: {size_str}
                </div>
                {get_binary_file_downloader_html(str(doc), doc.name)}
            </div>
            """, unsafe_allow_html=True)

def main():
    load_css()
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">FENI OBED TENKORANG</div>
        <div class="hero-subtitle">Electrical Engineer | Hardware & Systems Technician</div>
        <div style="max-width: 800px; margin: 0 auto; opacity: 0.9; line-height: 1.6;">
            Electrical Engineer with hands-on experience in industrial and mining electrical systems, 
            hardware installation, configuration, and technical support. Skilled in deploying and 
            maintaining switchgear, transformers, SCADA systems, and field instrumentation.
        </div>
        <div class="hero-contact">
            <div class="hero-contact-item">📞 +233 541 468 102</div>
            <div class="hero-contact-item">✉️ obedfeni23@gmail.com</div>
            <div class="hero-contact-item">📍 Ghana</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("""
    <div class="nav-container">
        <a href="#about" class="nav-link">About</a>
        <a href="#experience" class="nav-link">Experience</a>
        <a href="#education" class="nav-link">Education</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#projects" class="nav-link">Projects</a>
        <a href="#certifications" class="nav-link">Certifications</a>
        <a href="#documents" class="nav-link">Documents</a>
        <a href="#contact" class="nav-link">Contact</a>
    </div>
    """, unsafe_allow_html=True)
    
    # About Section
    st.markdown('<a name="about"></a>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">👨‍💻 Professional Summary</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%); 
                    height: 300px; border-radius: 15px; display: flex; 
                    align-items: center; justify-content: center; color: white;
                    font-size: 4rem; box-shadow: 0 10px 30px rgba(30, 58, 138, 0.3);">
            ⚡
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-description">
                Experienced in preventive and corrective maintenance, troubleshooting, system upgrades, 
                and commissioning in harsh industrial environments. Strong knowledge of safety compliance, 
                technical documentation, and client-focused technical service.
                <br><br>
                <strong>Core Competencies:</strong>
                <ul>
                    <li>Industrial & Mining Electrical Systems</li>
                    <li>SCADA Systems & Field Instrumentation</li>
                    <li>Switchgear & Transformer Testing</li>
                    <li>Preventive & Corrective Maintenance</li>
                    <li>QHSE Safety Standards & Job Hazard Analysis</li>
                    <li>Hardware Deployment & System Installation</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Experience Section
    st.markdown('<a name="experience"></a>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">💼 Work Experience</h2>', unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "Electrical Engineer — Switchgear Systems",
            "company": "Davak Engineering Services (Zijin Golden Ridge Limited)",
            "date": "Nov 2024 — Present",
            "description": """
            <ul>
                <li>Deployed, tested, and commissioned electrical systems including transformers and switchgear in active mining operations</li>
                <li>Configured and upgraded system components following technical specifications and change management procedures</li>
                <li>Provided on-site troubleshooting and technical support to resolve operational issues efficiently</li>
                <li>Prepared Job Hazard Analysis (JHA) and maintained compliance with QHSE safety standards</li>
                <li>Maintained technical documentation of deployed systems and project progress reports</li>
            </ul>
            """
        },
        {
            "title": "National Service Personnel — Electrical Maintenance",
            "company": "Volta River Authority (VRA), Akosombo Generating Station",
            "date": "Nov 2023 — Sep 2024",
            "description": """
            <ul>
                <li>Executed preventive and corrective maintenance on SCADA servers, CCTV systems, and field instruments</li>
                <li>Monitored system performance, diagnosed faults, and applied electrical protection standards</li>
                <li>Assisted with remote and on-site support for operational reliability of power plant equipment</li>
                <li>Collected and reported operational data for performance optimization and safety compliance</li>
            </ul>
            """
        },
        {
            "title": "Intern — Electrical Maintenance",
            "company": "Volta River Authority (VRA), Akosombo Generating Station",
            "date": "Sep 2022 — Nov 2022",
            "description": """
            <ul>
                <li>Assisted engineers in installation, inspection, and testing of transformers, switchgear, and auxiliary panels</li>
                <li>Supported SCADA system operations, monitoring, and data collection</li>
                <li>Observed and assisted in commissioning and troubleshooting of electrical systems</li>
            </ul>
            """
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-title">{exp['title']}</div>
            <div class="card-subtitle">{exp['company']}</div>
            <div class="card-date">📅 {exp['date']}</div>
            <div class="card-description">{exp['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Education Section
    st.markdown('<a name="education"></a>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">BSc. Electrical & Electronic Engineering</div>
            <div class="card-subtitle">University of Energy and Natural Resources</div>
            <div class="card-date">📅 Sep 2019 — Sep 2023</div>
            <div class="card-description">
                Comprehensive program covering power systems, electronics, control systems, 
                and industrial automation. Graduated with practical experience in hardware 
                systems and electrical infrastructure.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="card-title">General Science</div>
            <div class="card-subtitle">Okuapemman Senior High School</div>
            <div class="card-date">📅 Oct 2016 — Jun 2019</div>
            <div class="card-description">
                Strong foundation in Physics, Chemistry, and Mathematics. 
                Developed analytical and problem-solving skills essential for engineering studies.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True)
    
    skills = {
        "Electrical Systems": ["Switchgear", "Transformers", "SCADA Systems", "Field Instrumentation", "Power Distribution"],
        "Maintenance": ["Preventive Maintenance", "Corrective Maintenance", "Fault Diagnosis", "System Commissioning", "Troubleshooting"],
        "Safety & Compliance": ["QHSE Standards", "Job Hazard Analysis (JHA)", "Safety Protocols", "Risk Assessment"],
        "Software & Tools": ["Microsoft Office", "MATLAB (Basic)", "Python (Basic)", "Arduino Programming"],
        "Hardware": ["Hardware Deployment", "System Installation", "OS Installation", "System Upgrades", "Technical Documentation"]
    }
    
    for category, skill_list in skills.items():
        st.markdown(f'<div style="margin-bottom: 0.5rem;"><strong style="color: #1e3a8a; font-size: 1.1rem;">{category}:</strong></div>', unsafe_allow_html=True)
        badges = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skill_list])
        st.markdown(badges, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Projects Section
    st.markdown('<a name="projects"></a>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">🚀 Featured Project</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <div class="card-title">Smart Robotic Arm for Waste Sorting</div>
        <div class="card-subtitle">Final Year Project</div>
        <div class="card-description">
            <ul>
                <li>Designed and implemented automated robotic arm using sensors, Arduino, and motor control logic</li>
                <li>Developed object detection and classification systems, demonstrating skills in system deployment and programming</li>
                <li>Integrated hardware components with software algorithms for automated waste segregation</li>
                <li>Demonstrated practical application of embedded systems and automation principles</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications Section
    st.markdown('<a name="certifications"></a>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📜 Certifications</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    certifications = [
        ("🌐", "Basic Network Engineering", "Alison"),
        ("🔧", "MATLAB Engineering Workshop", "GHIE"),
        ("📊", "Excel for Beginners", "Online Course")
    ]
    
    cols = [col1, col2, col3]
    for idx, (icon, title, issuer) in enumerate(certifications):
        with cols[idx]:
            st.markdown(f"""
            <div class="cert-card">
                <div class="cert-icon">{icon}</div>
                <div class="cert-title">{title}</div>
                <div class="cert-issuer">{issuer}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Documents Section
    st.markdown('<a name="documents"></a>', unsafe_allow_html=True)
    show_documents()
    
    # Contact Section
    st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📫 Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📧</div>
            <div class="card-title">Email</div>
            <a href="mailto:obedfeni23@gmail.com" class="contact-link">obedfeni23@gmail.com</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📱</div>
            <div class="card-title">Phone</div>
            <a href="tel:+233541468102" class="contact-link">+233 541 468 102</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📍</div>
            <div class="card-title">Location</div>
            <span style="color: #374151;">Ghana</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2024 Feni Obed Tenkorang. Built with Streamlit ⚡</p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">Electrical Engineer | Hardware & Systems Technician</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
