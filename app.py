
from pathlib import Path

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="India Air Quality Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "city_day_cleaned.csv"
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "archive-3" / "city_day.csv"

st.markdown(
    """
    <style>
    .stApp {
        background: #0b1120;
        color: #e5e7eb;
    }
    [data-testid="stSidebar"] {
        background: #111827;
    }
    [data-testid="stMetric"] {
        background: #151f32;
        border: 1px solid #29364d;
        padding: 18px;
        border-radius: 12px;
    }
    h1, h2, h3 {
        color: #f8fafc;
    }
    .subtitle {
        color: #94a3b8;
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["AQI"] = pd.to_numeric(data["AQI"], errors="coerce")

    data = data.dropna(subset=["Date", "City"]).copy()
    data["Year"] = data["Date"].dt.year
    data["Month"] = data["Date"].dt.month
    data["Month_Name"] = data["Date"].dt.strftime("%b")

    data["Season"] = np.select(
        [
            data["Month"].isin([12, 1, 2]),
            data["Month"].isin([3, 4, 5]),
            data["Month"].isin([6, 7, 8, 9]),
            data["Month"].isin([10, 11]),
        ],
        ["Winter", "Summer", "Monsoon", "Post-Monsoon"],
        default="Unknown",
    )
    return data


if not DATA_PATH.exists():
    st.error(f"Cleaned dataset not found: {DATA_PATH}")
    st.info(
        "Run notebooks/02_data_cleaning.ipynb first to generate "
        "data/processed/city_day_cleaned.csv."
    )
    st.stop()

df = load_data(str(DATA_PATH))

if df.empty or df["AQI"].notna().sum() == 0:
    st.error("The dataset contains no usable AQI observations.")
    st.stop()


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🌍 India Air Quality Explorer")
st.markdown(
    '<p class="subtitle">Explore historical air quality, city-level patterns, '
    'seasonality, and pollutant measurements across India.</p>',
    unsafe_allow_html=True,
)

st.caption(
    f"Dataset period: {df['Date'].min():%d %b %Y} – "
    f"{df['Date'].max():%d %b %Y} | "
    f"{df['City'].nunique()} cities"
)


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.title("Explore the data")
st.sidebar.caption("Choose a location and time period.")

all_cities = sorted(df["City"].dropna().unique().tolist())
selected_cities = st.sidebar.multiselect(
    "Cities",
    options=all_cities,
    default=all_cities,
)

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if len(date_range) != 2:
    st.warning("Select both a start date and an end date.")
    st.stop()

start_date, end_date = date_range

if start_date > end_date:
    st.error("The start date must be before the end date.")
    st.stop()

filtered = df[
    df["City"].isin(selected_cities)
    & df["Date"].dt.date.between(start_date, end_date)
].copy()

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

aqi_data = filtered.dropna(subset=["AQI"]).copy()

if aqi_data.empty:
    st.warning("No AQI observations are available for these filters.")
    st.stop()


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
average_aqi = aqi_data["AQI"].mean()
median_aqi = aqi_data["AQI"].median()
maximum_aqi = aqi_data["AQI"].max()
observation_count = len(aqi_data)

k1, k2, k3, k4 = st.columns(4)

k1.metric("Average AQI", f"{average_aqi:,.1f}")
k2.metric("Median AQI", f"{median_aqi:,.1f}")
k3.metric("Highest recorded AQI", f"{maximum_aqi:,.0f}")
k4.metric("AQI observations", f"{observation_count:,}")

st.caption(
    "These are descriptive statistics for the selected records, "
    "not a real-time air-quality reading or a health advisory."
)

st.divider()


# --------------------------------------------------
# AQI TREND OVER TIME
# --------------------------------------------------
st.subheader("📈 AQI over time")

daily_trend = (
    aqi_data.groupby(["Date", "City"], as_index=False)["AQI"]
    .mean()
)

trend_fig = px.line(
    daily_trend,
    x="Date",
    y="AQI",
    color="City",
    title="Daily AQI by city",
    labels={"AQI": "Air Quality Index", "Date": "Date"},
    template="plotly_dark",
)

trend_fig.update_layout(
    height=480,
    legend_title_text="City",
    hovermode="x unified",
    margin=dict(l=15, r=15, t=60, b=15),
)

st.plotly_chart(trend_fig, width="stretch")


# --------------------------------------------------
# CITY COMPARISON
# --------------------------------------------------
left, right = st.columns(2)

with left:
    st.subheader("🏙️ City comparison")

    city_summary = (
        aqi_data.groupby("City")["AQI"]
        .agg(Average_AQI="mean", Observations="count")
        .reset_index()
        .sort_values("Average_AQI", ascending=False)
    )

    city_fig = px.bar(
        city_summary,
        x="Average_AQI",
        y="City",
        orientation="h",
        color="Average_AQI",
        color_continuous_scale="Turbo",
        hover_data=["Observations"],
        title="Average AQI by city",
        labels={"Average_AQI": "Average AQI"},
        template="plotly_dark",
    )

    city_fig.update_layout(
        height=max(400, len(city_summary) * 25),
        yaxis={"categoryorder": "total ascending"},
        coloraxis_showscale=False,
    )

    st.plotly_chart(city_fig, use_container_width=True)

with right:
    st.subheader("🌦️ Seasonal patterns")

    season_order = ["Winter", "Summer", "Monsoon", "Post-Monsoon"]

    seasonal = (
        aqi_data.groupby("Season", as_index=False)
        .agg(Average_AQI=("AQI", "mean"), Observations=("AQI", "count"))
    )

    seasonal["Season"] = pd.Categorical(
        seasonal["Season"], categories=season_order, ordered=True
    )
    seasonal = seasonal.sort_values("Season")

    season_fig = px.bar(
        seasonal,
        x="Season",
        y="Average_AQI",
        color="Average_AQI",
        color_continuous_scale="Blues",
        hover_data=["Observations"],
        title="Average AQI by calendar season",
        labels={"Average_AQI": "Average AQI"},
        template="plotly_dark",
    )

    season_fig.update_layout(
        height=450,
        coloraxis_showscale=False,
    )

    st.plotly_chart(season_fig, use_container_width=True)

st.caption(
    "Season labels use simplified calendar-month groupings. "
    "Seasonality can vary across Indian regions."
)

st.divider()


# --------------------------------------------------
# POLLUTANT ANALYSIS
# --------------------------------------------------
st.subheader("🧪 Pollutant measurements")

pollutants = [
    column
    for column in [
        "PM2.5", "PM10", "NO", "NO2", "NOx",
        "NH3", "CO", "SO2", "O3", "Benzene",
        "Toluene", "Xylene",
    ]
    if column in filtered.columns
]

if pollutants:
    selected_pollutant = st.selectbox(
        "Choose a pollutant",
        pollutants,
    )

    pollutant_data = filtered.dropna(subset=[selected_pollutant])

    pollutant_fig = px.line(
        pollutant_data.groupby(["Date", "City"], as_index=False)[
            selected_pollutant
        ].mean(),
        x="Date",
        y=selected_pollutant,
        color="City",
        title=f"{selected_pollutant} measurements over time",
        labels={selected_pollutant: "Recorded concentration"},
        template="plotly_dark",
    )

    pollutant_fig.update_layout(
        height=420,
        hovermode="x unified",
    )

    st.plotly_chart(pollutant_fig, use_container_width=True)
else:
    st.info("No recognized pollutant columns are available.")


# --------------------------------------------------
# DATA TABLE AND DOWNLOAD
# --------------------------------------------------
with st.expander("View filtered data"):
    display_columns = [
        column
        for column in [
            "City", "Date", "AQI", "AQI_Bucket",
            "PM2.5", "PM10", "NO2", "CO", "SO2", "O3",
        ]
        if column in filtered.columns
    ]

    st.dataframe(
        filtered[display_columns].sort_values("Date", ascending=False),
        use_container_width=True,
        hide_index=True,
    )

    csv_data = filtered[display_columns].to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download filtered data (CSV)",
        data=csv_data,
        file_name="india_air_quality_filtered.csv",
        mime="text/csv",
    )


# --------------------------------------------------
# METHODOLOGY AND LIMITATIONS
# --------------------------------------------------
with st.expander("Methodology and limitations"):
    st.markdown(
        """
        - **Historical data:** This dashboard uses the local cleaned dataset,
          not live monitoring data.
        - **Missing AQI:** Rows without AQI are excluded from AQI statistics.
        - **Imputation:** The cleaned dataset may contain pollutant values
          imputed using city medians. These values are not original
          measurements and can affect pollutant trends.
        - **City comparisons:** Cities may have different observation counts
          and periods, so average AQI comparisons should be interpreted
          cautiously.
        - **Extreme values:** Unusually high recorded AQI values are retained
          unless explicitly addressed during data preparation.
        - **Interpretation:** These charts describe patterns and associations;
          they do not establish causation.
        """
    )

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#94a3b8; padding:12px;">
        India Air Quality Explorer · Built with Python, Pandas, and Plotly
    </div>
    """,
    unsafe_allow_html=True,
)
