# ============================================================
# 2_City_Explorer.py — City Inflation Explorer Page
# ============================================================

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import load_data, get_cities, get_city_data

st.set_page_config(
    page_title="City Explorer",
    page_icon="🏙️",
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
    .summary-table-header {
        background-color: #E63946;
        color: white;
        padding: 8px 15px;
        border-radius: 6px 6px 0 0;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="page-title">🏙️ City Inflation Explorer</p>', unsafe_allow_html=True)
st.markdown("Compare how inflation has behaved differently across major Indian cities.")
st.markdown("---")

df = load_data()
cities = get_cities(df)

# ---- CONTROLS ROW ----
ctrl1, ctrl2, ctrl3 = st.columns(3)

with ctrl1:
    city1 = st.selectbox("🔴 First City", cities, index=0)

with ctrl2:
    city2 = st.selectbox("🔵 Second City", cities, index=1)

with ctrl3:
    categories = ['National_CPI','Food','Housing','Fuel',
                  'Clothing','Health','Education','Transport','Misc']
    category_labels = {
        'National_CPI': '📊 Overall CPI',
        'Food': '🛒 Food',
        'Housing': '🏠 Housing',
        'Fuel': '⛽ Fuel',
        'Clothing': '👕 Clothing',
        'Health': '💊 Health',
        'Education': '📚 Education',
        'Transport': '🚌 Transport',
        'Misc': '📦 Misc'
    }
    selected_cat = st.selectbox(
        "📂 CPI Category",
        categories,
        format_func=lambda x: category_labels[x]
    )

st.markdown("---")

# ---- GET CITY DATA ----
data1 = get_city_data(df, city1).sort_values('Date')
data2 = get_city_data(df, city2).sort_values('Date')

# ---- MAIN COMPARISON CHART ----
st.markdown(f'<p class="section-header">📈 {category_labels[selected_cat]} — {city1} vs {city2}</p>', unsafe_allow_html=True)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data1['Date'],
    y=data1[selected_cat],
    name=city1,
    line=dict(color='#E63946', width=2.5),
    fill='tozeroy',
    fillcolor='rgba(230,57,70,0.06)',
    mode='lines+markers',
    marker=dict(size=5)
))

fig.add_trace(go.Scatter(
    x=data2['Date'],
    y=data2[selected_cat],
    name=city2,
    line=dict(color='#4895EF', width=2.5),
    fill='tozeroy',
    fillcolor='rgba(72,149,239,0.06)',
    mode='lines+markers',
    marker=dict(size=5)
))

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#FFFFFF'),
    xaxis=dict(title='Month', gridcolor='#30363D'),
    yaxis=dict(title='CPI Value', gridcolor='#30363D'),
    legend=dict(orientation='h', y=1.12, bgcolor='rgba(0,0,0,0)'),
    hovermode='x unified',
    height=420,
    margin=dict(l=10, r=10, t=40, b=10)
)

st.plotly_chart(fig, use_container_width=True)

# ---- SUMMARY TABLE ----
st.markdown('<p class="section-header">📋 Quick Comparison Summary</p>', unsafe_allow_html=True)

def get_summary(data, city_name, col):
    latest = data[col].iloc[-1]
    avg12 = data[col].tail(12).mean()
    yoy = ((data[col].iloc[-1] / data[col].iloc[-13]) - 1) * 100 if len(data) >= 13 else None
    return {
        'City': city_name,
        'Latest CPI Value': f"{latest:.1f}",
        '12-Month Average': f"{avg12:.1f}",
        'Year-on-Year Change': f"{yoy:.2f}%" if yoy else "N/A"
    }

summary = pd.DataFrame([
    get_summary(data1, city1, selected_cat),
    get_summary(data2, city2, selected_cat)
])

st.dataframe(summary, use_container_width=True, hide_index=True)

# ---- ALL CATEGORIES CHART ----
st.markdown("---")
st.markdown(f'<p class="section-header">📊 All Categories — {city1}</p>', unsafe_allow_html=True)

fig2 = go.Figure()
cat_colors = ['#E63946','#4895EF','#2DC653','#F4A261',
              '#A8DADC','#E9C46A','#264653','#F77F00']
cat_only = ['Food','Housing','Fuel','Clothing',
            'Health','Education','Transport','Misc']

for i, cat in enumerate(cat_only):
    fig2.add_trace(go.Scatter(
        x=data1['Date'],
        y=data1[cat],
        name=cat,
        line=dict(color=cat_colors[i], width=2),
        mode='lines'
    ))

fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#FFFFFF'),
    xaxis=dict(title='Month', gridcolor='#30363D'),
    yaxis=dict(title='CPI Value', gridcolor='#30363D'),
    hovermode='x unified',
    height=430,
    legend=dict(orientation='h', y=-0.2, bgcolor='rgba(0,0,0,0)'),
    margin=dict(l=10, r=10, t=20, b=10)
)

st.plotly_chart(fig2, use_container_width=True)