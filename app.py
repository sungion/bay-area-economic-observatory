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

st.subheader("Latest Available Data")

latest = bart_df["2026"].dropna().iloc[-1]

st.metric(
    "June 2026 Average Weekday Exits",
    f"{latest:,.0f}"
)

st.write(
    "MTC's latest available monthly data currently extends through June 2026."
)
