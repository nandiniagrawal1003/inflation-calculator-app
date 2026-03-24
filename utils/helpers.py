# ============================================================
# helpers.py — Shared functions used by all pages
# Think of this as the engine room nobody sees
# ============================================================

import pandas as pd
import streamlit as st

# ---- DATA LOADING ----
# @st.cache_data means: run this once, remember the result
# Don't re-read the file every time user clicks something
@st.cache_data
def load_data():
    df = pd.read_csv("data/cpi_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_cities(df):
    # Returns a sorted list of all city names
    return sorted(df['City'].unique().tolist())

def get_city_data(df, city):
    # Returns only the rows for one specific city
    return df[df['City'] == city].copy()

# ---- PERSONAL INFLATION CALCULATION ----
def calculate_personal_inflation(spending, df, city):
    city_df = get_city_data(df, city)
    city_df = city_df.sort_values('Date')

    total_spending = sum(spending.values())
    if total_spending == 0:
        return 0, city_df

    categories = ['Food','Housing','Fuel','Clothing',
                  'Health','Education','Transport','Misc']
    spending_keys = ['food','housing','fuel','clothing',
                     'health','education','transport','misc']

    # Weight = what % of total spending goes to each category
    weights = {key: spending[key] / total_spending 
               for key in spending_keys}

    # Month on month % change for each category
    for cat in categories:
        city_df[f'{cat}_pct'] = city_df[cat].pct_change() * 100

    # Weighted personal inflation
    city_df['personal_inflation'] = sum(
        city_df[f'{cat}_pct'] * weights[key]
        for cat, key in zip(categories, spending_keys)
    )

    city_df['national_inflation'] = (
        city_df['National_CPI'].pct_change() * 100
    )

    avg_personal = city_df['personal_inflation'].mean()
    return avg_personal, city_df