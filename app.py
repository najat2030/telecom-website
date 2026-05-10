import streamlit as st

st.set_page_config(
    page_title="Etisalat Telecom",
    page_icon="📡",
    layout="wide"
)

# ================= LANGUAGE =================
lang = st.sidebar.selectbox(
    "🌍 Language | اللغة",
    ["English", "العربية"]
)

is_ar = lang == "العربية"

# ================= TEXT =================
if is_ar:
    DIR = "rtl"

    nav_home = "الرئيسية"
    nav_services = "الخدمات"
    nav_solutions = "الحلول"
    nav_about = "من نحن"
    nav_contact = "تواصل معنا"

    hero_badge = "حلول اتصالات متطورة للشركات"
    hero_title = "حلول اتصالات احترافية\nلتطوير أعمالك"
    hero_desc = """
    نوفر حلول متكاملة للشركات تشمل خطوط الموبايل،
    الإنترنت، حلول VSAT، البنية التحتية الرقمية،
    وخدمات الاتصالات المؤسسية باحترافية عالية.
    """

    btn_offer = "اطلب عرض سعر"
    btn_services = "استكشف الخدمات"

    services_title = "خدماتنا"
    services_sub = "كل ما تحتاجه شركتك للبقاء متصلة وفعالة"

    cards = [
        ("📱", "خطوط الشركات", "إدارة خطوط الشركات والباقات والفواتير والدعم الفني."),
        ("🌐", "إنترنت الشركات", "حلول إنترنت ثابت وراوترات وشبكات احترافية."),
        ("🛰️", "خدمات VSAT", "ربط واتصالات عبر الأقمار الصناعية للمناطق النائية."),
        ("🏢", "البنية التحتية", "حلول شبكات وتحول رقمي للشركات."),
        ("📊", "إدارة الفواتير", "تقارير ومتابعة الفواتير والتحصيل والاستهلاك."),
        ("🛡️", "الأنظمة المتكاملة", "أنظمة مراقبة وربط وحلول تقنية متطورة.")
    ]

    solutions_title = "حلول متكاملة للشركات"
    solutions_desc = """
    نقدم باقات وخدمات مصممة خصيصًا للشركات
    لتحسين الأداء وتقليل التكلفة وزيادة الكفاءة التشغيلية.
    """

    about_title = "من نحن"
    about_desc = """
    اتصالات تليكوم شركة متخصصة في حلول الاتصالات
    وخدمات الشركات والبنية التحتية الرقمية وحلول الإنترنت
    والربط عبر الأقمار الصناعية.
    """

    contact_title = "ابدأ الآن"
    contact_desc = "تواصل معنا وسيقوم فريقنا بتجهيز أفضل الحلول لشركتك."

    call_btn = "اتصل الآن"
    whatsapp_btn = "واتساب"
    email_btn = "البريد الإلكتروني"

    footer = "اتصالات تليكوم © 2026 — نربط المستقبل"

else:
    DIR = "ltr"

    nav_home = "Home"
    nav_services = "Services"
    nav_solutions = "Solutions"
    nav_about = "About"
    nav_contact = "Contact"

    hero_badge = "Advanced Telecom Solutions"
    hero_title = "Powerful Telecom Solutions\nFor Modern Business"
    hero_desc = """
    We provide integrated telecom services including
    corporate lines, internet solutions, VSAT,
    digital infrastructure, and enterprise connectivity.
    """

    btn_offer = "Request Offer"
    btn_services = "Explore Services"

    services_title = "Our Services"
    services_sub = "Everything your business needs to stay connected"

    cards = [
        ("📱", "Corporate Lines", "Corporate mobile lines, bundles, billing and support."),
        ("🌐", "Business Internet", "Professional internet and connectivity solutions."),
        ("🛰️", "VSAT Solutions", "Satellite connectivity for remote operations."),
        ("🏢", "Infrastructure", "Networking and digital infrastructure services."),
        ("📊", "Billing Management", "Invoices, collections and reporting systems."),
        ("🛡️", "Integrated Systems", "Monitoring, surveillance and smart systems.")
    ]

    solutions_title = "Integrated Business Solutions"
    solutions_desc = """
    We deliver tailored telecom solutions for companies
    to improve operations and reduce communication costs.
    """

    about_title = "About Us"
    about_desc = """
    Etisalat Telecom is specialized in telecom solutions,
    corporate services, digital infrastructure,
    internet services and satellite connectivity.
    """

    contact_title = "Get Started Today"
    contact_desc = "Contact us and our team will prepare the right solution for your business."

    call_btn = "Call Now"
    whatsapp_btn = "WhatsApp"
    email_btn = "Email Us"

    footer = "Etisalat Telecom © 2026 — Connect The Future"

