"""
📡 Etisalat Telecom - Professional Business Website
Built with Streamlit | Designed for Enterprise Solutions
Author: Najat Al-Bakry | © 2026
"""

import streamlit as st
from datetime import datetime

# ================= إعدادات الصفحة الأساسية =================
st.set_page_config(
    page_title="Etisalat Telecom | حلول اتصالات متكاملة للأعمال",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= إدارة الحالة (Session State) =================
if 'active_section' not in st.session_state:
    st.session_state.active_section = 'home'
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# ================= CSS الاحترافي مع Animations =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800&display=swap');

/* ===== Base Reset ===== */
* { font-family: 'Cairo', sans-serif; box-sizing: border-box; margin: 0; padding: 0; }
.stApp { background: linear-gradient(135deg, #fffaf7 0%, #ffffff 100%); overflow-x: hidden; }
#MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }

/* ===== Navbar ===== */
.navbar {
    background: linear-gradient(135deg, #5b0008 0%, #7a0010 100%);
    padding: 15px 5%; border-radius: 0 0 30px 30px;
    display: flex; justify-content: space-between; align-items: center;
    color: white; box-shadow: 0 10px 40px rgba(91,0,8,0.3);
    position: sticky; top: 0; z-index: 1000; backdrop-filter: blur(10px);
}
.logo { font-size: 24px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 10px; cursor: pointer; transition: transform 0.3s ease; }
.logo:hover { transform: scale(1.05); }
.logo-icon { font-size: 30px; animation: pulse 2s infinite; }
@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }

.nav-links { display: flex; gap: 8px; flex-wrap: wrap; }
.nav-links span {
    padding: 10px 18px; font-size: 14px; font-weight: 600;
    color: rgba(255,255,255,0.9); border-radius: 50px; cursor: pointer;
    transition: all 0.3s ease; position: relative; overflow: hidden;
}
.nav-links span:hover { color: #fff; transform: translateY(-2px); background: rgba(255,255,255,0.15); }
.nav-links span.active { background: white; color: #7a0010; font-weight: 700; box-shadow: 0 5px 20px rgba(0,0,0,0.15); }
.menu-toggle { display: none; font-size: 26px; cursor: pointer; color: white; }

/* ===== Hero Section ===== */
.hero {
    margin: 30px 5%; min-height: 480px; border-radius: 35px;
    background: linear-gradient(135deg, rgba(91,0,8,0.92), rgba(122,0,16,0.88)),
                url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1920');
    background-size: cover; background-position: center; background-attachment: fixed;
    color: white; padding: 60px 50px; box-shadow: 0 25px 60px rgba(91,0,8,0.35);
    display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden;
}
.hero::before {
    content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: rotate 20s linear infinite;
}
@keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
.hero h1 { font-size: clamp(30px, 5vw, 48px); font-weight: 800; line-height: 1.25; margin-bottom: 18px; animation: fadeInUp 0.8s ease-out; position: relative; z-index: 2; }
.hero p { font-size: clamp(15px, 2.3vw, 19px); max-width: 650px; line-height: 1.85; opacity: 0.95; animation: fadeInUp 0.8s ease-out 0.2s both; position: relative; z-index: 2; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(25px); } to { opacity: 1; transform: translateY(0); } }

.hero-btn {
    display: inline-flex; align-items: center; gap: 8px; margin-top: 30px;
    padding: 15px 38px; background: white; color: #7a0010 !important;
    border-radius: 50px; font-weight: 700; font-size: 16px; text-decoration: none;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2); position: relative; z-index: 2;
    cursor: pointer; border: none;
}
.hero-btn:hover { transform: translateY(-4px) scale(1.02); box-shadow: 0 18px 40px rgba(0,0,0,0.3); }

/* ===== Sections ===== */
.section-title {
    text-align: center; color: #5b0008; font-size: clamp(26px, 4vw, 38px);
    font-weight: 800; margin: 70px 5% 10px; position: relative; display: inline-block;
    left: 50%; transform: translateX(-50%);
}
.section-title::after {
    content: ''; position: absolute; bottom: -10px; left: 50%; transform: translateX(-50%);
    width: 65px; height: 4px; background: linear-gradient(90deg, #7a0010, #b30018); border-radius: 2px;
}
.section-subtitle {
    text-align: center; color: #666; font-size: clamp(14px, 2vw, 17px);
    margin: 15px 5% 45px; max-width: 680px; margin-left: auto; margin-right: auto; line-height: 1.7;
}

/* ===== Cards ===== */
.services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 22px; padding: 0 5% 35px; }
.card {
    background: white; border-radius: 26px; padding: 32px 28px; min-height: 270px;
    box-shadow: 0 14px 38px rgba(91,0,8,0.11); border: 1px solid #f1d7d9;
    transition: all 0.4s ease; position: relative; overflow: hidden; cursor: pointer;
}
.card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #7a0010, #b30018); transform: scaleX(0);
    transition: transform 0.4s ease; transform-origin: left;
}
.card:hover { transform: translateY(-8px); box-shadow: 0 22px 55px rgba(91,0,8,0.22); border-color: #e0b5b9; }
.card:hover::before { transform: scaleX(1); }
.card-icon { font-size: 40px; margin-bottom: 16px; display: block; transition: transform 0.3s ease; }
.card:hover .card-icon { transform: scale(1.12) rotate(3deg); }
.card h3 { color: #7a0010; font-size: 20px; font-weight: 700; margin-bottom: 10px; }
.card p { color: #555; font-size: 14px; line-height: 1.8; margin: 0; }

/* ===== About ===== */
.about-box {
    background: linear-gradient(135deg, #7a0010 0%, #5b0008 100%); color: white;
    padding: clamp(28px, 5.5vw, 55px); border-radius: 32px; margin: 55px 5%;
    box-shadow: 0 18px 45px rgba(91,0,8,0.28); position: relative; overflow: hidden;
}
.about-box::before {
    content: ''; position: absolute; top: -40%; right: -15%; width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%); border-radius: 50%;
}
.about-box h2 { font-size: clamp(24px, 3.8vw, 32px); font-weight: 800; position: relative; z-index: 2; margin-bottom: 15px; }
.about-box p { font-size: clamp(14px, 2vw, 17px); line-height: 1.9; opacity: 0.95; position: relative; z-index: 2; margin: 0; }

/* ===== Contact ===== */
.contact-section { padding: 20px 5% 55px; }
.contact-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 28px; max-width: 1150px; margin: 0 auto; }
.contact-box {
    background: white; border: 1px solid #f1d7d9; border-radius: 28px;
    padding: 35px 30px; text-align: center; box-shadow: 0 14px 38px rgba(91,0,8,0.09);
    transition: transform 0.3s ease;
}
.contact-box:hover { transform: translateY(-4px); }
.contact-box h2 { color: #5b0008; font-size: 24px; font-weight: 700; margin-bottom: 12px; }
.contact-box p { color: #666; font-size: 15px; line-height: 1.65; margin-bottom: 22px; }

.contact-btn {
    display: inline-flex; align-items: center; gap: 7px; margin: 7px;
    padding: 13px 28px; background: linear-gradient(135deg, #7a0010, #5b0008);
    color: white !important; border-radius: 50px; font-weight: 600; font-size: 14px;
    text-decoration: none; transition: all 0.33s ease; box-shadow: 0 7px 22px rgba(122,0,16,0.28);
    border: none; cursor: pointer;
}
.contact-btn:hover { transform: translateY(-3px); box-shadow: 0 13px 32px rgba(122,0,16,0.42); }
.contact-btn.secondary { background: white; color: #7a0010 !important; border: 2px solid #7a0010; box-shadow: none; }
.contact-btn.secondary:hover { background: #7a0010; color: white !important; }

/* ===== Form Styling ===== */
.contact-form { background: white; border-radius: 28px; padding: 35px; box-shadow: 0 14px 38px rgba(91,0,8,0.11); border: 1px solid #f1d7d9; }
.stTextInput > div > div > input, .stTextArea > div > div > textarea {
    border-radius: 12px !important; border: 2px solid #f1d7d9 !important;
    padding: 12px 16px !important; font-size: 14px !important; transition: all 0.3s ease !important; background: #fff !important;
}
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
    border-color: #7a0010 !important; box-shadow: 0 0 0 3px rgba(122,0,16,0.08) !important;
}
.stButton > button {
    background: linear-gradient(135deg, #7a0010, #5b0008) !important; color: white !important;
    border: none !important; border-radius: 50px !important; padding: 13px 40px !important;
    font-weight: 600 !important; font-size: 15px !important; transition: all 0.33s ease !important;
    box-shadow: 0 7px 22px rgba(122,0,16,0.28) !important; width: auto !important;
}
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 13px 32px rgba(122,0,16,0.42) !important; }

.success-message {
    background: linear-gradient(135deg, #10b981, #059669); color: white;
    padding: 18px 22px; border-radius: 18px; text-align: center; font-weight: 600;
    animation: slideIn 0.45s ease; margin: 18px 0;
}
@keyframes slideIn { from { opacity: 0; transform: translateY(-18px); } to { opacity: 1; transform: translateY(0); } }

/* ===== Floating WhatsApp ===== */
.whatsapp-float {
    position: fixed; bottom: 22px; right: 22px;
    background: linear-gradient(135deg, #25D366, #128C7E); color: white !important;
    width: 62px; height: 62px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center; font-size: 30px;
    text-decoration: none; box-shadow: 0 9px 32px rgba(37,211,102,0.48);
    z-index: 9999; transition: all 0.38s ease; animation: bounce 2s infinite;
}
.whatsapp-float:hover { transform: scale(1.1) rotate(8deg); box-shadow: 0 14px 42px rgba(37,211,102,0.65); }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-9px); } }

/* ===== Footer ===== */
.footer {
    text-align: center; padding: 32px 20px 45px; margin-top: 35px;
    color: #7a0010; font-weight: 600; font-size: 14px;
    background: linear-gradient(transparent, rgba(122,0,16,0.03));
}
.footer-links { display: flex; justify-content: center; gap: 22px; margin-bottom: 18px; flex-wrap: wrap; }
.footer-links a { color: #7a0010; text-decoration: none; font-weight: 500; transition: color 0.3s ease; opacity: 0.85; }
.footer-links a:hover { color: #5b0008; opacity: 1; }

/* ===== Responsive ===== */
@media (max-width: 992px) {
    .navbar { flex-wrap: wrap; padding: 12px 4%; }
    .nav-links { width: 100%; justify-content: center; margin-top: 10px; gap: 4px; }
    .nav-links span { padding: 7px 13px; font-size: 13px; }
    .hero { padding: 45px 28px; margin: 18px 3%; }
    .services-grid { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
}
@media (max-width: 768px) {
    .menu-toggle { display: block; }
    .nav-links { display: none; width: 100%; flex-direction: column; align-items: center; margin-top: 12px; padding: 12px 0; background: rgba(255,255,255,0.1); border-radius: 12px; }
    .nav-links.active { display: flex; }
    .nav-links span { width: 100%; text-align: center; padding: 10px; margin: 2px 0; }
    .hero { padding: 35px 22px; min-height: auto; }
    .hero h1 { font-size: 26px; }
    .hero p { font-size: 14px; }
    .section-title { font-size: 24px; }
    .about-box { padding: 32px 22px; }
    .contact-form { padding: 28px 22px; }
}
@media (max-width: 480px) {
    .navbar { padding: 9px 3%; }
    .logo { font-size: 20px; }
    .hero { padding: 30px 18px; border-radius: 22px; }
    .hero-btn { padding: 13px 28px; font-size: 14px; }
    .card { padding: 26px 20px; min-height: auto; }
    .contact-btn { padding: 11px 22px; font-size: 13px; margin: 4px; }
    .whatsapp-float { width: 52px; height: 52px; font-size: 24px; }
}

/* ===== Streamlit Overrides ===== */
.stMarkdown p { margin: 0; }
.element-container { margin-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ================= Navbar تفاعلي =================
def render_navbar():
    nav_html = f"""
    <div class="navbar">
        <div class="logo">
            <span class="logo-icon">📡</span>Etisalat Telecom
        </div>
        <div class="menu-toggle" onclick="toggleMenu()">☰</div>
        <div class="nav-links" id="navLinks">
            <span class="{'active' if st.session_state.active_section == 'home' else ''}" 
                  onclick="setSection('home')">🏠 الرئيسية</span>
            <span class="{'active' if st.session_state.active_section == 'services' else ''}" 
                  onclick="setSection('services')">🛠️ الخدمات</span>
            <span class="{'active' if st.session_state.active_section == 'about' else ''}" 
                  onclick="setSection('about')">🏢 من نحن</span>
            <span class="{'active' if st.session_state.active_section == 'contact' else ''}" 
                  onclick="setSection('contact')">📬 تواصل معنا</span>
        </div>
    </div>
    <script>
        function setSection(sec) {{
            const streamlitDoc = window.parent.document;
            const radio = streamlitDoc.querySelector('input[type="radio"][value="'+sec+'"]');
            if(radio) {{ radio.click(); }}
        }}
        function toggleMenu() {{
            document.getElementById('navLinks').classList.toggle('active');
        }}
    </script>
    """
    st.markdown(nav_html, unsafe_allow_html=True)

# زر التنقل المخفي
section = st.radio(
    "Navigate", ["home", "services", "about", "contact"],
    index=["home", "services", "about", "contact"].index(st.session_state.active_section),
    label_visibility="collapsed", horizontal=True, key="nav_radio"
)
if section != st.session_state.active_section:
    st.session_state.active_section = section
    st.rerun()

render_navbar()

# ================= 🏠 الصفحة الرئيسية =================
if st.session_state.active_section == 'home':
    st.markdown("""
    <div class="hero">
        <h1>حلول اتصالات متكاملة <br>لأعمال المستقبل</h1>
        <p>نقدم لشركتك خدمات اتصالات مؤسسية متطورة، وحلول اتصال موثوقة، 
        وبنية رقمية ذكية تدعم نمو أعمالك في العصر الرقمي.</p>
        <button class="hero-btn" onclick="setSection('services')">✨ ابدأ رحلتك الآن</button>
    </div>
    """, unsafe_allow_html=True)
    
    # إحصائيات سريعة
    cols = st.columns(4)
    stats = [("🏢", "+500", "شركة عميلة"), ("📞", "24/7", "دعم فني"), 
             ("🌍", "99.9%", "نسبة التوفر"), ("🚀", "+10", "سنوات خبرة")]
    for col, (icon, val, label) in zip(cols, stats):
        col.markdown(f"""
        <div style="text-align:center; padding:18px;">
            <div style="font-size:30px;">{icon}</div>
            <div style="font-size:22px; font-weight:800; color:#7a0010;">{val}</div>
            <div style="font-size:13px; color:#666;">{label}</div>
        </div>""", unsafe_allow_html=True)
    
    # معاينة الخدمات
    st.markdown('<div class="section-title">أهم خدماتنا</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">حلول مصممة خصيصاً لاحتياجات قطاع الأعمال</div>', unsafe_allow_html=True)
    
    services = [
        ("📱", "الخطوط المؤسسية", "إدارة خطوط الجوال للشركات، باقات صوت وبيانات، ودعم فني مخصص"),
        ("🌐", "إنترنت الأعمال", "اتصال إنترنت ثابت و4G/5G للشركات مع خطوط احتياطية"),
        ("🛰️", "الأقمار الصناعية", "حلول VSAT للمواقع النائية والمناجم والمشاريع الصحراوية"),
        ("🔐", "الأمن السيبراني", "حماية البنية الرقمية للشركات من التهديدات الإلكترونية")
    ]
    for i in range(0, len(services), 2):
        c1, c2 = st.columns(2)
        for j, (icon, title, desc) in enumerate(services[i:i+2]):
            with [c1, c2][j]:
                st.markdown(f"""
                <div class="card" onclick="setSection('services')">
                    <span class="card-icon">{icon}</span>
                    <h3>{title}</h3><p>{desc}</p>
                </div>""", unsafe_allow_html=True)
    
    # CTA
    st.markdown("""
    <div style="text-align:center; margin:45px 5%; padding:35px; background:linear-gradient(135deg,#fff5f5,#fff); 
                border-radius:22px; border:2px dashed #f1d7d9;">
        <h3 style="color:#7a0010; margin-bottom:12px;">جاهز لتحويل اتصالات شركتك؟</h3>
        <p style="color:#666; margin-bottom:20px;">فريقنا جاهز لتصميم الحل الأمثل لاحتياجاتك</p>
        <button class="hero-btn" onclick="setSection('contact')" style="margin:0;">📩 استشارة مجانية</button>
    </div>""", unsafe_allow_html=True)

# ================= 🛠️ صفحة الخدمات =================
elif st.session_state.active_section == 'services':
    st.markdown('<div class="section-title">حلولنا المتكاملة</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">نقدم باقة شاملة من خدمات الاتصالات والبنية الرقمية</div>', unsafe_allow_html=True)
    
    services = [
        ("📱", "الخطوط المؤسسية", "إدارة محفظة خطوط الجوال، تخصيص الباقات، تحسين التعريفات، متابعة الفواتير، ودعم مخصص."),
        ("🌐", "إنترنت الأعمال", "إنترنت ثابت، راوترات 4G/5G، خطوط احتياطية تلقائية، وخدمات بيانات عالية السرعة."),
        ("🛰️", "الأقمار الصناعية - VSAT", "اتصال عبر الأقمار الصناعية للمواقع النائية، المناجم، المناطق الصحراوية، والعمليات الحرجة."),
        ("🏗️", "البنية الرقمية", "البنية التحتية الذكية، التحول الرقمي، الشبكات المؤسسية، وتقنيات السحابة."),
        ("🔒", "الأنظمة المتكاملة", "المراقبة الذكية، الاتصال الداخلي، إدارة الوصول، والتكامل بين الأنظمة التقنية."),
        ("📊", "إدارة الحسابات", "مدير حساب مخصص، متابعة الدعم، تتبع الفواتير، وتقارير دورية للأداء.")
    ]
    
    for icon, title, desc in services:
        st.markdown(f"""
        <div class="services-grid">
            <div class="card">
                <span class="card-icon">{icon}</span>
                <h3>{title}</h3><p>{desc}</p>
            </div>
        </div>""", unsafe_allow_html=True)
    
    # Badges
    st.markdown("""
    <div style="text-align:center; margin:45px 5%; padding:28px; background:white; border-radius:22px; box-shadow:0 10px 30px rgba(91,0,8,0.08);">
        <p style="color:#666; margin-bottom:18px; font-weight:600;">مدعومة بأحدث التقنيات</p>
        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
            <span style="padding:7px 18px; background:#f1d7d9; border-radius:50px; font-size:13px; color:#7a0010; font-weight:600;">5G Ready</span>
            <span style="padding:7px 18px; background:#f1d7d9; border-radius:50px; font-size:13px; color:#7a0010; font-weight:600;">Cloud Native</span>
            <span style="padding:7px 18px; background:#f1d7d9; border-radius:50px; font-size:13px; color:#7a0010; font-weight:600;">ISO 27001</span>
            <span style="padding:7px 18px; background:#f1d7d9; border-radius:50px; font-size:13px; color:#7a0010; font-weight:600;">SLA Guaranteed</span>
        </div>
    </div>""", unsafe_allow_html=True)

# ================= 🏢 صفحة من نحن =================
elif st.session_state.active_section == 'about':
    st.markdown("""
    <div class="about-box">
        <h2>عن اتصالات للأعمال</h2>
        <p>نحن شريك استراتيجي في مجال حلول الاتصالات للشركات، نتمتع بخبرة تزيد عن 10 سنوات 
        في تقديم خدمات اتصال موثوقة وآمنة. نركز على تبسيط العمليات التقنية لشركائنا 
        من خلال حلول قابلة للتطوير، مدعومة بفريق دعم فني متخصص على مدار الساعة.</p>
    </div>""", unsafe_allow_html=True)
    
    # القيم
    st.markdown('<div class="section-title">قيمنا الأساسية</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    values = [
        ("🎯", "التركيز على العميل", "نضع احتياجات شركتك في قلب كل قرار نتخذه"),
        ("🔐", "الموثوقية والأمان", "بنية تحتية آمنة مع ضمانات مستوى الخدمة (SLA)"),
        ("🚀", "الابتكار المستمر", "نواكب أحدث التقنيات لنقدم لك الأفضل دائماً")
    ]
    for col, (icon, title, desc) in zip(cols, values):
        col.markdown(f"""
        <div style="text-align:center; padding:22px;">
            <div style="font-size:38px; margin-bottom:12px;">{icon}</div>
            <h4 style="color:#7a0010; margin-bottom:8px;">{title}</h4>
            <p style="color:#666; font-size:14px; line-height:1.7;">{desc}</p>
        </div>""", unsafe_allow_html=True)
    
    # الجدول الزمني
    st.markdown('<div class="section-title">محطاتنا</div>', unsafe_allow_html=True)
    timeline = [("2016", "انطلاق خدمات الأعمال"), ("2019", "توسيع تغطية الأقمار الصناعية"),
                ("2022", "إطلاق منصة إدارة الحسابات الرقمية"), ("2025", "الشراكة مع مؤسسات حكومية كبرى")]
    for year, event in timeline:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:18px; margin:12px 5%; padding:14px 22px; 
                    background:white; border-radius:18px; box-shadow:0 5px 18px rgba(91,0,8,0.07);">
            <div style="background:linear-gradient(135deg,#7a0010,#5b0008); color:white; 
                        padding:9px 18px; border-radius:13px; font-weight:700; min-width:75px; text-align:center;">{year}</div>
            <div style="color:#555; font-size:15px; font-weight:500;">{event}</div>
        </div>""", unsafe_allow_html=True)

# ================= 📬 صفحة التواصل =================
elif st.session_state.active_section == 'contact':
    st.markdown('<div class="section-title" id="contact">تواصل معنا</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.15])
    
    with col1:
        st.markdown("""
        <div class="contact-box">
            <h2 style="color:#5b0008;">📞 قنوات الاتصال</h2>
            <p style="color:#666; font-size:15px;">فريق الدعم والمبيعات جاهز للرد على مدار الساعة</p>
            <a class="contact-btn" href="tel:111">📞 اتصل بـ 111</a><br>
            <a class="contact-btn secondary" href="mailto:b2b@etisalat.com.eg">✉️ b2b@etisalat.com.eg</a><br>
            <a class="contact-btn" href="https://wa.me/201000000000" target="_blank" style="background:linear-gradient(135deg,#25D366,#128C7E);">💬 واتساب</a>
            <div style="margin-top:28px; padding-top:22px; border-top:1px solid #f1d7d9;">
                <p style="color:#666; font-size:14px; margin-bottom:12px;"><strong>🕒 ساعات العمل</strong></p>
                <p style="color:#555; font-size:13px;">الأحد - الخميس: 8:00 ص - 8:00 م</p>
                <p style="color:#555; font-size:13px;">الجمعة - السبت: 10:00 ص - 4:00 م</p>
            </div>
        </div>""", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="contact-form"><h3 style="color:#7a0010; margin-bottom:18px; text-align:center;">📩 أرسل رسالة</h3>', unsafe_allow_html=True)
        
        if st.session_state.form_submitted:
            st.markdown('<div class="success-message">✅ تم الإرسال بنجاح! سنتواصل معك خلال 24 ساعة.</div>', unsafe_allow_html=True)
            if st.button("🔄 رسالة جديدة"):
                st.session_state.form_submitted = False
                st.rerun()
        else:
            with st.form("contact_form"):
                name = st.text_input("الاسم الكامل *", placeholder="أدخل اسمك")
                company = st.text_input("اسم الشركة", placeholder="اسم مؤسستك")
                email = st.text_input("البريد الإلكتروني *", placeholder="name@company.com")
                phone = st.text_input("رقم الجوال", placeholder="+20 1XX XXX XXXX")
                service = st.selectbox("نوع الخدمة", ["اختر...", "الخطوط المؤسسية", "إنترنت الأعمال", "الأقمار الصناعية", "البنية الرقمية", "دعم فني", "أخرى"])
                message = st.text_area("تفاصيل الطلب *", placeholder="اشرح احتياجاتك...", height=110)
                
                c1, c2 = st.columns([1, 3])
                with c1: submit = st.form_submit_button("📤 إرسال")
                with c2: st.form_submit_button("🗑️ مسح", type="secondary")
            
            if submit:
                if name and email and message:
                    st.session_state.form_data = {"name": name, "email": email, "company": company, "phone": phone, "service": service, "message": message, "date": datetime.now().strftime("%Y-%m-%d %H:%M")}
                    st.session_state.form_submitted = True
                    st.rerun()
                else:
                    st.error("⚠️ يرجى ملء الحقول المطلوبة (*)")
        st.markdown('</div>', unsafe_allow_html=True)

# ================= زر واتساب العائم =================
st.markdown('<a class="whatsapp-float" href="https://wa.me/201000000000" target="_blank" title="واتساب">💬</a>', unsafe_allow_html=True)

# ================= Footer =================
st.markdown("""
<div class="footer">
    <div class="footer-links">
        <a href="#">سياسة الخصوصية</a>
        <a href="#">شروط الاستخدام</a>
        <a href="#">الدعم الفني</a>
        <a href="#">خريطة الموقع</a>
    </div>
    <p>Etisalat Telecom © 2026 — Connect The Future 🌐</p>
    <p style="font-size:12px; opacity:0.7; margin-top:6px;">جميع الحقوق محفوظة | حلول اتصالات مؤسسية معتمدة</p>
</div>""", unsafe_allow_html=True)
