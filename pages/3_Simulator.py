# pages/3_Sources.py
# Place this file at: inflation_calculator/pages/3_Sources.py

import streamlit as st
from components.inject_css import inject_fonts, inject_css, nav_html, footer_html

st.set_page_config(
    page_title="Sources — InflaTrack",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_fonts()
inject_css()
st.markdown(nav_html("sources"), unsafe_allow_html=True)

st.markdown("""
<div class="page-wrap">
<div class="page-header">
  <div class="page-header-grid"></div>
  <div class="page-header-content">
    <div class="section-eyebrow">Data Integrity</div>
    <h1>Where the data comes from</h1>
    <p>Every number in this tool traces back to official government sources. Here's what we use, and why.</p>
  </div>
</div>

<div class="sources-body">
  <p class="sources-intro">
    This tool uses only data published by India's official statistical agencies.
    No estimates, no private data providers, no third-party aggregators.
    If a number appears in this calculator, you can trace it directly to a government
    document. The links below take you to the exact sources.
  </p>

  <div class="source-cards">

    <div class="source-card">
      <div class="source-badge">Primary</div>
      <div>
        <div class="source-name">Ministry of Statistics &amp; PI (MOSPI)</div>
        <div class="source-desc">
          The primary source for all CPI data in this application. MOSPI publishes monthly
          Consumer Price Index figures at the national level, disaggregated by urban/rural
          and all 8 expenditure sub-categories. City-level CPI for major Indian urban centres
          is also published here. Data goes back to 2012 under the current base year series.
        </div>
        <div class="source-tags">
          <span class="source-tag">Monthly CPI releases</span>
          <span class="source-tag">Urban &amp; Rural split</span>
          <span class="source-tag">8 sector breakdown</span>
          <span class="source-tag">State-wise data</span>
          <span class="source-tag">Base Year 2012 &amp; 2024</span>
        </div>
      </div>
      <a class="source-link"
         href="https://mospi.gov.in/themes/product/9-consumer-price-index-cpi"
         target="_blank">mospi.gov.in ↗</a>
    </div>

    <div class="source-card">
      <div class="source-badge">Supplementary</div>
      <div>
        <div class="source-name">RBI — Database on Indian Economy</div>
        <div class="source-desc">
          The Reserve Bank of India's DBIE portal provides clean, downloadable time-series
          CPI data in CSV format, often easier to work with programmatically than MOSPI's
          Excel files. Also the source for RBI's inflation target band (2–6%) and Monetary
          Policy Committee projections used in the future inflation section.
        </div>
        <div class="source-tags">
          <span class="source-tag">CSV downloads</span>
          <span class="source-tag">Long time series</span>
          <span class="source-tag">MPC projections</span>
          <span class="source-tag">Monetary policy context</span>
        </div>
      </div>
      <a class="source-link" href="https://dbie.rbi.org.in" target="_blank">dbie.rbi.org.in ↗</a>
    </div>

    <div class="source-card">
      <div class="source-badge">Cross-reference</div>
      <div>
        <div class="source-name">Open Government Data — data.gov.in</div>
        <div class="source-desc">
          India's open government data platform provides archived CPI datasets in structured
          CSV format. Used to cross-reference and validate MOSPI data, and to access some
          historical series that are easier to parse here than from MOSPI's Excel workbooks directly.
        </div>
        <div class="source-tags">
          <span class="source-tag">Archived datasets</span>
          <span class="source-tag">CSV format</span>
          <span class="source-tag">Cross-validation</span>
        </div>
      </div>
      <a class="source-link" href="https://data.gov.in" target="_blank">data.gov.in ↗</a>
    </div>

  </div>

  <!-- Methodology box -->
  <div class="methodology-box">
    <div class="section-eyebrow" style="color:var(--lime)">Methodology</div>
    <div class="methodology-title">How the personal inflation rate is calculated</div>
    <p class="methodology-body">
      This tool uses the same mathematical framework that MOSPI uses to compute the
      official CPI — the Laspeyres weighted price index, formalized by economist
      Étienne Laspeyres in 1871 and used by every major national statistics agency
      in the world. The only difference is that we replace the government's fixed
      national weights with weights derived from your own spending.
    </p>
    <p class="methodology-body">
      Each sector's contribution to your personal inflation is its spending weight
      multiplied by the official inflation rate for that sector in the selected period.
      Summing these contributions gives your personal inflation rate.
    </p>
    <div class="formula-display">
      Personal Inflation = <span>Σ</span> ( W<span>ᵢ</span> × P<span>ᵢ</span> )<br>
      <span style="font-size:12px;opacity:.6">
        Where W<span>ᵢ</span> = your spending on sector i ÷ total spending<br>
        And P<span>ᵢ</span> = official YoY inflation rate for sector i (from MOSPI)
      </span>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown(footer_html(), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
