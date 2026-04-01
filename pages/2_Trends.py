# pages/2_Trends.py
# Place this file at: inflation_calculator/pages/2_Trends.py

import streamlit as st
from components.inject_css import inject_fonts, inject_css, nav_html, footer_html

st.set_page_config(
    page_title="Trends — InflaTrack",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_fonts()
inject_css()
st.markdown(nav_html("trends"), unsafe_allow_html=True)

st.markdown("""
<div class="page-wrap">
<div class="page-header">
  <div class="page-header-grid"></div>
  <div class="page-header-content">
    <div class="section-eyebrow">Inflation Trends</div>
    <h1>India's inflation, visualised</h1>
    <p>Official CPI data from MOSPI going back to 2012 — overall trends and all 8 sector breakdowns.</p>
  </div>
</div>

<div class="charts-body">

  <!-- Overall CPI chart -->
  <div class="chart-block">
    <div class="chart-block-header">
      <div>
        <div class="chart-block-title">Overall India CPI — annual inflation rate</div>
        <div class="chart-block-sub">Year-on-year % change · 2013–2025 · Base year 2012</div>
      </div>
      <div class="chart-tabs">
        <button class="chart-tab active" onclick="setTab(this,'combined')">Combined</button>
        <button class="chart-tab" onclick="setTab(this,'urban')">Urban</button>
        <button class="chart-tab" onclick="setTab(this,'rural')">Rural</button>
      </div>
    </div>
    <div class="chart-area">
      <!-- NOTE: Replace this SVG with a Plotly chart (st.plotly_chart) once
           your real CSV data is loaded from utils/data_loader.py.
           The SVG below is a design placeholder showing approximate historical shape. -->
      <svg class="chart-svg" viewBox="0 0 900 220" preserveAspectRatio="none">
        <line x1="0" y1="0" x2="900" y2="0" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".4"/>
        <line x1="0" y1="55" x2="900" y2="55" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".4"/>
        <line x1="0" y1="110" x2="900" y2="110" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".4"/>
        <line x1="0" y1="165" x2="900" y2="165" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".4"/>
        <line x1="0" y1="220" x2="900" y2="220" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".4"/>
        <!-- RBI target band (2–6%) shaded -->
        <rect x="0" y="66" width="900" height="88" fill="#92B775" opacity=".08"/>
        <!-- Overall CPI line -->
        <polyline points="0,28 75,77 150,99 225,116 300,121 375,132 450,143 525,88 600,66 650,55 700,88 750,99 800,88 850,82 900,91"
          fill="none" stroke="#133215" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="600" cy="66" r="4" fill="#133215"/>
        <circle cx="525" cy="88" r="4" fill="#133215"/>
        <text x="4" y="-6" font-size="10" fill="#6a7a6c" font-family="DM Mono">12%</text>
        <text x="4" y="49" font-size="10" fill="#6a7a6c" font-family="DM Mono">9%</text>
        <text x="4" y="104" font-size="10" fill="#6a7a6c" font-family="DM Mono">6%</text>
        <text x="4" y="159" font-size="10" fill="#6a7a6c" font-family="DM Mono">3%</text>
        <text x="4" y="214" font-size="10" fill="#6a7a6c" font-family="DM Mono">0%</text>
        <text x="820" y="80" font-size="9" fill="#92B775" font-family="DM Mono" opacity=".8">RBI target</text>
        <text x="820" y="92" font-size="9" fill="#92B775" font-family="DM Mono" opacity=".8">2–6%</text>
        <text x="0" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2013</text>
        <text x="112" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2015</text>
        <text x="225" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2017</text>
        <text x="338" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2019</text>
        <text x="450" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2021</text>
        <text x="563" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2022</text>
        <text x="675" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2024</text>
        <text x="788" y="236" font-size="10" fill="#6a7a6c" font-family="DM Mono">2025</text>
      </svg>
    </div>
  </div>

  <!-- Annotation cards -->
  <div class="annotation-grid">
    <div class="annotation-card">
      <div class="annotation-year">2013–14</div>
      <div class="annotation-title">Food-driven spike (9.5%)</div>
      <div class="annotation-body">Vegetable price surge driven by supply shocks. Onion prices rose over 200% in some months. RBI held rates high to contain food inflation.</div>
    </div>
    <div class="annotation-card">
      <div class="annotation-year">2020–21</div>
      <div class="annotation-title">COVID supply disruption (6.2%)</div>
      <div class="annotation-body">Lockdowns broke supply chains while food demand remained inelastic. Urban CPI spiked even as fuel deflated — an unusual composition effect.</div>
    </div>
    <div class="annotation-card">
      <div class="annotation-year">2022</div>
      <div class="annotation-title">Post-war commodity surge (7.8%)</div>
      <div class="annotation-body">Russia-Ukraine conflict sent edible oil, wheat, and fuel prices sharply higher. India's export ban on wheat stabilised domestic prices partially.</div>
    </div>
  </div>

  <!-- 8-sector chart -->
  <div class="chart-block">
    <div class="chart-block-header">
      <div>
        <div class="chart-block-title">Inflation by sector — all 8 CPI categories</div>
        <div class="chart-block-sub">Annual YoY % change per sector · 2013–2025</div>
      </div>
    </div>
    <div class="chart-area" style="height:300px">
      <!-- NOTE: Replace with st.plotly_chart using px.line with 8 colored lines
           once data/cpi_national.csv is loaded via utils/data_loader.py -->
      <svg class="chart-svg" viewBox="0 0 900 260" preserveAspectRatio="none">
        <line x1="0" y1="0" x2="900" y2="0" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".3"/>
        <line x1="0" y1="65" x2="900" y2="65" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".3"/>
        <line x1="0" y1="130" x2="900" y2="130" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".3"/>
        <line x1="0" y1="195" x2="900" y2="195" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".3"/>
        <line x1="0" y1="260" x2="900" y2="260" stroke="#c8c4b4" stroke-width=".5" stroke-dasharray="4 4" opacity=".3"/>
        <polyline points="0,19 100,78 200,104 300,130 400,156 500,91 600,39 700,91 800,104 900,117" fill="none" stroke="#EF9F27" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
        <polyline points="0,130 100,117 200,130 300,143 400,143 500,130 600,143 700,130 800,143 900,130" fill="none" stroke="#378ADD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
        <polyline points="0,156 100,130 200,169 300,117 400,52 500,182 600,78 700,169 800,143 900,156" fill="none" stroke="#E24B4A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
        <polyline points="0,143 100,130 200,117 300,104 400,91 500,78 600,78 700,78 800,91 900,78" fill="none" stroke="#7F77DD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
        <polyline points="0,91 100,91 200,78 300,78 400,65 500,65 600,65 700,78 800,78 900,78" fill="none" stroke="#1D9E75" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
        <polyline points="0,169 100,156 200,156 300,91 400,52 500,169 600,130 700,156 800,156 900,143" fill="none" stroke="#D85A30" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
        <polyline points="0,195 100,182 200,195 300,182 400,182 500,182 600,182 700,195 800,195 900,195" fill="none" stroke="#1D9E75" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity=".6" stroke-dasharray="6 3"/>
        <polyline points="0,195 100,182 200,156 300,143 400,130 500,117 600,117 700,130 800,130 900,130" fill="none" stroke="#D4537E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
        <text x="0" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2013</text>
        <text x="100" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2015</text>
        <text x="200" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2017</text>
        <text x="300" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2019</text>
        <text x="400" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2021</text>
        <text x="500" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2022</text>
        <text x="600" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2023</text>
        <text x="700" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2024</text>
        <text x="800" y="276" font-size="9.5" fill="#6a7a6c" font-family="DM Mono">2025</text>
      </svg>
    </div>
    <div class="chart-legend">
      <div class="legend-item"><div class="legend-dot" style="background:#EF9F27"></div>Food &amp; Beverages</div>
      <div class="legend-item"><div class="legend-dot" style="background:#378ADD"></div>Housing</div>
      <div class="legend-item"><div class="legend-dot" style="background:#E24B4A"></div>Fuel &amp; Light</div>
      <div class="legend-item"><div class="legend-dot" style="background:#7F77DD"></div>Healthcare</div>
      <div class="legend-item"><div class="legend-dot" style="background:#1D9E75"></div>Education</div>
      <div class="legend-item"><div class="legend-dot" style="background:#D85A30"></div>Transport</div>
      <div class="legend-item"><div class="legend-dot" style="background:#1D9E75;opacity:.6"></div>Clothing</div>
      <div class="legend-item"><div class="legend-dot" style="background:#D4537E"></div>Miscellaneous</div>
    </div>
  </div>

</div>

<script>
function setTab(el, type) {
  el.closest('.chart-tabs').querySelectorAll('.chart-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  // When real Plotly charts are in place, call a Python callback here via
  // st.session_state or trigger a Streamlit rerun with the selected series type.
}
</script>
""", unsafe_allow_html=True)

# ── IMPORTANT: Replace SVG placeholders with real Plotly charts here ──────────
# Once data/cpi_national.csv is ready, add this block below the SVGs:
#
# import plotly.express as px
# from utils.data_loader import load_national_cpi
#
# df = load_national_cpi()
# df_overall = df[df['sector'] == 'overall']
# fig = px.line(df_overall, x='date', y='inflation_rate',
#               color_discrete_sequence=['#133215'],
#               labels={'inflation_rate': 'YoY %', 'date': ''})
# fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
# st.plotly_chart(fig, use_container_width=True)

st.markdown(footer_html("Chart data is illustrative pending live MOSPI data integration. Historical trend shapes are directionally accurate."), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
