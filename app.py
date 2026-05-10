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
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {{
    direction:{DIR};
}}

* {{
    font-family:'Cairo',sans-serif;
}}

.stApp {{
    background:#fff8f6;
}}

#MainMenu, footer, header {{
    visibility:hidden;
}}

.block-container {{
    max-width:1200px;
    padding-top:20px;
}}

.navbar {{
    background:#70000d;
    padding:18px 35px;
    border-radius:0 0 24px 24px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    color:white;
    box-shadow:0 12px 30px rgba(112,0,13,.2);
}}

.logo {{
    font-size:28px;
    font-weight:900;
}}

.nav-links span {{
    margin:0 15px;
    font-weight:700;
}}

.hero {{
    margin-top:25px;
    min-height:600px;
    border-radius:35px;
    padding:80px 60px;
    color:white;
    background:
    linear-gradient(rgba(70,0,8,.85), rgba(140,0,20,.78)),
    url('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1800&q=80');

    background-size:cover;
    background-position:center;
}}

.badge {{
    display:inline-block;
    padding:10px 22px;
    border-radius:40px;
    background:rgba(255,255,255,.15);
    margin-bottom:25px;
    font-weight:700;
}}

.hero h1 {{
    font-size:62px;
    font-weight:900;
    line-height:1.2;
}}

.hero p {{
    font-size:22px;
    line-height:1.9;
    max-width:760px;
}}

.btns a {{
    display:inline-block;
    margin-top:25px;
    margin-right:14px;
    padding:15px 30px;
    border-radius:50px;
    text-decoration:none;
    font-weight:800;
}}

.btn-main {{
    background:white;
    color:#70000d;
}}

.btn-outline {{
    border:2px solid white;
    color:white;
}}

.title {{
    text-align:center;
    color:#70000d;
    font-size:40px;
    font-weight:900;
    margin-top:70px;
}}

.subtitle {{
    text-align:center;
    color:#666;
    margin-bottom:40px;
}}

.card {{
    background:white;
    border-radius:28px;
    padding:32px;
    min-height:270px;
    border:1px solid #f2d5d8;
    box-shadow:0 15px 35px rgba(112,0,13,.10);
    transition:.3s;
}}

.card:hover {{
    transform:translateY(-8px);
}}

.icon {{
    font-size:40px;
}}

.card h3 {{
    color:#70000d;
    font-size:24px;
    font-weight:900;
}}

.card p {{
    color:#555;
    line-height:1.9;
}}

.offer {{
    margin-top:70px;
    background:linear-gradient(120deg,#70000d,#b10019);
    color:white;
    border-radius:35px;
    padding:55px;
}}

.offer h2 {{
    font-size:42px;
    font-weight:900;
}}

.offer p {{
    font-size:20px;
    line-height:1.9;
}}

.contact {{
    background:white;
    border-radius:30px;
    padding:45px;
    text-align:center;
    box-shadow:0 15px 35px rgba(112,0,13,.10);
}}

.contact h2 {{
    color:#70000d;
    font-weight:900;
}}

.contact a {{
    display:inline-block;
    margin:10px;
    padding:15px 28px;
    background:#70000d;
    color:white!important;
    text-decoration:none;
    border-radius:50px;
    font-weight:800;
}}

.whatsapp {{
    position:fixed;
    bottom:25px;
    right:25px;
    width:72px;
    height:72px;
    border-radius:50%;
    background:#70000d;
    color:white!important;
    display:flex;
    justify-content:center;
    align-items:center;
    text-decoration:none;
    font-size:32px;
    box-shadow:0 12px 30px rgba(112,0,13,.3);
}}

.footer {{
    text-align:center;
    padding:30px;
    color:#70000d;
    font-weight:800;
    margin-top:60px;
}}
</style>
""", unsafe_allow_html=True)

# ================= NAV =================
st.markdown(f"""
<div class="navbar">
    <div class="logo">Etisalat Telecom</div>

    <div class="nav-links">
        <span>{nav_home}</span>
        <span>{nav_services}</span>
        <span>{nav_solutions}</span>
        <span>{nav_about}</span>
        <span>{nav_contact}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown(f"""
<div class="hero">

<div class="badge">{hero_badge}</div>

<h1>{hero_title}</h1>

<p>{hero_desc}</p>

<div class="btns">
    <a class="btn-main" href="https://wa.me/201000000000" target="_blank">{btn_offer}</a>

    <a class="btn-outline" href="#">{btn_services}</a>
</div>

</div>
""", unsafe_allow_html=True)

# ================= SERVICES =================
st.markdown(f'<div class="title">{services_title}</div>', unsafe_allow_html=True)
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
<div class="offer">

<h2>{solutions_title}</h2>

<p>{solutions_desc}</p>

</div>
""", unsafe_allow_html=True)

# ================= ABOUT =================
st.markdown(f'<div class="title">{about_title}</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="contact">
<p style="font-size:20px;line-height:1.9;color:#555;">
{about_desc}
</p>
</div>
""", unsafe_allow_html=True)

# ================= CONTACT =================
st.markdown(f'<div class="title">{nav_contact}</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="contact">

<h2>{contact_title}</h2>

<p style="color:#666;font-size:18px;">
{contact_desc}
</p>

<a href="tel:01000000000">{call_btn}</a>

<a href="https://wa.me/201000000000" target="_blank">
{whatsapp_btn}
</a>

<a href="mailto:info@etisalattelecom.net">
{email_btn}
</a>

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
