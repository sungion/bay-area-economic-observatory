import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bay Area Economic Observatory",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Bay Area Economic Observatory")

st.caption(
    "Tracking economic and transportation trends across the San Francisco Bay Area"
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Region", "9 Counties")

with col2:
    st.metric("Focus", "Transportation")

with col3:
    st.metric("Data Coverage", "2019–Present")

st.divider()

st.header("🚇 BART Ridership")

st.write(
    """
    BART ridership is measured by the average weekday exits
    from all BART stations.
    """
)

# BART data from MTC
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

bart_data = {
    "Month": months,
    "2019": [
        395860, 407337, 409515, 414397,
        412165, 413521, 401465, 410854,
        426755, 420277, 411183, 376551
    ],
    "2020": [
        388910, 404552, 166574, 25136,
        29878, 40979, 45633, 46020,
        48838, 53255, 52198, 45893
    ],
    "2021": [
        43012, 47665, 51596, 57886,
        64934, 75963, 85291, 92402,
        105997, 109781, 112282, 102993
    ],
    "2022": [
        85463, 105374, 124094, 132181,
        135824, 140564, 133858, 144008,
        161902, 159099, 150242, 130283
    ],
    "2023": [
        134140, 151390, 151150, 159696,
        159918, 158361, 154825, 166637,
        172051, 171277, 165802, 144070
    ],
    "2024": [
        151854, 162186, 162459, 163267,
        168356, 164743, 159220, 165764,
        184248, 180834, 166035, 156466
    ],
    "2025": [
        162938, 171856, 174538, 181466,
        170293, 183481, 172984, 186515,
        189810, 196331, 173574, 159537
    ],
    "2026": [
        170543, 178379, 188231, 201256,
        196692, 206689, None, None,
        None, None, None, None
    ]
}

bart_df = pd.DataFrame(bart_data)

st.subheader("Average Weekday BART Station Exits")

st.line_chart(
    bart_df.set_index("Month")
)

st.caption(
    "Source: Metropolitan Transportation Commission (MTC). "
    "Data represents average weekday BART station exits."
)

st.divider()

st.subheader("📊 BART Recovery Compared With 2019")

# Latest available month
latest_month_index = bart_df["2026"].last_valid_index()

latest = bart_df.loc[latest_month_index, "2026"]
baseline = bart_df.loc[latest_month_index, "2019"]

change = latest - baseline
percent_change = (change / baseline) * 100
recovery = (latest / baseline) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Latest Ridership",
        f"{latest:,.0f}"
    )

with col2:
    st.metric(
        "Change vs. 2019",
        f"{percent_change:.1f}%"
    )

with col3:
    st.metric(
        "2019 Level Reached",
        f"{recovery:.1f}%"
    )

st.write(
    f"""
    In **{latest_month_index}**, average weekday BART station exits
    were **{latest:,.0f}**.

    The same month in 2019 had **{baseline:,.0f}** average weekday
    station exits.

    This means current ridership is **{recovery:.1f}%** of the
    comparable 2019 level.
    """
)
