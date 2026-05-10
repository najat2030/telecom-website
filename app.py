import streamlit as st

st.set_page_config(
    page_title="Etisalat Telecom",
    page_icon="📡",
    layout="wide"
)

# ================= HELPER =================
def html(code):
    st.markdown(code, unsafe_allow_html=True)

# ================= LANGUAGE =================
lang = st.sidebar.selectbox("🌍 Language | اللغة", ["English", "العربية"])
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
    hero_title = "حلول اتصالات احترافية لتطوير أعمالك"
    hero_desc = "نوفر حلول متكاملة للشركات تشمل خطوط الموبايل، الإنترنت، حلول VSAT، البنية التحتية الرقمية، وخدمات الاتصالات المؤسسية باحترافية عالية."

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
    solutions_desc = "نقدم باقات وخدمات مصممة خصيصًا للشركات لتحسين الأداء وتقليل التكلفة وزيادة الكفاءة التشغيلية."

    about_title = "من نحن"
    about_desc = "اتصالات تليكوم شركة متخصصة في حلول الاتصالات وخدمات الشركات والبنية التحتية الرقمية وحلول الإنترنت والربط عبر الأقمار الصناعية."

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
    nav_about = "About Us"
    nav_contact = "Contact"

    hero_badge = "Advanced Telecom Solutions"
    hero_title = "Powerful Telecom Solutions For Modern Business"
    hero_desc = "We provide integrated telecom services including corporate lines, internet solutions, VSAT, digital infrastructure, and enterprise connectivity."

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
    solutions_desc = "We deliver tailored telecom solutions for companies to improve operations and reduce communication costs."

    about_title = "About Us"
    about_desc = "Etisalat Telecom is specialized in telecom solutions, corporate services, digital infrastructure, internet services and satellite connectivity."

    contact_title = "Get Started Today"
    contact_desc = "Contact us and our team will prepare the right solution for your business."

    call_btn = "Call Now"
    whatsapp_btn = "WhatsApp"
    email_btn = "Email Us"

    footer = "Etisalat Telecom © 2026 — Connect The Future"

# ================= STYLE =================
html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;500;600;700;800;900&display=swap');

html {{
    scroll-behavior: smooth;
}}

* {{
    font-family: 'Alexandria', sans-serif;
    box-sizing: border-box;
}}

.stApp {{
    background: #fff7f5;
    direction: {DIR};
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
    background: linear-gradient(120deg, #ff003c, #ff315c);
    padding: 22px 40px;
    border-radius: 0 0 32px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    box-shadow: 0 20px 45px rgba(255, 0, 60, .25);
}}

.logo {{
    font-size: 30px;
    font-weight: 900;
    color: white;
}}

.nav-links {{
    display: flex;
    gap: 28px;
    align-items: center;
}}

.nav-links a {{
    color: white !important;
    text-decoration: none !important;
    font-size: 16px;
    font-weight: 700;
}}

.nav-links a:hover {{
    color: #ffe2e7 !important;
}}

/* HERO */
.hero {{
    margin-top: 30px;
    min-height: 610px;
    border-radius: 42px;
    padding: 90px 70px;
    color: white;
    background:
        linear-gradient(90deg, rgba(255,0,60,.94), rgba(255,49,92,.82)),
        url('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1800&q=80');
    background-size: cover;
    background-position: center;
    box-shadow: 0 28px 60px rgba(255, 0, 60, .23);
}}

.badge {{
    display: inline-block;
    background: rgba(255,255,255,.20);
    border: 1px solid rgba(255,255,255,.45);
    padding: 12px 24px;
    border-radius: 50px;
    font-weight: 700;
    margin-bottom: 28px;
}}

.hero h1 {{
    font-size: 62px;
    line-height: 1.25;
    font-weight: 900;
    max-width: 850px;
    margin: 0 0 25px 0;
}}

.hero p {{
    font-size: 21px;
    line-height: 1.9;
    max-width: 790px;
    margin-bottom: 35px;
}}

.btns {{
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}}

.btns a {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 180px;
    padding: 16px 32px;
    border-radius: 50px;
    text-decoration: none !important;
    font-weight: 800;
    font-size: 16px;
}}

.btn-main {{
    background: white;
    color: #ff003c !important;
}}

.btn-outline {{
    border: 2px solid white;
    color: white !important;
}}

/* TITLES */
.title {{
    text-align: center;
    color: #ff003c;
    font-size: 44px;
    font-weight: 900;
    margin-top: 80px;
    margin-bottom: 12px;
}}

.subtitle {{
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 42px;
}}

/* CARDS */
.card {{
    background: white;
    border-radius: 30px;
    padding: 34px;
    min-height: 285px;
    border: 1px solid #ffd5dd;
    box-shadow: 0 18px 42px rgba(255, 0, 60, .10);
    transition: .25s;
    text-align: center;
    margin-bottom: 25px;
}}

.card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 26px 55px rgba(255, 0, 60, .18);
}}

