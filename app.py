import streamlit as st

st.set_page_config(
    page_title="Etisalat Telecom | Enterprise Solutions",
    page_icon="📡",
    layout="wide"
)

# ================= CSS MORDERN UPGRADE =================
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

:root {
    --primary: #5b0008;
    --secondary: #b30018;
    --light: #fffaf7;
    --text: #2d3436;
}

* { font-family: 'Cairo', sans-serif; }

.stApp { background-color: var(--light); }

/* Hide Streamlit elements */
#MainMenu, footer, header { visibility: hidden; }

/* Global Card Style */
.css-1r6slb0 { /* Target streamlit columns padding */
    padding: 10px;
}

/* Navbar */
.navbar {
    background: var(--primary);
    padding: 20px 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 0 0 30px 30px;
    box-shadow: 0 10px 30px rgba(91,0,8,0.3);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo-text { font-size: 26px; font-weight: 900; color: white; }

/* Hero Section */
.hero-section {
    background: linear-gradient(135deg, rgba(91,0,8,0.9) 0%, rgba(179,0,24,0.8) 100%), 
                url('https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1350&q=80');
    background-size: cover;
    padding: 100px 8%;
    border-radius: 40px;
    color: white;
    margin-top: 20px;
    text-align: center;
    transition: transform 0.3s ease;
}

.hero-section:hover { transform: translateY(-5px); }

.hero-section h1 { font-size: 55px; font-weight: 900; margin-bottom: 20px; }

/* Service Cards */
.service-card {
    background: white;
    padding: 40px 30px;
    border-radius: 25px;
    text-align: center;
    border-bottom: 5px solid transparent;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    height: 100%;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
}

.service-card:hover {
    transform: translateY(-15px);
    border-bottom: 5px solid var(--secondary);
    box-shadow: 0 25px 50px rgba(91,0,8,0.15);
}

.icon-box {
    font-size: 45px;
    color: var(--secondary);
    margin-bottom: 20px;
}

/* Form Styling */
div[data-testid="stForm"] {
    background: white;
    padding: 40px;
    border-radius: 30px;
    border: none;
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
}

/* Floating WhatsApp */
.float-wa {
    position: fixed;
    width: 65px;
    height: 65px;
    bottom: 40px;
    right: 40px;
    background-color: #25d366;
    color: #FFF !important;
    border-radius: 50px;
    text-align: center;
    font-size: 30px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# ================= NAVIGATION =================
st.markdown("""
<div class="navbar">
    <div class="logo-text"><i class="fas fa-satellite-dish"></i> Etisalat Business</div>
    <div style="color:white; font-weight:600;">
        <span style="margin-right:20px">الرئيسية</span>
        <span style="margin-right:20px">خدماتنا</span>
        <span>اتصل بنا</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero-section">
    <h1>مستقبل الاتصالات بين يديك</h1>
    <p style="font-size:22px; opacity:0.9;">نقدم حلولاً تكنولوجية متكاملة للشركات لضمان تواصل ذكي وآمن ومستمر</p>
    <br>
    <a href="#contact" style="background:white; color:#5b0008; padding:15px 40px; border-radius:50px; text-decoration:none; font-weight:bold; font-size:18px;">ابدأ الآن</a>
</div>
""", unsafe_allow_html=True)

# ================= SERVICES =================
st.markdown("<br><h2 style='text-align:center; color:#5b0008; font-weight:800;'>خدماتنا الاحترافية</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>حلول مصممة خصيصاً لتناسب احتياجات أعمالكم</p><br>", unsafe_allow_html=True)

serv_col1, serv_col2, serv_col3 = st.columns(3)

services = [
    {"icon": "fa-sim-card", "title": "خطوط الشركات", "desc": "إدارة كاملة لخطوط الموظفين باقات مرنة تناسب حجم استهلاك شركتك."},
    {"icon": "fa-wifi", "title": "إنترنت الأعمال", "desc": "سرعات فائقة وحلول ربط الفروع (Dedicated Internet) لضمان عدم الانقطاع."},
    {"icon": "fa-satellite", "title": "خدمات VSAT", "desc": "تغطية الأماكن النائية وحقول العمل عبر الأقمار الصناعية بأحدث التقنيات."}
]

for i, col in enumerate([serv_col1, serv_col2, serv_col3]):
    with col:
        st.markdown(f"""
        <div class="service-card">
            <div class="icon-box"><i class="fas {services[i]['icon']}"></i></div>
            <h3 style="color:#5b0008;">{services[i]['title']}</h3>
            <p style="color:#666;">{services[i]['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# ================= INTERACTIVE SECTION =================
st.markdown("<br><br>", unsafe_allow_html=True)
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("""
    <div style="background:var(--primary); color:white; padding:40px; border-radius:30px; height:100%;">
        <h2 style="color:white;">لماذا تختار اتصالات تليكوم؟</h2>
        <p style="font-size:18px; line-height:2;">
            <i class="fas fa-check-circle"></i> دعم فني متخصص على مدار الساعة<br>
            <i class="fas fa-check-circle"></i> أحدث البنية التحتية في الشرق الأوسط<br>
            <i class="fas fa-check-circle"></i> حلول مخصصة حسب ميزانية الشركة<br>
            <i class="fas fa-check-circle"></i> تقارير أداء وتحليل بيانات الاستهلاك
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    with st.form("contact_form"):
        st.markdown("<h3 id='contact' style='text-align:center; color:#5b0008;'>اطلب استشارة مجانية</h3>", unsafe_allow_html=True)
        name = st.text_input("اسم الشركة")
        email = st.text_input("البريد الإلكتروني")
        service_type = st.selectbox("نوع الخدمة المطلوبة", ["خطوط موبايل", "إنترنت فايبر", "أقمار صناعية"])
        msg = st.text_area("رسالتك")
        submit = st.form_submit_button("إرسال الطلب")
        if submit:
            st.success("تم استلام طلبك بنجاح، سيتواصل معك فريقنا قريباً!")

# ================= FOOTER =================
st.markdown(f"""
<a href="https://wa.me/20100000000" class="float-wa" target="_blank">
    <i class="fab fa-whatsapp"></i>
</a>
<div style="text-align:center; padding:40px; color:#999;">
    <hr style="border:0.1px solid #eee;">
    جميع الحقوق محفوظة لشركة اتصالات تليكوم © 2026
</div>
""", unsafe_allow_html=True)
