import streamlit as st

st.set_page_config(
    page_title="Etisalat Business",
    page_icon="📡",
    layout="wide"
)

# ================= CSS UPGRADE (Pure Red Style) =================
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

/* الألوان الأساسية - أحمر اتصالات */
:root {
    --etisalat-red: #FF0000;
    --dark-red: #D00000;
    --bg-light: #fdfdfd;
}

* { font-family: 'Cairo', sans-serif; direction: rtl; }

.stApp { background-color: var(--bg-light); }

/* إخفاء زوائد ستريمليت */
#MainMenu, footer, header { visibility: hidden; }

/* الهيدر (Navbar) */
.navbar {
    background: var(--etisalat-red);
    padding: 15px 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 0 0 20px 20px;
    box-shadow: 0 4px 15px rgba(255,0,0,0.2);
}

.logo-text { font-size: 24px; font-weight: 900; color: white; }

/* قسم البطولة (Hero) */
.hero-section {
    background: linear-gradient(45deg, #FF0000, #BB0000);
    padding: 80px 5%;
    border-radius: 30px;
    color: white;
    text-align: center;
    margin-top: 20px;
}

.hero-section h1 { font-size: 45px; font-weight: 900; margin-bottom: 10px; }

/* كروت الخدمات */
.service-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    transition: 0.3s;
    border: 1px solid #eee;
    height: 100%;
}

.service-card:hover {
    transform: translateY(-10px);
    border-color: var(--etisalat-red);
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
}

.icon-box {
    font-size: 40px;
    color: var(--etisalat-red);
    margin-bottom: 15px;
}

/* زر التواصل */
.cta-btn {
    background: white;
    color: var(--etisalat-red);
    padding: 12px 35px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    display: inline-block;
    margin-top: 20px;
}

/* زر الواتساب الطائر */
.float-wa {
    position: fixed;
    width: 60px;
    height: 60px;
    bottom: 30px;
    left: 30px; /* جهة اليسار لأن الموقع عربي */
    background-color: #25d366;
    color: white !important;
    border-radius: 50px;
    text-align: center;
    font-size: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# ================= الهيكل (Layout) =================

# 1. القائمة العلوية
st.markdown("""
<div class="navbar">
    <div class="logo-text">Etisalat Business</div>
    <div style="color:white; font-weight:600;">
        <span style="margin-left:20px">الرئيسية</span>
        <span style="margin-left:20px">الخدمات</span>
        <span>اتصل بنا</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. قسم الترحيب
st.markdown("""
<div class="hero-section">
    <h1>اتصالات للأعمال</h1>
    <p style="font-size:20px;">الحلول التكنولوجية الأقوى لنمو شركتك في مصر</p>
    <a href="#contact" class="cta-btn">تواصل معنا الآن</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 3. الخدمات
st.markdown("<h2 style='text-align:center; color:#333;'>خدماتنا</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <div class="icon-box"><i class="fas fa-sim-card"></i></div>
        <h3>باقات الموبايل</h3>
        <p>أنظمة تحكم مرنة لخطوط الموظفين وتوفير في الفواتير.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div class="icon-box"><i class="fas fa-network-wired"></i></div>
        <h3>إنترنت الفايبر</h3>
        <p>سرعات ثابتة وعالية جداً مخصصة للشركات فقط.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <div class="icon-box"><i class="fas fa-cloud"></i></div>
        <h3>الحلول السحابية</h3>
        <p>استضافة بياناتك وتأمينها بأحدث المعايير العالمية.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 4. نموذج التواصل (تفاعلي)
st.markdown("<h2 id='contact' style='text-align:center;'>اطلب الخدمة</h2>", unsafe_allow_html=True)
with st.container():
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        with st.form("my_form"):
            name = st.text_input("الاسم أو اسم الشركة")
            phone = st.text_input("رقم الهاتف")
            service = st.selectbox("الخدمة المهتم بها", ["إنترنت شركات", "خطوط موبايل", "حلول ذكية"])
            submitted = st.form_submit_button("إرسال البيانات")
            if submitted:
                st.success("تم الإرسال! سنتصل بك خلال دقائق.")

# 5. الفوتر والواتساب
st.markdown("""
<a href="https://wa.me/20100000000" class="float-wa" target="_blank">
    <i class="fab fa-whatsapp"></i>
</a>
<div style="text-align:center; padding:30px; color:#777; margin-top:50px;">
    جميع الحقوق محفوظة - اتصالات تليكوم 2026 ©
</div>
""", unsafe_allow_html=True)
