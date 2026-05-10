import streamlit as st
import time
from datetime import datetime

# ================= إعدادات الصفحة =================
st.set_page_config(
    page_title="Etisalat Telecom | حلول اتصالات متكاملة",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= إدارة الحالة (Session State) =================
if 'active_section' not in st.session_state:
    st.session_state.active_section = 'home'
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# ================= CSS محسّن مع Animations وتجاوب =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800&display=swap');

/* Reset & Base */
* {
    font-family: 'Cairo', sans-serif;
    box-sizing: border-box;
}

.stApp {
    background: linear-gradient(135deg, #fffaf7 0%, #ffffff 100%);
    overflow-x: hidden;
}

/* Hide Streamlit elements */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

/* ================= Navbar محسّن ================= */
.navbar {
    background: linear-gradient(135deg, #5b0008 0%, #7a0010 100%);
    padding: 15px 5%;
    border-radius: 0 0 30px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    box-shadow: 0 10px 40px rgba(91,0,8,0.3);
    position: sticky;
    top: 0;
    z-index: 1000;
    backdrop-filter: blur(10px);
}

.logo {
    font-size: 26px;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    transition: transform 0.3s ease;
}
.logo:hover { transform: scale(1.05); }

.logo-icon {
    font-size: 32px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

.nav-links {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.nav-links span {
    padding: 10px 20px;
    font-size: 15px;
    font-weight: 600;
    color: rgba(255,255,255,0.9);
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.nav-links span::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.15);
    border-radius: 50px;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.nav-links span:hover {
    color: #fff;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}
.nav-links span:hover::before { opacity: 1; }

.nav-links span.active {
    background: white;
    color: #7a0010;
    font-weight: 700;
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}

/* Mobile Menu Toggle */
.menu-toggle {
    display: none;
    font-size: 28px;
    cursor: pointer;
    color: white;
    padding: 5px;
}

/* ================= Hero Section ================= */
.hero {
    margin: 30px 5%;
    min-height: 500px;
    border-radius: 35px;
    background: 
        linear-gradient(135deg, rgba(91,0,8,0.92) 0%, rgba(122,0,16,0.88) 50%, rgba(155,0,18,0.85) 100%),
        url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1920');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
    padding: 70px 60px;
    box-shadow: 0 25px 60px rgba(91,0,8,0.35);
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: rotate 20s linear infinite;
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.hero h1 {
    font-size: clamp(32px, 5vw, 52px);
    font-weight: 800;
    line-height: 1.25;
    margin-bottom: 20px;
    animation: fadeInUp 0.8s ease-out;
    position: relative;
    z-index: 2;
}

.hero p {
    font-size: clamp(16px, 2.5vw, 20px);
    max-width: 680px;
    line-height: 1.9;
    opacity: 0.95;
    animation: fadeInUp 0.8s ease-out 0.2s both;
    position: relative;
    z-index: 2;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    margin-top: 35px;
    padding: 16px 42px;
    background: white;
    color: #7a0010 !important;
    border-radius: 50px;
    font-weight: 700;
    font-size: 17px;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    position: relative;
    z-index: 2;
    cursor: pointer;
    border: none;
}

.hero-btn:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 20px 45px rgba(0,0,0,0.35);
    background: #fff9f9;
}

.hero-btn:active {
    transform: translateY(-1px);
}

/* ================= Sections Titles ================= */
.section-title {
    text-align: center;
    color: #5b0008;
    font-size: clamp(28px, 4vw, 40px);
    font-weight: 800;
    margin: 80px 5% 10px;
    position: relative;
    display: inline-block;
    left: 50%;
    transform: translateX(-50%);
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -12px;
    left: 50%;
    transform: translateX(-50%);
    width: 70px;
    height: 4px;
    background: linear-gradient(90deg, #7a0010, #b30018);
    border-radius: 2px;
}

.section-subtitle {
    text-align: center;
    color: #666;
    font-size: clamp(15px, 2vw, 18px);
    margin: 15px 5% 50px;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.7;
}

/* ================= Cards Grid ================= */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    padding: 0 5% 40px;
}

.card {
    background: white;
    border-radius: 28px;
    padding: 35px 30px;
    min-height: 280px;
    box-shadow: 0 15px 40px rgba(91,0,8,0.12);
    border: 1px solid #f1d7d9;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    cursor: pointer;
}

.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #7a0010, #b30018);
    transform: scaleX(0);
    transition: transform 0.4s ease;
    transform-origin: left;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 25px 60px rgba(91,0,8,0.25);
    border-color: #e0b5b9;
}

.card:hover::before {
    transform: scaleX(1);
}

.card-icon {
    font-size: 42px;
    margin-bottom: 18px;
    display: block;
    transition: transform 0.3s ease;
}

.card:hover .card-icon {
    transform: scale(1.15) rotate(5deg);
}

.card h3 {
    color: #7a0010;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 12px;
}

.card p {
    color: #555;
    font-size: 15px;
    line-height: 1.85;
    margin: 0;
}

/* ================= About Section ================= */
.about-box {
    background: linear-gradient(135deg, #7a0010 0%, #5b0008 100%);
    color: white;
    padding: clamp(30px, 6vw, 60px);
    border-radius: 35px;
    margin: 60px 5%;
    box-shadow: 0 20px 50px rgba(91,0,8,0.3);
    display: grid;
    grid-template-columns: 1fr;
    gap: 25px;
    position: relative;
    overflow: hidden;
}

.about-box::before {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
    border-radius: 50%;
}

.about-box h2 {
    font-size: clamp(26px, 4vw, 34px);
    font-weight: 800;
    position: relative;
    z-index: 2;
}

.about-box p {
    font-size: clamp(15px, 2.2vw, 18px);
    line-height: 1.95;
    opacity: 0.95;
    position: relative;
    z-index: 2;
    margin: 0;
}

/* ================= Contact Section ================= */
.contact-section {
    padding: 20px 5% 60px;
}

.contact-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
}

.contact-box {
    background: white;
    border: 1px solid #f1d7d9;
    border-radius: 30px;
    padding: 40px 35px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(91,0,8,0.1);
    transition: transform 0.3s ease;
}

.contact-box:hover {
    transform: translateY(-5px);
}

.contact-box h2 {
    color: #5b0008;
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 15px;
}

.contact-box p {
    color: #666;
    font-size: 16px;
    line-height: 1.7;
    margin-bottom: 25px;
}

.contact-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin: 8px;
    padding: 14px 32px;
    background: linear-gradient(135deg, #7a0010, #5b0008);
    color: white !important;
    border-radius: 50px;
    font-weight: 600;
    font-size: 15px;
    text-decoration: none;
    transition: all 0.35s ease;
    box-shadow: 0 8px 25px rgba(122,0,16,0.3);
    border: none;
    cursor: pointer;
}

.contact-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px rgba(122,0,16,0.45);
    background: linear-gradient(135deg, #8b0012, #6b000a);
}

.contact-btn.secondary {
    background: white;
    color: #7a0010 !important;
    border: 2px solid #7a0010;
    box-shadow: none;
}
.contact-btn.secondary:hover {
    background: #7a0010;
    color: white !important;
}

/* ================= Contact Form ================= */
.contact-form {
    background: white;
    border-radius: 30px;
    padding: 40px;
    box-shadow: 0 15px 40px rgba(91,0,8,0.12);
    border: 1px solid #f1d7d9;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    border-radius: 14px !important;
    border: 2px solid #f1d7d9 !important;
    padding: 14px 18px !important;
    font-size: 15px !important;
    transition: all 0.3s ease !important;
    background: #fff !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #7a0010 !important;
    box-shadow: 0 0 0 4px rgba(122,0,16,0.1) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #7a0010, #5b0008) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 14px 45px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    transition: all 0.35s ease !important;
    box-shadow: 0 8px 25px rgba(122,0,16,0.3) !important;
    width: auto !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 15px 35px rgba(122,0,16,0.45) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* Success Message */
.success-message {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    padding: 20px 25px;
    border-radius: 20px;
    text-align: center;
    font-weight: 600;
    animation: slideIn 0.5s ease;
    margin: 20px 0;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ================= Floating WhatsApp ================= */
.whatsapp-float {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: linear-gradient(135deg, #25D366, #128C7E);
    color: white !important;
    width: 65px;
    height: 65px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    text-decoration: none;
    box-shadow: 0 10px 35px rgba(37,211,102,0.5);
    z-index: 9999;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    animation: bounce 2s infinite;
}

.whatsapp-float:hover {
    transform: scale(1.12) rotate(10deg);
    box-shadow: 0 15px 45px rgba(37,211,102,0.7);
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

/* ================= Footer ================= */
.footer {
    text-align: center;
    padding: 35px 20px 50px;
    margin-top: 40px;
    color: #7a0010;
    font-weight: 600;
    font-size: 15px;
    background: linear-gradient(transparent, rgba(122,0,16,0.03));
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.footer-links a {
    color: #7a0010;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
    opacity: 0.85;
}
.footer-links a:hover {
    color: #5b0008;
    opacity: 1;
}

/* ================= Responsive Design ================= */
@media (max-width: 992px) {
    .navbar {
        flex-wrap: wrap;
        padding: 12px 4%;
    }
    .nav-links {
        width: 100%;
        justify-content: center;
        margin-top: 12px;
        gap: 5px;
    }
    .nav-links span {
        padding: 8px 14px;
        font-size: 14px;
    }
    .hero {
        padding: 50px 30px;
        margin: 20px 3%;
    }
    .services-grid {
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    }
}

@media (max-width: 768px) {
    .menu-toggle { display: block; }
    .nav-links {
        display: none;
        width: 100%;
        flex-direction: column;
        align-items: center;
        margin-top: 15px;
        padding: 15px 0;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
    }
    .nav-links.active { display: flex; }
    .nav-links span {
        width: 100%;
        text-align: center;
        padding: 12px;
        margin: 3px 0;
    }
    .hero {
        padding: 40px 25px;
        min-height: auto;
    }
    .hero h1 { font-size: 28px; }
    .hero p { font-size: 15px; }
    .section-title { font-size: 26px; }
    .about-box { padding: 35px 25px; }
    .contact-form { padding: 30px 25px; }
}

@media (max-width: 480px) {
    .navbar { padding: 10px 3%; }
    .logo { font-size: 22px; }
    .hero { padding: 35px 20px; border-radius: 25px; }
    .hero-btn { padding: 14px 32px; font-size: 15px; }
    .card { padding: 28px 22px; min-height: auto; }
    .contact-btn { padding: 12px 24px; font-size: 14px; margin: 5px; }
    .whatsapp-float { width: 55px; height: 55px; font-size: 26px; }
}

/* ================= Streamlit Overrides ================= */
.stMarkdown p { margin: 0; }
.element-container { margin-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ================= Navbar تفاعلي =================
def render_navbar():
    nav_html = f"""
    <div class="navbar">
        <div class="logo" onclick="navigate('home')">
            <span class="logo-icon">📡</span>
            Etisalat Telecom
        </div>
        <div class="menu-toggle" onclick="toggleMenu()">☰</div>
        <div class="nav-links" id="navLinks">
            <span class="{'active' if st.session_state.active_section == 'home' else ''}" 
                  onclick="navigate('home')">الرئيسية</span>
            <span class="{'active' if st.session_state.active_section == 'services' else ''}" 
                  onclick="navigate('services')">الخدمات</span>
            <span class="{'active' if st.session_state.active_section == 'about' else ''}" 
                  onclick="navigate('about')">من نحن</span>
            <span class="{'active' if st.session_state.active_section == 'contact' else ''}" 
                  onclick="navigate('contact')">تواصل معنا</span>
        </div>
    </div>
    
    <script>
        function navigate(section) {{
            const streamlitDoc = window.parent.document;
            const buttons = streamlitDoc.querySelectorAll('.stButton > button');
            // Trigger section change via session state
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                value: section
            }}, '*');
        }}
        function toggleMenu() {{
            document.getElementById('navLinks').classList.toggle('active');
        }}
    </script>
    """
    st.markdown(nav_html, unsafe_allow_html=True)

# زر تنقل مخفي للتحكم في الأقسام
section = st.radio(
    "Navigate",
    ["home", "services", "about", "contact"],
    index=["home", "services", "about", "contact"].index(st.session_state.active_section),
    label_visibility="collapsed",
    horizontal=True,
    key="nav_radio"
)

if section != st.session_state.active_section:
    st.session_state.active_section = section
    st.rerun()

render_navbar()

# ================= المحتوى الديناميكي حسب القسم =================

# 🏠 الصفحة الرئيسية
if st.session_state.active_section == 'home':
    # Hero Section
    st.markdown("""
    <div class="hero">
        <h1>حلول اتصالات متكاملة <br>لأعمال المستقبل</h1>
        <p>
            نقدم لشركتك خدمات اتصالات مؤسسية متطورة، وحلول اتصال موثوقة، 
            وبنية رقمية ذكية تدعم نمو أعمالك في العصر الرقمي.
        </p>
        <button class="hero-btn" onclick="navigate('services')">
            ✨ ابدأ رحلتك الآن
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        stats = [
            ("🏢", "+500", "شركة عميلة"),
            ("📞", "24/7", "دعم فني"),
            ("🌍", "99.9%", "نسبة التوفر"),
            ("🚀", "+10", "سنوات خبرة")
        ]
        for col, (icon, value, label) in zip([col1, col2, col3, col4], stats):
            col.markdown(f"""
            <div style="text-align:center; padding: 20px;">
                <div style="font-size:32px; margin-bottom:8px;">{icon}</div>
                <div style="font-size:24px; font-weight:800; color:#7a0010;">{value}</div>
                <div style="font-size:14px; color:#666;">{label}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Featured Services Preview
    st.markdown('<div class="section-title">أهم خدماتنا</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">حلول مصممة خصيصاً لاحتياجات قطاع الأعمال</div>', unsafe_allow_html=True)
    
    services_preview = [
        ("📱", "الخطوط المؤسسية", "إدارة خطوط الجوال للشركات، باقات صوت وبيانات، ودعم فني مخصص"),
        ("🌐", "إنترنت الأعمال", "اتصال إنترنت ثابت و4G/5G للشركات مع خطوط احتياطية"),
        ("🛰️", "خدمات الأقمار الصناعية", "حلول VSAT للمواقع النائية والمناجم والمشاريع الصحراوية"),
        ("🔐", "الأمن السيبراني", "حماية البنية الرقمية للشركات من التهديدات الإلكترونية")
    ]
    
    for i in range(0, len(services_preview), 2):
        cols = st.columns(2)
        for j, (icon, title, desc) in enumerate(services_preview[i:i+2]):
            with cols[j]:
                st.markdown(f"""
                <div class="card" style="cursor: pointer;" onclick="navigate('services')">
                    <span class="card-icon">{icon}</span>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
    <div style="text-align:center; margin: 50px 5%; padding: 40px; 
                background: linear-gradient(135deg, #fff5f5, #fff); 
                border-radius: 25px; border: 2px dashed #f1d7d9;">
        <h3 style="color:#7a0010; margin-bottom:15px;">جاهز لتحويل اتصالات شركتك؟</h3>
        <p style="color:#666; margin-bottom:25px;">فريقنا جاهز لتصميم الحل الأمثل لاحتياجاتك</p>
        <button class="hero-btn" onclick="navigate('contact')" style="margin:0;">
            📩 احصل على استشارة مجانية
        </button>
    </div>
    """, unsafe_allow_html=True)

# 🛠️ صفحة الخدمات
elif st.session_state.active_section == 'services':
    st.markdown('<div class="section-title">حلولنا المتكاملة</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">نقدم باقة شاملة من خدمات الاتصالات والبنية الرقمية المصممة لدعم نمو أعمالك</div>', unsafe_allow_html=True)
    
    services = [
        ("📱", "الخطوط المؤسسية", "إدارة محفظة خطوط الجوال للشركات، تخصيص باقات الصوت والبيانات، تحسين التعريفات، متابعة الفواتير، ودعم عملاء مخصص لحسابات الشركات."),
        ("🌐", "إنترنت الأعمال", "حلول اتصال إنترنت ثابت للشركات، راوترات 4G/5G للأعمال، خطوط احتياطية تلقائية، وخدمات بيانات مؤسسية عالية السرعة."),
        ("🛰️", "الأقمار الصناعية - VSAT", "حلول اتصال عبر الأقمار الصناعية للمواقع النائية، المناجم، المناطق الصحراوية، مواقع الإنشاءات، والعمليات الحرجة التي تتطلب اتصالاً مستقراً."),
        ("🏗️", "البنية الرقمية", "تصميم وتنفيذ البنية التحتية الذكية، حلول التحول الرقمي، الشبكات المؤسسية، وتقنيات السحابة للشركات."),
        ("🔒", "الأنظمة المتكاملة", "أنظمة المراقبة الذكية، حلول الاتصال الداخلي، إدارة الوصول، والتكامل بين الأنظمة التقنية المختلفة."),
        ("📊", "إدارة الحسابات", "مدير حساب مخصص للشركة، متابعة الدعم الفني، تتبع الفواتير والمدفوعات، وتقارير دورية لأداء الخدمات.")
    ]
    
    for icon, title, desc in services:
        st.markdown(f"""
        <div class="services-grid">
            <div class="card">
                <span class="card-icon">{icon}</span>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tech Stack Badges
    st.markdown("""
    <div style="text-align:center; margin: 50px 5%; padding: 30px; background:white; 
                border-radius:25px; box-shadow:0 10px 30px rgba(91,0,8,0.08);">
        <p style="color:#666; margin-bottom:20px; font-weight:600;">مدعومة بأحدث التقنيات</p>
        <div style="display:flex; justify-content:center; gap:15px; flex-wrap:wrap;">
            <span style="padding:8px 20px; background:#f1d7d9; border-radius:50px; font-size:14px; color:#7a0010; font-weight:600;">5G Ready</span>
            <span style="padding:8px 20px; background:#f1d7d9; border-radius:50px; font-size:14px; color:#7a0010; font-weight:600;">Cloud Native</span>
            <span style="padding:8px 20px; background:#f1d7d9; border-radius:50px; font-size:14px; color:#7a0010; font-weight:600;">ISO 27001</span>
            <span style="padding:8px 20px; background:#f1d7d9; border-radius:50px; font-size:14px; color:#7a0010; font-weight:600;">SLA Guaranteed</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 🏢 صفحة "من نحن"
elif st.session_state.active_section == 'about':
    st.markdown("""
    <div class="about-box">
        <h2>عن اتصالات للأعمال</h2>
        <p>
            نحن شريك استراتيجي في مجال حلول الاتصالات للشركات، نتمتع بخبرة تزيد عن 10 سنوات 
            في تقديم خدمات اتصال موثوقة وآمنة. نركز على تبسيط العمليات التقنية لشركائنا 
            من خلال حلول قابلة للتطوير، مدعومة بفريق دعم فني متخصص على مدار الساعة.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Values Grid
    st.markdown('<div class="section-title">قيمنا الأساسية</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    values = [
        ("🎯", "التركيز على العميل", "نضع احتياجات شركتك في قلب كل قرار نتخذه"),
        ("🔐", "الموثوقية والأمان", "بنية تحتية آمنة مع ضمانات مستوى الخدمة (SLA)"),
        ("🚀", "الابتكار المستمر", "نواكب أحدث التقنيات لنقدم لك الأفضل دائماً")
    ]
    for col, (icon, title, desc) in zip(cols, values):
        col.markdown(f"""
        <div style="text-align:center; padding:25px;">
            <div style="font-size:40px; margin-bottom:15px;">{icon}</div>
            <h4 style="color:#7a0010; margin-bottom:10px;">{title}</h4>
            <p style="color:#666; font-size:15px; line-height:1.7;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Timeline
    st.markdown('<div class="section-title">محطاتنا</div>', unsafe_allow_html=True)
    timeline = [
        ("2016", "انطلاق خدمات الأعمال"),
        ("2019", "توسيع نطاق تغطية الأقمار الصناعية"),
        ("2022", "إطلاق منصة إدارة الحسابات الرقمية"),
        ("2025", "الشراكة مع كبرى المؤسسات الحكومية")
    ]
    for year, event in timeline:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:20px; margin:15px 5%; padding:15px 25px; 
                    background:white; border-radius:20px; box-shadow:0 5px 20px rgba(91,0,8,0.08);">
            <div style="background:linear-gradient(135deg,#7a0010,#5b0008); color:white; 
                        padding:10px 20px; border-radius:15px; font-weight:700; min-width:80px; text-align:center;">
                {year}
            </div>
            <div style="color:#555; font-size:16px; font-weight:500;">{event}</div>
        </div>
        """, unsafe_allow_html=True)

# 📬 صفحة التواصل
elif st.session_state.active_section == 'contact':
    st.markdown('<div class="section-title" id="contact">تواصل معنا</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("""
        <div class="contact-box">
            <h2 style="color:#5b0008;">📞 قنوات الاتصال المباشرة</h2>
            <p style="color:#666; font-size:16px;">
                فريق الدعم الفني والمبيعات جاهز للرد على استفساراتكم على مدار الساعة
            </p>
            <a class="contact-btn" href="tel:111" style="margin:8px 0;">📞 اتصل بـ 111</a><br>
            <a class="contact-btn secondary" href="mailto:b2b@etisalat.com.eg" style="margin:8px 0;">✉️ b2b@etisalat.com.eg</a><br>
            <a class="contact-btn" href="https://wa.me/201000000000" target="_blank" style="margin:8px 0; background:linear-gradient(135deg,#25D366,#128C7E);">💬 واتساب للأعمال</a>
            
            <div style="margin-top:30px; padding-top:25px; border-top:1px solid #f1d7d9;">
                <p style="color:#666; font-size:15px; margin-bottom:15px;"><strong>🕒 ساعات العمل</strong></p>
                <p style="color:#555; font-size:14px;">الأحد - الخميس: 8:00 ص - 8:00 م</p>
                <p style="color:#555; font-size:14px;">الجمعة - السبت: 10:00 ص - 4:00 م</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="contact-form"><h3 style="color:#7a0010; margin-bottom:20px; text-align:center;">📩 أرسل لنا رسالة</h3>', unsafe_allow_html=True)
        
        if st.session_state.form_submitted:
            st.markdown('<div class="success-message">✅ تم إرسال رسالتك بنجاح! سنتواصل معك خلال 24 ساعة.</div>', unsafe_allow_html=True)
            if st.button("🔄 إرسال رسالة جديدة"):
                st.session_state.form_submitted = False
                st.rerun()
        else:
            with st.form("contact_form"):
                name = st.text_input("الاسم الكامل *", placeholder="أدخل اسمك")
                company = st.text_input("اسم الشركة", placeholder="اسم مؤسستك")
                email = st.text_input("البريد الإلكتروني *", placeholder="name@company.com")
                phone = st.text_input("رقم الجوال", placeholder="+20 1XX XXX XXXX")
                service = st.selectbox("نوع الخدمة المطلوبة", [
                    "اختر خدمة...",
                    "الخطوط المؤسسية",
                    "إنترنت الأعمال", 
                    "خدمات الأقمار الصناعية",
                    "البنية الرقمية",
                    "دعم فني",
                    "أخرى"
                ])
                message = st.text_area("تفاصيل الطلب *", placeholder="اشرح احتياجاتك...", height=120)
                
                col_btn1, col_btn2 = st.columns([1, 3])
                with col_btn1:
                    submit = st.form_submit_button("📤 إرسال")
                with col_btn2:
                    st.form_submit_button("🗑️ مسح", type="secondary")
            
            if submit:
                if name and email and message:
                    # هنا يمكن إضافة كود إرسال البريد أو حفظ في قاعدة بيانات
                    st.session_state.form_submitted = True
                    st.rerun()
                else:
                    st.error("⚠️ يرجى ملء الحقول المطلوبة (*)")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ================= زر واتساب العائم =================
st.markdown("""
<a class="whatsapp-float" href="https://wa.me/201000000000" target="_blank" title="تواصل عبر واتساب">
    💬
</a>
""", unsafe_allow_html=True)

# ================= Footer احترافي =================
st.markdown("""
<div class="footer">
    <div class="footer-links">
        <a href="#">سياسة الخصوصية</a>
        <a href="#">شروط الاستخدام</a>
        <a href="#">الدعم الفني</a>
        <a href="#">خريطة الموقع</a>
    </div>
    <p>Etisalat Telecom © 2026 — Connect The Future 🌐</p>
    <p style="font-size:13px; opacity:0.7; margin-top:8px;">جميع الحقوق محفوظة | حلول اتصالات مؤسسية معتمدة</p>
</div>
""", unsafe_allow_html=True)

# ================= تحسينات إضافية: تصدير التقارير =================
# (يمكن تفعيلها لاحقاً حسب الاحتياج)
# with st.sidebar:
#     st.markdown("### ⚙️ خيارات متقدمة")
#     if st.button("📥 تصدير الصفحة كـ PDF"):
#         # يمكن استخدام مكتبة pdfkit أو reportlab هنا
#         st.info("✅ جاري تجهيز الملف... (ميزة قيد التطوير)")
#     if st.button("📊 تصدير البيانات كـ Excel"):
#         st.info("✅ سيتم تصدير بيانات الخدمات قريباً")
