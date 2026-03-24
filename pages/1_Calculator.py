# ============================================================
# app.py — Homepage of the app
# This is what users see when they first open the link
# ============================================================

import streamlit as st

# MUST be the very first Streamlit command
st.set_page_config(
    page_title="Personal Inflation Calculator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- CUSTOM CSS ----
# This block adds extra styling on top of the theme
# It makes the homepage look more polished
st.markdown("""
    <style>
    /* Make the main title bigger and centered */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: #E63946;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    /* Subtitle below the title */
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #AAAAAA;
        margin-top: 0;
        padding-top: 5px;
        margin-bottom: 30px;
    }
    /* Each feature card box */
    .feature-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 25px;
        margin: 10px 0;
        transition: border-color 0.3s;
    }
    /* Card title */
    .card-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #E63946;
        margin-bottom: 10px;
    }
    /* Card description */
    .card-desc {
        font-size: 0.95rem;
        color: #CCCCCC;
        line-height: 1.6;
    }
    /* The how it works steps */
    .step-box {
        background-color: #161B22;
        border-left: 4px solid #E63946;
        padding: 15px 20px;
        margin: 8px 0;
        border-radius: 0 8px 8px 0;
        color: #FFFFFF;
    }
    /* Bottom stats bar */
    .stat-box {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #E63946;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #AAAAAA;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown(
    '<p class="main-title">📊 Personal Inflation Calculator</p>',
    unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-title">Discover your real inflation rate — not just the national average</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---- THREE FEATURE CARDS ----
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="card-title">🧮 Personal Calculator</div>
        <div class="card-desc">
            Enter your monthly expenses across 8 categories.
            Get your own personalised inflation rate compared 
            to the official national CPI — and see exactly 
            where your money is losing value fastest.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="card-title">🏙️ City Explorer</div>
        <div class="card-desc">
            Compare inflation trends across Mumbai, Delhi, 
            Chennai, Bengaluru, and Kolkata. Select any two 
            cities and see a side-by-side chart of how 
            inflation has differed over time.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="card-title">🔮 Future Simulator</div>
        <div class="card-desc">
            Enter your current monthly expenses and see 
            projections for 1, 3, and 5 years ahead under 
            optimistic, baseline, and pessimistic inflation 
            scenarios using compound growth.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---- HOW IT WORKS SECTION ----
st.markdown("### How It Works")
st.markdown(" ")

st.markdown('<div class="step-box">📌 <b>Step 1</b> — Go to the <b>Personal Calculator</b> page from the sidebar and enter your monthly spending in each category</div>', unsafe_allow_html=True)
st.markdown('<div class="step-box">📌 <b>Step 2</b> — Click Calculate — the app computes your personal inflation rate using real MOSPI city-level CPI data</div>', unsafe_allow_html=True)
st.markdown('<div class="step-box">📌 <b>Step 3</b> — Compare your rate against the national average on an interactive chart</div>', unsafe_allow_html=True)
st.markdown('<div class="step-box">📌 <b>Step 4</b> — Explore the City Explorer and Future Simulator for deeper insights</div>', unsafe_allow_html=True)

st.markdown("---")

# ---- BOTTOM STATS BAR ----
s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">5</div>
        <div class="stat-label">Indian Cities Covered</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">8</div>
        <div class="stat-label">Spending Categories</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">3</div>
        <div class="stat-label">Future Scenarios</div>
    </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">2+</div>
        <div class="stat-label">Years of CPI Data</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---- FOOTER ----
st.markdown("""
<div style="text-align:center; color:#666666; font-size:0.8rem; padding:10px 0;">
    Data Source: Ministry of Statistics and Programme Implementation (MOSPI), 
    Government of India &nbsp;|&nbsp; For educational purposes only
</div>
""", unsafe_allow_html=True)