.icon {{
    width: 70px;
    height: 70px;
    margin: 0 auto 20px auto;
    background: linear-gradient(120deg, #ff003c, #ff315c);
    color: white;
    border-radius: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
}}

.card h3 {{
    color: #ff003c;
    font-size: 23px;
    font-weight: 900;
    margin-bottom: 14px;
}}

.card p {{
    color: #555;
    line-height: 1.9;
    font-size: 16px;
}}

/* OFFER */
.offer {{
    margin-top: 70px;
    background: linear-gradient(120deg, #ff003c, #ff315c);
    color: white;
    border-radius: 42px;
    padding: 60px;
    box-shadow: 0 25px 55px rgba(255, 0, 60, .25);
}}

.offer h2 {{
    font-size: 42px;
    font-weight: 900;
    margin-bottom: 20px;
}}

.offer p {{
    font-size: 20px;
    line-height: 1.9;
}}

/* CONTACT / ABOUT */
.info-box {{
    background: white;
    border-radius: 34px;
    padding: 50px;
    text-align: center;
    box-shadow: 0 18px 42px rgba(255, 0, 60, .10);
    border: 1px solid #ffd5dd;
}}

.info-box h2 {{
    color: #ff003c;
    font-weight: 900;
    font-size: 36px;
    margin-bottom: 18px;
}}

.info-box p {{
    color: #555;
    font-size: 18px;
    line-height: 1.9;
    max-width: 850px;
    margin: auto;
}}

.contact-buttons {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 30px;
}}

.contact-buttons a {{
    display: inline-flex;
    justify-content: center;
    align-items: center;
    min-width: 170px;
    padding: 16px 30px;
    background: linear-gradient(120deg, #ff003c, #ff315c);
    color: white !important;
    text-decoration: none !important;
    border-radius: 50px;
    font-weight: 800;
    font-size: 16px;
    box-shadow: 0 14px 28px rgba(255, 0, 60, .25);
}}

/* FLOATING */
.whatsapp {{
    position: fixed;
    bottom: 25px;
    right: 25px;
    width: 72px;
    height: 72px;
    border-radius: 50%;
    background: linear-gradient(120deg, #ff003c, #ff315c);
    color: white !important;
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none !important;
    font-size: 32px;
    box-shadow: 0 14px 32px rgba(255, 0, 60, .35);
    z-index: 99999;
}}

.footer {{
    text-align: center;
    padding: 35px;
    color: #ff003c;
    font-weight: 800;
    margin-top: 60px;
}}

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
        font-size: 38px;
    }}

    .hero p {{
        font-size: 17px;
    }}

    .title {{
        font-size: 34px;
    }}
}}
</style>
""")

# ================= NAV =================
html(f"""
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
""")

# ================= HERO =================
html(f"""
<section class="hero" id="home">
    <div class="badge">{hero_badge}</div>
    <h1>{hero_title}</h1>
    <p>{hero_desc}</p>
    <div class="btns">
        <a class="btn-main" href="https://wa.me/201000000000" target="_blank">{btn_offer}</a>
        <a class="btn-outline" href="#services">{btn_services}</a>
    </div>
</section>
""")

# ================= SERVICES =================
html(f"""
<div class="title" id="services">{services_title}</div>
<div class="subtitle">{services_sub}</div>
""")

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, card in enumerate(cards[:3]):
    with cols[i]:
        html(f"""
        <div class="card">
            <div class="icon">{card[0]}</div>
            <h3>{card[1]}</h3>
            <p>{card[2]}</p>
        </div>
        """)

col4, col5, col6 = st.columns(3)
cols2 = [col4, col5, col6]

for i, card in enumerate(cards[3:]):
    with cols2[i]:
        html(f"""
        <div class="card">
            <div class="icon">{card[0]}</div>
            <h3>{card[1]}</h3>
            <p>{card[2]}</p>
        </div>
        """)

# ================= SOLUTIONS =================
html(f"""
<section class="offer" id="solutions">
    <h2>{solutions_title}</h2>
    <p>{solutions_desc}</p>
</section>
""")

# ================= ABOUT =================
html(f"""
<div class="title" id="about">{about_title}</div>
<section class="info-box">
    <p>{about_desc}</p>
</section>
""")

# ================= CONTACT =================
html(f"""
<div class="title" id="contact">{nav_contact}</div>
<section class="info-box">
    <h2>{contact_title}</h2>
    <p>{contact_desc}</p>
    <div class="contact-buttons">
        <a href="tel:01000000000">☎ {call_btn}</a>
        <a href="https://wa.me/201000000000" target="_blank">💬 {whatsapp_btn}</a>
        <a href="mailto:info@etisalattelecom.net">✉ {email_btn}</a>
    </div>
</section>
""")

# ================= FLOAT =================
html("""
<a class="whatsapp" href="https://wa.me/201000000000" target="_blank">☎</a>
""")

# ================= FOOTER =================
html(f"""
<div class="footer">{footer}</div>
""")
