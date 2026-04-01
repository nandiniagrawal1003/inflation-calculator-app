# pages/1_Calculator.py
# Place this file at: inflation_calculator/pages/1_Calculator.py
# Streamlit will auto-add it to the nav as "Calculator"

import streamlit as st
from components.inject_css import inject_fonts, inject_css, nav_html, footer_html

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Calculator — InflaTrack",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_fonts()
inject_css()
st.markdown(nav_html("calculator"), unsafe_allow_html=True)

# ── Sector inflation rates (replace with real MOSPI data from your CSVs) ──────
# These are placeholder values. In Phase 4, load these from:
# utils/data_loader.py → load_national_cpi() → filtered by city + period
SECTOR_RATES = {
    "food": 9.2, "house": 5.8, "fuel": 7.4,
    "cloth": 3.1, "health": 5.9, "edu": 4.1,
    "trans": 6.0, "misc": 3.8
}
NATIONAL_CPI = 5.1

SECTOR_META = {
    "food":  {"label": "Food & Beverages", "icon": "🌾"},
    "house": {"label": "Housing / Rent",    "icon": "🏠"},
    "fuel":  {"label": "Fuel & Light",      "icon": "⛽"},
    "cloth": {"label": "Clothing",          "icon": "👕"},
    "health":{"label": "Healthcare",        "icon": "🏥"},
    "edu":   {"label": "Education",         "icon": "🎓"},
    "trans": {"label": "Transport",         "icon": "🚌"},
    "misc":  {"label": "Miscellaneous",     "icon": "🛒"},
}

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-wrap">
<div class="page-header">
  <div class="page-header-grid"></div>
  <div class="page-header-content">
    <div class="section-eyebrow">Personal Inflation Calculator</div>
    <h1>What's your real inflation rate?</h1>
    <p>Enter your monthly spending across each category. We'll compute your personal rate using official MOSPI sector data.</p>
  </div>
</div>
<div class="calc-body">
  <div class="calc-left">
""", unsafe_allow_html=True)

# ── Location & period row ─────────────────────────────────────────────────────
st.markdown('<div class="calc-section-title">Location &amp; period</div>', unsafe_allow_html=True)
st.markdown('<div class="location-row">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    city = st.selectbox(
        "City / State",
        ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata",
         "Hyderabad", "Lucknow", "Ahmedabad",
         "All India (Urban)", "All India (Rural)"],
        index=6,
        key="city_select"
    )
with col2:
    period = st.selectbox(
        "Reference period",
        ["Jan 2026", "Dec 2025", "Nov 2025", "Oct 2025", "Sep 2025"],
        index=1,
        key="period_select"
    )

st.markdown('</div>', unsafe_allow_html=True)

# ── Spending inputs ───────────────────────────────────────────────────────────
st.markdown('<div class="calc-section-title">Monthly spending breakdown</div>', unsafe_allow_html=True)
st.markdown('<div class="spending-grid">', unsafe_allow_html=True)

spending = {}
keys = list(SECTOR_META.keys())

# Build 2-column input grid using Streamlit columns
cols = st.columns(2)
for i, key in enumerate(keys):
    meta = SECTOR_META[key]
    with cols[i % 2]:
        val = st.number_input(
            f"{meta['icon']} {meta['label']}",
            min_value=0,
            max_value=500000,
            value=0,
            step=100,
            key=f"inp_{key}",
            help=f"Your average monthly spend on {meta['label'].lower()}"
        )
        spending[key] = val

st.markdown('</div>', unsafe_allow_html=True)

# ── Total bar ─────────────────────────────────────────────────────────────────
total = sum(spending.values())
st.markdown(f"""
<div class="total-bar">
  <div class="total-bar-label">Total monthly spending</div>
  <div class="total-bar-amount">₹{total:,.0f}</div>
</div>
""", unsafe_allow_html=True)

# ── Calculate button ──────────────────────────────────────────────────────────
calculate = st.button("Calculate my personal inflation rate →", key="calc_btn", use_container_width=True)

# Close calc-left div
st.markdown('</div>', unsafe_allow_html=True)

# ── Result panel ──────────────────────────────────────────────────────────────
st.markdown('<div class="result-panel">', unsafe_allow_html=True)

if not calculate or total == 0:
    st.markdown("""
    <div class="result-placeholder">
      <div class="result-placeholder-icon">📊</div>
      <div class="result-placeholder-text">
        Enter your monthly spending above and click calculate to see your personal inflation rate.
      </div>
    </div>
    """, unsafe_allow_html=True)
else:
    # ── Core calculation (mirrors utils/calculator.py) ────────────────────────
    contributions = {}
    personal_rate = 0.0
    for key, amount in spending.items():
        weight = amount / total
        contrib = weight * SECTOR_RATES[key]
        contributions[key] = contrib
        personal_rate += contrib

    personal_rate = round(personal_rate, 2)
    delta = round(personal_rate - NATIONAL_CPI, 2)
    delta_sign = "+" if delta >= 0 else ""
    delta_class = "result-delta" if delta > 0 else "result-delta below"

    # Save to session state for Future Simulator page
    st.session_state["spending_profile"] = spending
    st.session_state["personal_rate"] = personal_rate

    # ── Result header ─────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="result-header">
      <div class="result-label">Your personal inflation rate</div>
      <div class="result-rate">{personal_rate}%</div>
      <div class="result-vs">
        vs. national CPI&nbsp;
        <span style="font-family:'DM Mono',monospace;color:rgba(221,218,204,.6)">{NATIONAL_CPI}%</span>
        <span class="{delta_class}">{delta_sign}{delta}%</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Sector contribution bars ──────────────────────────────────────────────
    sorted_contribs = sorted(contributions.items(), key=lambda x: x[1], reverse=True)
    max_contrib = sorted_contribs[0][1] if sorted_contribs else 1

    drivers_html = '<div class="result-drivers"><div class="result-drivers-title">Contribution by sector</div>'
    for key, val in sorted_contribs:
        if val < 0.01:
            continue
        bar_w = int((val / max_contrib) * 100) if max_contrib > 0 else 0
        drivers_html += f"""
        <div class="driver-row">
          <div class="driver-name">{SECTOR_META[key]['label'].split('/')[0].strip()}</div>
          <div class="driver-track"><div class="driver-fill" style="width:{bar_w}%"></div></div>
          <div class="driver-val">{val:.2f}%</div>
        </div>"""
    drivers_html += '</div>'
    st.markdown(drivers_html, unsafe_allow_html=True)

    # ── Insight text ──────────────────────────────────────────────────────────
    top_key, top_val = sorted_contribs[0]
    top_name = SECTOR_META[top_key]['label']
    gap_desc = (
        f"Your inflation is <strong>{delta}% above</strong> the national average"
        if delta > 0
        else f"Your inflation is <strong>{abs(delta)}% below</strong> the national average"
    )

    st.markdown(f"""
    <div class="result-insight">
      <div class="result-insight-text">
        {gap_desc}. Your biggest cost driver is <strong>{top_name}</strong>,
        contributing <strong>{top_val:.2f}%</strong> to your personal rate.
        To maintain your standard of living, your income needs to grow by at
        least <strong>{personal_rate}%</strong> per year.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close result-panel
st.markdown('</div>', unsafe_allow_html=True)  # close calc-body

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(footer_html("Calculated rates are estimates based on user-declared spending and official MOSPI sector inflation data. For educational purposes only."), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # close page-wrap