# ================= STYLE =================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800;900&display=swap');

html {{
    scroll-behavior: smooth;
}}

body, .stApp {{
    direction: {DIR};
}}

* {{
    font-family: 'Tajawal', 'Cairo', sans-serif;
    box-sizing: border-box;
}}

.stApp {{
    background: #fff7f5;
}}

#MainMenu, footer, header {{
    visibility: hidden;
}}

.block-container {{
    max-width: 1250px;
    padding-top: 25px;
}}

/* NAVBAR */
.navbar {{
    direction: ltr;
    background: #d90429;
    padding: 20px 38px;
    border-radius: 0 0 28px 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    box-shadow: 0 16px 35px rgba(217, 4, 41, .22);
}}

.logo {{
    font-size: 30px;
    font-weight: 900;
    color: white;
    letter-spacing: .3px;
}}

.nav-links {{
    display: flex;
    gap: 26px;
    align-items: center;
}}

.nav-links a {{
    color: white !important;
    text-decoration: none !important;
    font-size: 17px;
    font-weight: 800;
}}

.nav-links a:hover {{
    color: #ffe2e2 !important;
}}

/* HERO */
.hero {{
    margin-top: 28px;
    min-height: 620px;
    border-radius: 38px;
    padding: 85px 65px;
    color: white;
    background:
    linear-gradient(90deg, rgba(210,0,35,.92), rgba(255,35,60,.78)),
    url('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1800&q=80');
    background-size: cover;
    background-position: center;
    box-shadow: 0 25px 55px rgba(217, 4, 41, .24);
}}

.badge {{
    display: inline-block;
    background: rgba(255,255,255,.20);
    border: 1px solid rgba(255,255,255,.45);
    padding: 11px 24px;
    border-radius: 50px;
    font-weight: 800;
    margin-bottom: 25px;
}}

.hero h1 {{
    font-size: 64px;
    line-height: 1.18;
    font-weight: 900;
    max-width: 850px;
    margin-bottom: 25px;
    white-space: pre-line;
}}

.hero p {{
    font-size: 22px;
    line-height: 1.9;
    max-width: 780px;
}}

.btns a {{
    display: inline-block;
    margin-top: 25px;
    margin-inline-end: 14px;
    padding: 16px 34px;
    border-radius: 50px;
    text-decoration: none !important;
    font-weight: 900;
    font-size: 17px;
}}

.btn-main {{
    background: white;
    color: #d90429 !important;
}}

.btn-outline {{
    border: 2px solid white;
    color: white !important;
}}

/* TITLES */
.title {{
    text-align: center;
    color: #d90429;
    font-size: 44px;
    font-weight: 900;
    margin-top: 75px;
}}

.subtitle {{
    text-align: center;
    color: #666;
    font-size: 19px;
    margin-bottom: 40px;
}}

/* CARDS */
.card {{
    background: white;
    border-radius: 30px;
    padding: 34px;
    min-height: 280px;
    border: 1px solid #ffd6dc;
    box-shadow: 0 16px 38px rgba(217, 4, 41, .10);
    transition: .25s;
    text-align: center;
    margin-bottom: 25px;
}}

.card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 24px 55px rgba(217, 4, 41, .18);
}}

.icon {{
    width: 66px;
    height: 66px;
    margin: 0 auto 20px auto;
    background: #d90429;
    color: white;
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
}}

.card h3 {{
    color: #d90429;
    font-size: 25px;
    font-weight: 900;
}}

.card p {{
    color: #555;
    line-height: 1.9;
    font-size: 17px;
}}

/* OFFER */
.offer {{
    margin-top: 70px;
    background: linear-gradient(120deg, #d90429, #ff304f);
    color: white;
    border-radius: 38px;
    padding: 58px;
    box-shadow: 0 22px 48px rgba(217, 4, 41, .25);
}}

.offer h2 {{
    font-size: 44px;
    font-weight: 900;
}}

.offer p {{
    font-size: 21px;
    line-height: 1.9;
}}

/* CONTACT */
.contact {{
    background: white;
    border-radius: 34px;
    padding: 50px;
    text-align: center;
    box-shadow: 0 18px 42px rgba(217, 4, 41, .10);
    border: 1px solid #ffd6dc;
}}

.contact h2 {{
    color: #d90429;
    font-weight: 900;
    font-size: 38px;
}}

.contact p {{
    color: #666;
    font-size: 18px;
    line-height: 1.9;
}}

.contact-buttons {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 25px;
}}

