import streamlit as st
from datetime import timedelta

from api import fetch_covid_data
from processor import process_data
from plots import *

st.set_page_config(
    page_title="COVID-19 Dashboard",
    layout="wide"
)

st.title("🇧🇩 COVID-19 Disease Trend Dashboard")
st.caption("Colorful Data Visualization | Source: disease.sh")

COUNTRIES = [
    "Bangladesh", "India", "Pakistan",
    "Nepal", "Sri Lanka", "United States", "United Kingdom"
]

selected_country = st.selectbox("🌍 Select Country", COUNTRIES)

raw_data = fetch_covid_data(selected_country, days=120)
df = process_data(raw_data)

# Date range
min_date = df.index.min()
max_date = df.index.max()

start_date, end_date = st.date_input(
    "📅 Select Date Range",
    value=(max_date - timedelta(days=30), max_date),
    min_value=min_date,
    max_value=max_date
)

df = df.loc[start_date:end_date]

# Metrics cards
c1, c2, c3 = st.columns(3)
c1.metric("🧪 Total Cases", int(df["cases"].iloc[-1]))
c2.metric("⚰️ Total Deaths", int(df["deaths"].iloc[-1]))
c3.metric("💚 Recovered", int(df["recovered"].iloc[-1]))

st.download_button(
    "⬇️ Download CSV",
    df.to_csv().encode("utf-8"),
    file_name=f"{selected_country}_covid_data.csv"
)

st.divider()

st.pyplot(plot_daily_cases(df))

col_left, col_right = st.columns(2)
with col_left:
    st.pyplot(plot_deaths(df))
with col_right:
    st.pyplot(plot_recovery(df))

st.pyplot(plot_growth_rate(df))
