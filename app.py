import streamlit as st

st.set_page_config(
    page_title="Etisalat Telecom",
    page_icon="📡",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

* {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    background: #fffaf7;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* Navbar */
.navbar {
    background: #5b0008;
    padding: 18px 45px;
    border-radius: 0 0 24px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    box-shadow: 0 8px 25px rgba(91,0,8,0.25);
}

.logo {
    font-size: 28px;
    font-weight: 800;
    color: #fff;
}

.nav-links span {
    margin-left: 28px;
    font-size: 16px;
    font-weight: 600;
}

/* Hero */
.hero {
    margin-top: 25px;
    min-height: 560px;
    border-radius: 32px;
    background: linear-gradient(120deg, rgba(91,0,8,0.95), rgba(155,0,18,0.88)),
                url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3');
    background-size: cover;
    background-position: center;
    color: white;
    padding: 90px 70px;
    box-shadow: 0 20px 45px rgba(91,0,8,0.25);
}

.hero h1 {
    font-size: 58px;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 25px;
}

.hero p {
    font-size: 23px;
    max-width: 720px;
    line-height: 1.8;
}

.hero-btn {
    display: inline-block;
    margin-top: 35px;
    padding: 16px 36px;
    background: white;
    color: #7a0010;
    border-radius: 50px;
    font-weight: 800;
    text-decoration: none;
    font-size: 18px;
}

/* Sections */
.section-title {
    text-align: center;
    color: #5b0008;
    font-size: 38px;
    font-weight: 800;
    margin-top: 70px;
    margin-bottom: 15px;
}

.section-subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
    margin-bottom: 45px;
}

/* Cards */
.card {
    background: white;
    border-radius: 26px;
    padding: 32px;
    min-height: 260px;
    box-shadow: 0 12px 30px rgba(91,0,8,0.12);
    border: 1px solid #f1d7d9;
}

.card h3 {
    color: #7a0010;
    font-size: 24px;
    font-weight: 800;
}

.card p {
    color: #555;
    font-size: 16px;
    line-height: 1.8;
}

/* About */
.about-box {
    background: linear-gradient(120deg, #7a0010, #b30018);
    color: white;
    padding: 55px;
    border-radius: 30px;
    margin-top: 50px;
    box-shadow: 0 16px 35px rgba(91,0,8,0.22);
}

.about-box h2 {
    font-size: 36px;
    font-weight: 800;
}

.about-box p {
    font-size: 19px;
    line-height: 1.9;
}

/* Contact */
.contact-box {
    background: white;
    border: 1px solid #f1d7d9;
    border-radius: 28px;
    padding: 40px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(91,0,8,0.10);
}

.contact-btn {
    display: inline-block;
    margin: 10px;
    padding: 14px 30px;
    background: #7a0010;
    color: white !important;
    border-radius: 40px;
    font-weight: 700;
    text-decoration: none;
}

/* Floating WhatsApp */
.whatsapp {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: #7a0010;
    color: white !important;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    text-align: center;
    line-height: 64px;
    font-size: 32px;
    text-decoration: none;
    box-shadow: 0 8px 25px rgba(91,0,8,0.35);
    z-index: 9999;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px;
    margin-top: 70px;
    color: #7a0010;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ================= NAVBAR =================
st.markdown("""
<div class="navbar">
    <div class="logo">Etisalat Telecom</div>
    <div class="nav-links">
        <span>Home</span>
        <span>Services</span>
        <span>Solutions</span>
        <span>About Us</span>
        <span>Contact</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
    <h1>Premium Telecom Solutions<br>For Modern Business</h1>
    <p>
        Etisalat Telecom provides advanced corporate telecom services, 
        business connectivity, mobile lines, internet solutions, VSAT satellite services, 
        and integrated digital infrastructure for enterprises.
    </p>
    <a href="#contact" class="hero-btn">Get Started</a>
</div>
""", unsafe_allow_html=True)

# ================= SERVICES =================
st.markdown('<div class="section-title">Our Services</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Integrated telecom and connectivity solutions for your business</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Corporate Lines</h3>
        <p>
        Managing corporate mobile lines, voice and data bundles, 
        billing support, tariff optimization, and account operations.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Business Internet</h3>
        <p>
        Corporate connectivity solutions including fixed internet, 
        4G/5G business routers, backup lines, and enterprise data services.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>VSAT & Satellite</h3>
        <p>
        Satellite connectivity solutions for remote sites, mines, 
        desert areas, construction locations, and critical operations.
        </p>
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <h3>Digital Infrastructure</h3>
        <p>
        Smart infrastructure, business transformation, networking, 
        and technology solutions tailored for enterprise operations.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <h3>Integrated Systems</h3>
        <p>
        Surveillance systems, smart monitoring, internal communication, 
        and integrated technology solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <h3>Account Management</h3>
        <p>
        Dedicated business account management, support follow-up, 
        billing tracking, and operational coordination.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ================= ABOUT =================
st.markdown("""
<div class="about-box">
    <h2>About Etisalat Telecom</h2>
    <p>
        Etisalat Telecom is a business-focused telecom solutions provider, 
        supporting companies with reliable communication services, enterprise connectivity, 
        corporate mobile solutions, satellite communication, and digital infrastructure.
        Our mission is to simplify telecom operations and deliver professional, scalable, 
        and secure solutions for every business sector.
    </p>
</div>
""", unsafe_allow_html=True)

# ================= CONTACT =================
st.markdown('<div class="section-title" id="contact">Contact Us</div>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">
    <h2 style="color:#5b0008;">Ready to connect your business?</h2>
    <p style="color:#555;font-size:18px;">
        Contact our team today and get a tailored telecom solution for your company.
    </p>
    <a class="contact-btn" href="tel:01000000000">Call Us</a>
    <a class="contact-btn" href="mailto:info@etisalattelecom.net">Email Us</a>
    <a class="contact-btn" href="https://wa.me/201000000000" target="_blank">WhatsApp</a>
</div>
""", unsafe_allow_html=True)

# ================= WHATSAPP FLOAT =================
st.markdown("""
<a class="whatsapp" href="https://wa.me/201000000000" target="_blank">☎</a>
""", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
    Etisalat Telecom © 2026 — Connect The Future
</div>
""", unsafe_allow_html=True)