.contact-buttons a {{
    display: inline-flex;
    justify-content: center;
    align-items: center;
    min-width: 170px;
    padding: 16px 30px;
    background: #d90429;
    color: white !important;
    text-decoration: none !important;
    border-radius: 50px;
    font-weight: 900;
    font-size: 17px;
    box-shadow: 0 12px 26px rgba(217, 4, 41, .25);
}}

.contact-buttons a:hover {{
    background: #ff304f;
}}

/* FLOATING WHATSAPP */
.whatsapp {{
    position: fixed;
    bottom: 25px;
    right: 25px;
    width: 72px;
    height: 72px;
    border-radius: 50%;
    background: #d90429;
    color: white !important;
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none !important;
    font-size: 32px;
    box-shadow: 0 14px 32px rgba(217, 4, 41, .35);
    z-index: 99999;
}}

.footer {{
    text-align: center;
    padding: 30px;
    color: #d90429;
    font-weight: 900;
    margin-top: 60px;
}}

/* MOBILE */
@media(max-width: 850px) {{
    .navbar {{
        flex-direction: column;
        gap: 15px;
        text-align: center;
    }}

    .nav-links {{
        flex-wrap: wrap;
        justify-content: center;
        gap: 14px;
    }}

    .hero {{
        padding: 50px 30px;
        min-height: 520px;
    }}

    .hero h1 {{
        font-size: 40px;
    }}

    .hero p {{
        font-size: 18px;
    }}

    .title {{
        font-size: 34px;
    }}
}}
</style>
""", unsafe_allow_html=True)

# ================= NAV =================
st.markdown(f"""
<div class="navbar">
    <div class="logo">Etisalat Telecom</div>

    <div class="nav-links">
        <a href="#home">{nav_home}</a>
        <a href="#services">{nav_services}</a>
        <a href="#solutions">{nav_solutions}</a>
        <a href="#about">{nav_about}</a>
        <a href="#contact">{nav_contact}</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown(f"""
<div class="hero" id="home">

    <div class="badge">{hero_badge}</div>

    <h1>{hero_title}</h1>

    <p>{hero_desc}</p>

    <div class="btns">
        <a class="btn-main" href="https://wa.me/201000000000" target="_blank">{btn_offer}</a>
        <a class="btn-outline" href="#services">{btn_services}</a>
    </div>

</div>
""", unsafe_allow_html=True)

# ================= SERVICES =================
st.markdown(f'<div class="title" id="services">{services_title}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">{services_sub}</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, card in enumerate(cards[:3]):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <div class="icon">{card[0]}</div>
            <h3>{card[1]}</h3>
            <p>{card[2]}</p>
        </div>
        """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
cols2 = [col4, col5, col6]

for i, card in enumerate(cards[3:]):
    with cols2[i]:
        st.markdown(f"""
        <div class="card">
            <div class="icon">{card[0]}</div>
            <h3>{card[1]}</h3>
            <p>{card[2]}</p>
        </div>
        """, unsafe_allow_html=True)

# ================= SOLUTIONS =================
st.markdown(f"""
<div class="offer" id="solutions">

    <h2>{solutions_title}</h2>

    <p>{solutions_desc}</p>

</div>
""", unsafe_allow_html=True)

# ================= ABOUT =================
st.markdown(f'<div class="title" id="about">{about_title}</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="contact">
    <p>
        {about_desc}
    </p>
</div>
""", unsafe_allow_html=True)

# ================= CONTACT =================
st.markdown(f'<div class="title" id="contact">{nav_contact}</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="contact">

    <h2>{contact_title}</h2>

    <p>{contact_desc}</p>

    <div class="contact-buttons">
        <a href="tel:01000000000">☎ {call_btn}</a>
        <a href="https://wa.me/201000000000" target="_blank">💬 {whatsapp_btn}</a>
        <a href="mailto:info@etisalattelecom.net">✉ {email_btn}</a>
    </div>

</div>
""", unsafe_allow_html=True)

# ================= FLOAT =================
st.markdown("""
<a class="whatsapp" href="https://wa.me/201000000000" target="_blank">
☎
</a>
""", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown(f"""
<div class="footer">
{footer}
</div>
""", unsafe_allow_html=True)
