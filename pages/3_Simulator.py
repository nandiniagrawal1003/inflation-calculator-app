# ============================================================
# 3_Simulator.py — Future Expense Simulator Page
# ============================================================

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Future Simulator",
    page_icon="🔮",
    layout="wide"
)

st.markdown("""
    <style>
    .page-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #E63946;
    }
    .section-header {
        font-size: 1.1rem;
        font-weight: 700;
        color: #FFFFFF;
        margin: 20px 0 10px 0;
        padding-bottom: 5px;
        border-bottom: 2px solid #E63946;
    }
    .scenario-card {
        border-radius: 10px;
        padding: 15px 20px;
        margin: 8px 0;
        font-size: 0.95rem;
        font-weight: 600;
    }
    .insight-box {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 20px 25px;
        margin-top: 15px;
        line-height: 1.8;
        color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="page-title">🔮 Future Expense Simulator</p>', unsafe_allow_html=True)
st.markdown("Project how your monthly expenses will grow over time using the compound inflation formula.")
st.markdown("---")

# ---- LAYOUT ----
left_col, right_col = st.columns([1, 2], gap="large")

# ====================
# LEFT — INPUTS
# ====================
with left_col:

    st.markdown('<p class="section-header">Your Current Expenses</p>', unsafe_allow_html=True)

    current = st.number_input(
        "Total Monthly Expense (₹)",
        min_value=1000,
        value=25000,
        step=1000,
        help="Your total monthly spending right now"
    )

    st.markdown('<p class="section-header">Inflation Rate Assumption</p>', unsafe_allow_html=True)

    custom_rate = st.slider(
        "Drag to set annual inflation rate (%)",
        min_value=1.0,
        max_value=15.0,
        value=6.0,
        step=0.5,
        help="India's average CPI has been around 5-7% in recent years"
    )

    st.markdown('<p class="section-header">Preset Scenarios</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="scenario-card" style="background-color:#0d2b1a; border:1px solid #2DC653; color:#2DC653;">
        🟢 Optimistic &nbsp;—&nbsp; 3% annual inflation
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="scenario-card" style="background-color:#1a1a0d; border:1px solid #E9C46A; color:#E9C46A;">
        🟡 Baseline &nbsp;—&nbsp; 6% annual inflation
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="scenario-card" style="background-color:#2b0d0d; border:1px solid #E63946; color:#E63946;">
        🔴 Pessimistic &nbsp;—&nbsp; 10% annual inflation
    </div>
    """, unsafe_allow_html=True)

    st.markdown(" ")
    st.caption("Formula: Future Value = Present Value × (1 + r)ⁿ")

# ====================
# RIGHT — RESULTS
# ====================
with right_col:

    # Compound inflation formula
    def project(amount, rate, year):
        return amount * (1 + rate / 100) ** year

    # ---- CUSTOM RATE METRICS ----
    st.markdown(f'<p class="section-header">At Your Custom Rate ({custom_rate}%)</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        v1 = project(current, custom_rate, 1)
        st.metric(
            "After 1 Year",
            f"₹{v1:,.0f}",
            f"+₹{v1 - current:,.0f}/month"
        )

    with c2:
        v3 = project(current, custom_rate, 3)
        st.metric(
            "After 3 Years",
            f"₹{v3:,.0f}",
            f"+₹{v3 - current:,.0f}/month"
        )

    with c3:
        v5 = project(current, custom_rate, 5)
        st.metric(
            "After 5 Years",
            f"₹{v5:,.0f}",
            f"+₹{v5 - current:,.0f}/month"
        )

    st.markdown("---")

    # ---- GROUPED BAR CHART ----
    st.markdown('<p class="section-header">All Scenarios Comparison</p>', unsafe_allow_html=True)

    years = [1, 3, 5]
    scenarios = {
        f'Custom ({custom_rate}%)': (custom_rate, '#F4A261'),
        'Optimistic (3%)': (3.0, '#2DC653'),
        'Baseline (6%)': (6.0, '#4895EF'),
        'Pessimistic (10%)': (10.0, '#E63946'),
    }

    fig = go.Figure()

    for name, (rate, color) in scenarios.items():
        vals = [project(current, rate, y) for y in years]
        fig.add_trace(go.Bar(
            name=name,
            x=[f'Year {y}' for y in years],
            y=vals,
            text=[f'₹{v:,.0f}' for v in vals],
            textposition='outside',
            textfont=dict(size=10),
            marker_color=color
        ))

    # Dashed line showing current expense
    fig.add_hline(
        y=current,
        line_dash='dash',
        line_color='#FFFFFF',
        line_width=1.5,
        annotation_text=f'Current: ₹{current:,}',
        annotation_font_color='#FFFFFF',
        annotation_position='left'
    )

    fig.update_layout(
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(title='Time Horizon', gridcolor='#30363D'),
        yaxis=dict(title='Monthly Expense (₹)', gridcolor='#30363D'),
        legend=dict(orientation='h', y=-0.2, bgcolor='rgba(0,0,0,0)'),
        height=430,
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---- PLAIN LANGUAGE INSIGHT ----
    st.markdown('<p class="section-header">📌 What This Means For You</p>', unsafe_allow_html=True)

    best5 = project(current, 3.0, 5)
    base5 = project(current, 6.0, 5)
    worst5 = project(current, 10.0, 5)
    custom5 = project(current, custom_rate, 5)

    st.markdown(f"""
    <div class="insight-box">
        Starting from <b>₹{current:,}/month</b> today:<br><br>
        🟢 <b>Best case (3%):</b> You'll need <b>₹{best5:,.0f}/month</b> in 5 years 
        &nbsp;(+₹{best5 - current:,.0f})<br>
        🟡 <b>Expected (6%):</b> You'll need <b>₹{base5:,.0f}/month</b> in 5 years 
        &nbsp;(+₹{base5 - current:,.0f})<br>
        🔴 <b>Worst case (10%):</b> You'll need <b>₹{worst5:,.0f}/month</b> in 5 years 
        &nbsp;(+₹{worst5 - current:,.0f})<br>
        ⚙️ <b>Your custom ({custom_rate}%):</b> You'll need <b>₹{custom5:,.0f}/month</b> in 5 years 
        &nbsp;(+₹{custom5 - current:,.0f})<br><br>
        💡 This means your <b>income or savings must grow by at least {custom_rate}% per year</b> 
        just to maintain your current standard of living.
    </div>
    """, unsafe_allow_html=True)


