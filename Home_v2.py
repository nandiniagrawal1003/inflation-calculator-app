# Home.py
# Place this file at the ROOT of your project: inflation_calculator/Home.py
# Run with: streamlit run Home.py

import streamlit as st
from components.inject_css import inject_fonts, inject_css, nav_html, footer_html

st.set_page_config(
    page_title="InflaTrack — Personal Inflation Calculator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_fonts()
inject_css()
st.markdown(nav_html("home"), unsafe_allow_html=True)

# ── Extra page-specific styles ────────────────────────────────────────────────
st.markdown("""
<style>
.home-hero {
  background: var(--green);
  min-height: calc(100vh - 64px);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--green-light);
}
.home-hero-grid {
  position: absolute; inset: 0; z-index: 0;
  background-image:
    linear-gradient(rgba(146,183,117,.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(146,183,117,.05) 1px, transparent 1px);
  background-size: 48px 48px;
}
.home-hero-inner {
  position: relative; z-index: 1;
  max-width: 700px;
  text-align: center;
  padding: 80px 40px;
}
.home-eyebrow {
  font-family: 'DM Mono', monospace;
  font-size: 11px; font-weight: 500;
  color: var(--lime); letter-spacing: 2px;
  text-transform: uppercase; margin-bottom: 28px;
  display: flex; align-items: center; justify-content: center; gap: 10px;
}
.home-eyebrow-line {
  display: inline-block; width: 32px; height: 1px; background: var(--lime);
}
.home-hero-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(52px, 6vw, 80px);
  line-height: 1.08; color: var(--dew);
  margin-bottom: 28px; letter-spacing: -1.5px;
}
.home-hero-title em { font-style: italic; color: var(--lime); }
.home-hero-subtitle {
  font-size: 17px; line-height: 1.75; font-weight: 300;
  color: rgba(221,218,204,.7);
  max-width: 520px; margin: 0 auto 48px;
}
.home-hero-cta {
  display: flex; justify-content: center; margin-bottom: 28px;
}
.home-trust-line {
  font-family: 'DM Mono', monospace;
  font-size: 11px; color: rgba(221,218,204,.3); letter-spacing: .5px;
}
.home-why {
  background: var(--green);
  padding: 90px 80px;
  border-top: 1px solid var(--green-light);
  border-bottom: 1px solid var(--green-light);
}
.home-why-inner {
  max-width: 900px; margin: 0 auto; text-align: center;
}
.home-section-eyebrow {
  font-family: 'DM Mono', monospace;
  font-size: 11px; font-weight: 500;
  color: var(--lime); letter-spacing: 2px;
  text-transform: uppercase; margin-bottom: 20px;
  display: flex; align-items: center; justify-content: center; gap: 10px;
}
.home-section-eyebrow-line {
  display: inline-block; width: 24px; height: 1px; background: var(--lime);
}
.home-section-eyebrow.on-dew { color: var(--lime-dark); }
.home-section-eyebrow.on-dew .home-section-eyebrow-line { background: var(--lime-dark); }
.home-why-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(32px, 4vw, 48px);
  line-height: 1.15; letter-spacing: -1px;
  color: var(--dew); margin-bottom: 48px;
}
.home-why-cards {
  display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2px;
}
.home-why-card {
  background: rgba(221,218,204,.04);
  border: 1px solid rgba(146,183,117,.15);
  padding: 32px 28px; text-align: left;
}
.home-why-card:first-child { border-radius: 10px 0 0 10px; }
.home-why-card:last-child  { border-radius: 0 10px 10px 0; }
.home-why-card-icon { color: var(--lime); font-size: 22px; margin-bottom: 14px; }
.home-why-card-text {
  font-size: 14px; line-height: 1.75; font-weight: 300;
  color: rgba(221,218,204,.65);
}
.home-why-card-text strong { color: var(--dew); font-weight: 500; }
.home-how {
  background: var(--dew-light);
  padding: 90px 80px;
}
.home-how-inner { max-width: 900px; margin: 0 auto; }
.home-how-header { text-align: center; margin-bottom: 56px; }
.home-how-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(32px, 4vw, 48px);
  line-height: 1.1; letter-spacing: -1px;
  color: var(--green);
}
.home-cta {
  background: var(--green);
  padding: 72px 80px;
  text-align: center;
  border-top: 1px solid var(--green-light);
}
.home-cta-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(28px, 3.5vw, 42px);
  line-height: 1.15; letter-spacing: -0.5px;
  color: var(--dew); margin-bottom: 14px;
}
.home-cta-sub {
  font-size: 13px; font-weight: 300;
  color: rgba(221,218,204,.4);
  margin-bottom: 36px;
  font-family: 'DM Mono', monospace;
  letter-spacing: .3px;
}
.home-cta-btn {
  font-size: 15px;
  padding: 16px 40px;
  letter-spacing: .4px;
}
@media (max-width: 768px) {
  .home-why-cards { grid-template-columns: 1fr; }
  .home-why-card { border-radius: 8px !important; }
  .home-why, .home-how, .home-cta { padding: 60px 24px; }
  .home-hero-inner { padding: 60px 24px; }
}
</style>
""", unsafe_allow_html=True)

# ── Page sections ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-wrap">

<!-- 1. HERO -->
<section class="home-hero">
  <div class="home-hero-grid"></div>
  <div class="home-hero-inner">
    <div class="home-eyebrow">
      <span class="home-eyebrow-line"></span>
      Personal Inflation Calculator
      <span class="home-eyebrow-line"></span>
    </div>
    <h1 class="home-hero-title">Your inflation is <em>different.</em></h1>
    <p class="home-hero-subtitle">
      India's official inflation rate is an average.<br>
      But your spending habits aren't.<br>
      Calculate the inflation rate that actually reflects your life.
    </p>
    <div class="home-hero-cta">
      <a class="btn-primary home-cta-btn" href="/Calculator" target="_self">Calculate Mine</a>
    </div>
    <div class="home-trust-line">Based on official CPI data from MOSPI</div>
  </div>
</section>

<!-- 2. WHY THIS MATTERS -->
<section class="home-why">
  <div class="home-why-inner">
    <div class="home-section-eyebrow">
      <span class="home-section-eyebrow-line"></span>
      Why This Matters
      <span class="home-section-eyebrow-line"></span>
    </div>
    <h2 class="home-why-title">The numbers you see don't tell your story.</h2>
    <div class="home-why-cards">
      <div class="home-why-card">
        <div class="home-why-card-icon">&#128202;</div>
        <p class="home-why-card-text">
          When inflation is reported, it reflects the
          <strong>average spending pattern</strong> across millions of people.
        </p>
      </div>
      <div class="home-why-card">
        <div class="home-why-card-icon">&#129485;</div>
        <p class="home-why-card-text">
          But your lifestyle is different — what you spend on
          <strong>rent, food, travel, or lifestyle</strong>
          isn't the same as everyone else.
        </p>
      </div>
      <div class="home-why-card">
        <div class="home-why-card-icon">&#127919;</div>
        <p class="home-why-card-text">
          The real impact of inflation on <strong>your life</strong>
          can be very different from what's reported.
          This tool helps you understand that difference.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- 3. HOW IT WORKS -->
<section class="home-how">
  <div class="home-how-inner">
    <div class="home-how-header">
      <div class="home-section-eyebrow on-dew">
        <span class="home-section-eyebrow-line"></span>
        How It Works
        <span class="home-section-eyebrow-line"></span>
      </div>
      <h2 class="home-how-title">Simple. Personal. Accurate.</h2>
    </div>
    <div class="steps-grid">
      <div class="step-card">
        <div class="step-num">01</div>
        <div class="step-title">Tell us your spending</div>
        <div class="step-desc">Enter how much you spend across key categories like food, rent, transport, and more.</div>
      </div>
      <div class="step-card">
        <div class="step-num">02</div>
        <div class="step-title">We adjust the weights</div>
        <div class="step-desc">Your spending pattern is used to personalise how inflation is calculated for you — replacing national averages with your own basket.</div>
      </div>
      <div class="step-card">
        <div class="step-num">03</div>
        <div class="step-title">Get your personal rate</div>
        <div class="step-desc">See how inflation is actually affecting your lifestyle, with a full breakdown by category.</div>
      </div>
    </div>
  </div>
</section>

<!-- 4. FINAL CTA -->
<section class="home-cta">
  <h2 class="home-cta-title">See what inflation really looks like for you.</h2>
  <p class="home-cta-sub">It takes less than a minute.</p>
  <a class="btn-primary home-cta-btn" href="/Calculator" target="_self">Calculate Mine</a>
</section>

""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(footer_html(), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
