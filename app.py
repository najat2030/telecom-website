import streamlit as st

st.set_page_config(
    page_title="Etisalat Telecom",
    page_icon="📡",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap');

* {font-family:'Cairo',sans-serif;}
html {scroll-behavior:smooth;}
.stApp {background:#fff8f5;}
#MainMenu, footer, header {visibility:hidden;}
.block-container {padding-top:25px; max-width:1200px;}

/* NAV */
.navbar {
    position:sticky; top:0; z-index:999;
    background:rgba(90,0,10,.96);
    padding:18px 35px;
    border-radius:0 0 26px 26px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 15px 35px rgba(90,0,10,.25);
}
.logo {font-size:28px;font-weight:900;color:white;}
.navbar a {
    color:white!important;
    text-decoration:none;
    margin-left:26px;
    font-weight:700;
}
.navbar a:hover {color:#ffd7d7!important;}

/* HERO */
.hero {
    margin-top:30px;
    min-height:620px;
    border-radius:36px;
    padding:80px 60px;
    color:white;
    background:
    linear-gradient(90deg,rgba(70,0,8,.96),rgba(145,0,20,.84),rgba(40,0,5,.65)),
    url('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1800&q=80');
    background-size:cover;
    background-position:center;
    box-shadow:0 25px 55px rgba(90,0,10,.28);
}
.badge {
    display:inline-block;
    background:rgba(255,255,255,.16);
    border:1px solid rgba(255,255,255,.35);
    padding:10px 20px;
    border-radius:50px;
    font-weight:700;
    margin-bottom:25px;
}
.hero h1 {
    font-size:64px;
    line-height:1.18;
    font-weight:900;
    max-width:820px;
    margin-bottom:25px;
}
.hero p {
    font-size:22px;
    line-height:1.9;
    max-width:760px;
}
.btn-main, .btn-outline {
    display:inline-block;
    margin-top:32px;
    margin-right:14px;
    padding:16px 34px;
    border-radius:50px;
    font-size:17px;
    font-weight:900;
    text-decoration:none!important;
}
.btn-main {
    background:white;
    color:#7a0010!important;
}
.btn-outline {
    border:2px solid white;
    color:white!important;
}
.btn-main:hover, .btn-outline:hover {
    transform:translateY(-3px);
}

/* STATS */
.stats {
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:18px;
    margin-top:-60px;
    padding:0 40px;
}
.stat {
    background:white;
    border-radius:24px;
    padding:28px;
    text-align:center;
    box-shadow:0 15px 35px rgba(90,0,10,.13);
}
.stat h2 {color:#7a0010;font-size:34px;margin:0;font-weight:900;}
.stat p {color:#555;margin:5px 0 0;font-weight:700;}

/* SECTION */
.title {
    text-align:center;
    color:#5b0008;
    font-size:42px;
    font-weight:900;
    margin-top:80px;
}
.subtitle {
    text-align:center;
    color:#666;
    font-size:18px;
    margin-bottom:35px;
}

/* CARDS */
.card {
    background:white;
    border-radius:28px;
    padding:34px;
    min-height:285px;
    border:1px solid #f2d5d8;
    box-shadow:0 18px 38px rgba(90,0,10,.10);
    transition:.25s;
}
.card:hover {
    transform:translateY(-8px);
    box-shadow:0 28px 55px rgba(90,0,10,.18);
}
.icon {
    width:58px;height:58px;
    background:#7a0010;
    color:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:28px;
    margin-bottom:18px;
}
.card h3 {color:#7a0010;font-size:24px;font-weight:900;}
.card p {color:#555;line-height:1.8;font-size:16px;}

/* OFFER */
.offer {
    margin-top:70px;
    background:linear-gradient(120deg,#5b0008,#a40018);
    color:white;
    border-radius:34px;
    padding:55px;
    box-shadow:0 20px 45px rgba(90,0,10,.24);
}
.offer h2 {font-size:42px;font-weight:900;}
.offer p {font-size:20px;line-height:1.8;max-width:850px;}

/* CONTACT */
.contact {
    background:white;
    border-radius:30px;
    padding:45px;
    text-align:center;
    box-shadow:0 16px 40px rgba(90,0,10,.12);
    border:1px solid #f1d5d8;
}
.contact h2 {color:#5b0008;font-weight:900;}
.contact a {
    display:inline-block;
    margin:10px;
    padding:15px 32px;
    border-radius:45px;
    background:#7a0010;
    color:white!important;
    text-decoration:none!important;
    font-weight:900;
}

/* WHATSAPP */
.whatsapp {
    position:fixed;
    right:24px;
    bottom:24px;
    width:72px;
    height:72px;
    border-radius:50%;
    background:#7a0010;
    color:white!important;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:34px;
    text-decoration:none!important;
    box-shadow:0 14px 32px rgba(90,0,10,.35);
    z-index:99999;
}
.footer {
    text-align:center;
    margin-top:60px;
    padding:25px;
    color:#7a0010;
    font-weight:800;
}

/* MOBILE */
@media(max-width:800px){
    .hero h1 {font-size:40px;}
    .hero {padding:45px 28px;}
    .stats {grid-template-columns:repeat(2,1fr); padding:0; margin-top:25px;}
    .navbar {display:block;text-align:center;}
    .navbar a {display:inline-block;margin:8px;}
}
</style>
""", unsafe_allow_html=True)

# NAVBAR
st.markdown("""
<div class="navbar">
    <div class="logo">Etisalat Telecom</div>
    <div>
        <a href="#home">Home</a>
        <a href="#services">Services</a>
        <a href="#solutions">Solutions</a>
        <a href="#about">About Us</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero" id="home">
    <div class="badge">Royal Telecom Identity | Business Solutions</div>
    <h1>Powerful Telecom Solutions For Growing Businesses</h1>
    <p>
        We help companies manage corporate lines, internet connectivity, VSAT satellite services,
        digital infrastructure, and smart business communication with professional support.
    </p>
    <a class="btn-main" href="https://wa.me/201000000000" target="_blank">Request Business Offer</a>
    <a class="btn-outline" href="#services">Explore Services</a>
</div>
""", unsafe_allow_html=True)

# STATS
st.markdown("""
<div class="stats">
    <div class="stat"><h2>24/7</h2><p>Business Support</p></div>
    <div class="stat"><h2>5G</h2><p>Modern Connectivity</p></div>
    <div class="stat"><h2>VSAT</h2><p>Remote Coverage</p></div>
    <div class="stat"><h2>B2B</h2><p>Corporate Solutions</p></div>
</div>
""", unsafe_allow_html=True)

# SERVICES
st.markdown('<div class="title" id="services">Our Services</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Everything your business needs to stay connected and protected</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <div class="icon">📱</div>
        <h3>Corporate Mobile Lines</h3>
        <p>Corporate lines, business bundles, account management, billing follow-up, and migration support.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <div class="icon">🌐</div>
        <h3>Business Internet</h3>
        <p>Fixed internet, business routers, backup connectivity, and stable data solutions for offices.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <div class="icon">🛰️</div>
        <h3>VSAT Satellite Solutions</h3>
        <p>Satellite communication for remote areas, mines, quarries, construction sites, and critical operations.</p>
    </div>
    """, unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""
    <div class="card">
        <div class="icon">🏢</div>
        <h3>Enterprise Connectivity</h3>
        <p>Integrated connectivity solutions designed for companies, branches, warehouses, and operations teams.</p>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="card">
        <div class="icon">📊</div>
        <h3>Billing & Reporting</h3>
        <p>Clear follow-up for invoices, payments, collections, usage reports, and corporate account visibility.</p>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="card">
        <div class="icon">🛡️</div>
        <h3>Integrated Systems</h3>
        <p>Surveillance, smart monitoring, networking, and digital infrastructure for professional environments.</p>
    </div>
    """, unsafe_allow_html=True)

# SOLUTIONS
st.markdown("""
<div class="offer" id="solutions">
    <h2>Ready-Made Telecom Packages For Companies</h2>
    <p>
        Whether you are a small business, factory, retail chain, construction company, or remote site operator,
        Etisalat Telecom provides tailored solutions to reduce communication cost, improve control,
        and keep your teams connected everywhere.
    </p>
    <a class="btn-main" href="https://wa.me/201000000000" target="_blank">Get Free Consultation</a>
</div>
""", unsafe_allow_html=True)

# ABOUT
st.markdown('<div class="title" id="about">About Etisalat Telecom</div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact">
    <h2>Connecting Businesses With Smarter Telecom Operations</h2>
    <p style="color:#555;font-size:18px;line-height:1.9;">
        Etisalat Telecom is focused on delivering professional telecom and connectivity services
        for business clients. Our work covers corporate mobile lines, internet solutions,
        satellite communication, digital infrastructure, account operations, and continuous support.
    </p>
</div>
""", unsafe_allow_html=True)

# CONTACT
st.markdown('<div class="title" id="contact">Contact Us</div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact">
    <h2>Let’s Build Your Business Connectivity Plan</h2>
    <p style="color:#555;font-size:18px;">Contact us now and our team will prepare the right solution for your company.</p>
    <a href="tel:01000000000">Call Now</a>
    <a href="https://wa.me/201000000000" target="_blank">WhatsApp</a>
    <a href="mailto:info@etisalattelecom.net">Email Us</a>
</div>
""", unsafe_allow_html=True)

# FLOATING WHATSAPP
st.markdown("""
<a class="whatsapp" href="https://wa.me/201000000000" target="_blank">☎</a>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Etisalat Telecom © 2026 — Connect The Future
</div>
""", unsafe_allow_html=True)
