# Home.py
# Place this file at the ROOT of your project: inflation_calculator/Home.py
# This is the landing page. Run with: streamlit run Home.py

import streamlit as st
from components.inject_css import inject_fonts, inject_css, nav_html, footer_html

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="InflaTrack — Personal Inflation Calculator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_fonts()
inject_css()

# ── Nav ───────────────────────────────────────────────────────────────────────
st.markdown(nav_html("home"), unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-wrap">
<section class="hero">
  <div class="hero-left">
    <div class="hero-eyebrow">Personal Inflation Calculator</div>
    <h1 class="hero-title">
      Inflation hits everyone <em>differently.</em> See how it hits you.
    </h1>
    <p class="hero-subtitle">
      India's official CPI is an average across 1.4 billion people.
      Your spending isn't average. Calculate the inflation rate that
      actually reflects your life.
    </p>
    <div class="hero-buttons">
      <a class="btn-primary" href="/Calculator" target="_self">Calculate my inflation</a>
      <a class="btn-secondary" href="/Trends" target="_self">Explore trends</a>
    </div>
    <div class="hero-stats">
      <div class="stat-item">
        <div class="stat-num">8</div>
        <div class="stat-label">CPI categories tracked</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">13yr</div>
        <div class="stat-label">Historical data</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">MOSPI</div>
        <div class="stat-label">Official data source</div>
      </div>
    </div>
  </div>

  <div class="hero-right">
    <div class="hero-grid"></div>
    <div class="hero-card">
      <div class="hero-card-label">Your personal inflation rate</div>
      <div class="hero-card-rate">7.4%</div>
      <div class="hero-card-sub">Based on your spending profile</div>
      <div class="hero-card-vs">vs. official national CPI</div>
      <div class="hero-card-national">
        <div class="hero-card-national-rate">5.1%</div>
        <div class="hero-card-badge above">+2.3% above</div>
      </div>
      <div class="mini-bars">
        <div class="mini-bar-row">
          <div class="mini-bar-label">Food</div>
          <div class="mini-bar-track"><div class="mini-bar-fill" style="width:72%"></div></div>
          <div class="mini-bar-val">3.1%</div>
        </div>
        <div class="mini-bar-row">
          <div class="mini-bar-label">Housing</div>
          <div class="mini-bar-track"><div class="mini-bar-fill" style="width:48%;opacity:.7"></div></div>
          <div class="mini-bar-val">2.0%</div>
        </div>
        <div class="mini-bar-row">
          <div class="mini-bar-label">Fuel</div>
          <div class="mini-bar-track"><div class="mini-bar-fill" style="width:26%;opacity:.5"></div></div>
          <div class="mini-bar-val">1.1%</div>
        </div>
        <div class="mini-bar-row">
          <div class="mini-bar-label">Health</div>
          <div class="mini-bar-track"><div class="mini-bar-fill" style="width:16%;opacity:.4"></div></div>
          <div class="mini-bar-val">0.7%</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Features strip -->
<div class="features-strip">
  <div class="feature-pill"><div class="feature-pill-dot"></div><div class="feature-pill-text">Weighted Laspeyres formula</div></div>
  <div class="feature-pill"><div class="feature-pill-dot"></div><div class="feature-pill-text">MOSPI &amp; RBI official data</div></div>
  <div class="feature-pill"><div class="feature-pill-dot"></div><div class="feature-pill-text">City-level CPI comparison</div></div>
  <div class="feature-pill"><div class="feature-pill-dot"></div><div class="feature-pill-text">Sector-by-sector breakdown</div></div>
  <div class="feature-pill"><div class="feature-pill-dot"></div><div class="feature-pill-text">Historical trends 2012–2026</div></div>
  <div class="feature-pill"><div class="feature-pill-dot"></div><div class="feature-pill-text">Future expense projection</div></div>
</div>

<!-- How it works -->
<section class="how-section">
  <div class="section-eyebrow">How it works</div>
  <h2 class="section-title">Three steps to your real inflation number</h2>
  <div class="steps-grid">
    <div class="step-card">
      <div class="step-num">01</div>
      <div class="step-title">Enter your spending</div>
      <div class="step-desc">Tell us how much you spend each month across 8 categories — food, housing, fuel, health, education, transport, clothing, and miscellaneous.</div>
    </div>
    <div class="step-card">
      <div class="step-num">02</div>
      <div class="step-title">We apply official rates</div>
      <div class="step-desc">We multiply your spending weights against MOSPI's official sector-level CPI data using the same Laspeyres formula the government uses — just with your basket, not the national average.</div>
    </div>
    <div class="step-card">
      <div class="step-num">03</div>
      <div class="step-title">See your real rate</div>
      <div class="step-desc">Your personal inflation rate, compared against the official CPI, with a breakdown showing exactly which categories are driving your costs up — and by how much.</div>
    </div>
  </div>
</section>

<!-- Explainer band -->
<section class="explainer-band">
  <div class="explainer-left">
    <div class="section-eyebrow" style="color:var(--lime)">Why this matters</div>
    <h2 class="section-title" style="color:var(--dew);margin-bottom:20px">The official CPI doesn't reflect your life</h2>
    <p class="explainer-body">India's CPI uses spending weights from a 2011–12 household survey. It assigns 46% weight to food — but if you're a salaried urban professional, you might spend 25% on food and 35% on rent. That gap changes everything about what inflation means to you.</p>
    <p class="explainer-body">If food prices rise 9% and you only spend 25% on food, food contributes 2.25% to your personal inflation. But the government's 46% weight shows 4.14% from food alone — nearly double.</p>
    <a class="btn-primary" href="/Calculator" target="_self" style="margin-top:8px">Calculate my rate</a>
  </div>
  <div class="explainer-right">
    <div class="weight-title">Official MOSPI weights (Urban CPI)</div>
    <div class="weight-row"><div class="weight-sector">Food &amp; Bev.</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:36%"></div></div><div class="weight-pct">36.3%</div></div>
    <div class="weight-row"><div class="weight-sector">Housing</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:21%"></div></div><div class="weight-pct">21.7%</div></div>
    <div class="weight-row"><div class="weight-sector">Miscellaneous</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:22%"></div></div><div class="weight-pct">22.1%</div></div>
    <div class="weight-row"><div class="weight-sector">Fuel &amp; Light</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:6%"></div></div><div class="weight-pct">5.6%</div></div>
    <div class="weight-row"><div class="weight-sector">Clothing</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:6%"></div></div><div class="weight-pct">5.9%</div></div>
    <div class="weight-row"><div class="weight-sector">Transport</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:5%"></div></div><div class="weight-pct">4.5%</div></div>
    <div class="weight-row"><div class="weight-sector">Health</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:4%"></div></div><div class="weight-pct">3.8%</div></div>
    <div class="weight-row"><div class="weight-sector">Education</div><div class="weight-bar-track"><div class="weight-bar-fill" style="width:5%"></div></div><div class="weight-pct">4.5%</div></div>
    <div class="weight-note">Source: MOSPI Urban CPI weights, Base Year 2012. Your weights may differ significantly — which is exactly why this calculator exists.</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(footer_html(), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
