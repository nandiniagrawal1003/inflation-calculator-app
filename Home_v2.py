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

# ── Page Content ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-wrap">

<!-- ═══ 1. HERO SECTION ═══ -->
<section style="
  background: var(--green);
  min-height: calc(100vh - 64px);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--green-light);
">
  <!-- Decorative grid background -->
  <div style="
    position: absolute; inset: 0; z-index: 0;
    background-image:
      linear-gradient(rgba(146,183,117,.05) 1px, transparent 1px),
      linear-gradient(90deg, rgba(146,183,117,.05) 1px, transparent 1px);
    background-size: 48px 48px;
  "></div>

  <div style="
    position: relative; z-index: 1;
    max-width: 700px;
    text-align: center;
    padding: 80px 40px;
  ">
    <div style="
      font-family: 'DM Mono', monospace;
      font-size: 11px; font-weight: 500;
      color: var(--lime); letter-spacing: 2px;
      text-transform: uppercase; margin-bottom: 28px;
      display: flex; align-items: center; justify-content: center; gap: 10px;
    ">
      <span style="display:inline-block;width:32px;height:1px;background:var(--lime);"></span>
      Personal Inflation Calculator
      <span style="display:inline-block;width:32px;height:1px;background:var(--lime);"></span>
    </div>

    <h1 style="
      font-family: 'DM Serif Display', serif;
      font-size: clamp(52px, 6vw, 80px);
      line-height: 1.08; color: var(--dew);
      margin-bottom: 28px; letter-spacing: -1.5px;
    ">Your inflation is <em style="font-style:italic;color:var(--lime)">different.</em></h1>

    <p style="
      font-size: 17px; line-height: 1.75; font-weight: 300;
      color: rgba(221,218,204,.7);
      max-width: 520px; margin: 0 auto 48px;
    ">
      India's official inflation rate is an average.<br>
      But your spending habits aren't.<br>
      Calculate the inflation rate that actually reflects your life.
    </p>

    <div style="display:flex; justify-content:center; margin-bottom:28px;">
      <a class="btn-primary" href="/Calculator" target="_self"
         style="font-size:15px; padding:16px 40px; letter-spacing:.4px;">
        Calculate Mine
      </a>
    </div>

    <div style="
      font-family: 'DM Mono', monospace;
      font-size: 11px; color: rgba(221,218,204,.3);
      letter-spacing: .5px;
    ">Based on official CPI data from MOSPI</div>
  </div>
</section>

<!-- ═══ 2. WHY THIS MATTERS ═══ -->
<section style="
  background: var(--green);
  padding: 90px 80px;
  border-top: 1px solid var(--green-light);
  border-bottom: 1px solid var(--green-light);
">
  <div style="max-width: 800px; margin: 0 auto; text-align: center;">
    <div style="
      font-family: 'DM Mono', monospace;
      font-size: 11px; font-weight: 500;
      color: var(--lime); letter-spacing: 2px;
      text-transform: uppercase; margin-bottom: 20px;
      display: flex; align-items: center; justify-content: center; gap: 10px;
    ">
      <span style="display:inline-block;width:24px;height:1px;background:var(--lime);"></span>
      Why This Matters
      <span style="display:inline-block;width:24px;height:1px;background:var(--lime);"></span>
    </div>

    <h2 style="
      font-family: 'DM Serif Display', serif;
      font-size: clamp(32px, 4vw, 48px);
      line-height: 1.15; letter-spacing: -1px;
      color: var(--dew);
      margin-bottom: 40px;
    ">The numbers you see don't tell your story.</h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2px; margin-top: 16px;">
      <div style="
        background: rgba(221,218,204,.04);
        border: 1px solid rgba(146,183,117,.15);
        border-radius: 10px 0 0 10px;
        padding: 32px 28px; text-align: left;
      ">
        <div style="color:var(--lime);font-size:22px;margin-bottom:14px;">📊</div>
        <p style="font-size:14px;line-height:1.75;font-weight:300;color:rgba(221,218,204,.65);">
          When inflation is reported, it reflects the <strong style="color:var(--dew);font-weight:500;">average spending pattern</strong> across millions of people.
        </p>
      </div>
      <div style="
        background: rgba(221,218,204,.04);
        border: 1px solid rgba(146,183,117,.15);
        border-left: none; border-right: none;
        padding: 32px 28px; text-align: left;
      ">
        <div style="color:var(--lime);font-size:22px;margin-bottom:14px;">🧍</div>
        <p style="font-size:14px;line-height:1.75;font-weight:300;color:rgba(221,218,204,.65);">
          But your lifestyle is different — what you spend on <strong style="color:var(--dew);font-weight:500;">rent, food, travel, or lifestyle</strong> isn't the same as everyone else.
        </p>
      </div>
      <div style="
        background: rgba(221,218,204,.04);
        border: 1px solid rgba(146,183,117,.15);
        border-radius: 0 10px 10px 0;
        padding: 32px 28px; text-align: left;
      ">
        <div style="color:var(--lime);font-size:22px;margin-bottom:14px;">🎯</div>
        <p style="font-size:14px;line-height:1.75;font-weight:300;color:rgba(221,218,204,.65);">
          The real impact of inflation on <strong style="color:var(--dew);font-weight:500;">your life</strong> can be very different from what's reported. This tool helps you understand that difference.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 3. HOW IT WORKS ═══ -->
<section style="
  background: var(--dew-light);
  padding: 90px 80px;
">
  <div style="max-width: 900px; margin: 0 auto;">
    <div style="text-align:center; margin-bottom: 56px;">
      <div style="
        font-family: 'DM Mono', monospace;
        font-size: 11px; font-weight: 500;
        color: var(--lime-dark); letter-spacing: 2px;
        text-transform: uppercase; margin-bottom: 16px;
        display: flex; align-items: center; justify-content: center; gap: 10px;
      ">
        <span style="display:inline-block;width:24px;height:1px;background:var(--lime-dark);"></span>
        How It Works
        <span style="display:inline-block;width:24px;height:1px;background:var(--lime-dark);"></span>
      </div>
      <h2 style="
        font-family: 'DM Serif Display', serif;
        font-size: clamp(32px, 4vw, 48px);
        line-height: 1.1; letter-spacing: -1px;
        color: var(--green);
      ">Simple. Personal. Accurate.</h2>
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
        <div class="step-desc">Your spending pattern is used to personalise how inflation is calculated for you — replacing the government's national averages with your own basket.</div>
      </div>
      <div class="step-card">
        <div class="step-num">03</div>
        <div class="step-title">Get your personal rate</div>
        <div class="step-desc">See how inflation is actually affecting your lifestyle, with a full breakdown by category.</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 4. FINAL CTA ═══ -->
<section style="
  background: var(--green);
  padding: 72px 80px;
  text-align: center;
  border-top: 1px solid var(--green-light);
">
  <h2 style="
    font-family: 'DM Serif Display', serif;
    font-size: clamp(28px, 3.5vw, 42px);
    line-height: 1.15; letter-spacing: -0.5px;
    color: var(--dew); margin-bottom: 14px;
  ">See what inflation really looks like for you.</h2>

  <p style="
    font-size: 14px; font-weight: 300;
    color: rgba(221,218,204,.45);
    margin-bottom: 32px;
    font-family: 'DM Mono', monospace;
    letter-spacing: .3px;
  ">It takes less than a minute.</p>

  <a class="btn-primary" href="/Calculator" target="_self"
     style="font-size:15px; padding:16px 40px; letter-spacing:.4px;">
    Calculate Mine
  </a>
</section>

""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(footer_html(), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
