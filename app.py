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

transportation_df = pd.read_csv(
    "data/transportation.csv"
)

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

st.subheader("📊 Compare BART Ridership Across Years")

comparison_year = st.selectbox(
    "Choose a comparison year:",
    ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]
)

latest_row = bart_df["2026"].last_valid_index()
latest_month = bart_df.loc[latest_row, "Month"]

latest = bart_df.loc[latest_month, "2026"]
comparison = bart_df.loc[latest_month, comparison_year]

change = latest - comparison
percent_change = (change / comparison) * 100
recovery = (latest / comparison) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Latest Ridership",
        f"{latest:,.0f}"
    )

with col2:
    st.metric(
        f"Change vs. {comparison_year}",
        f"{percent_change:+.1f}%"
    )

with col3:
    st.metric(
        f"% of {comparison_year} Level",
        f"{recovery:.1f}%"
    )

st.write(
    f"""
    In **{latest_month} 2026**, average weekday BART station
    exits were **{latest:,.0f}**.

    In the same month of **{comparison_year}**, there were
    **{comparison:,.0f}** average weekday station exits.

    This represents a **{percent_change:+.1f}%** change relative to
    {comparison_year}.
    """
)

st.divider()

st.header("🚗 Bay Bridge Traffic")

st.write(
    """
    The San Francisco–Oakland Bay Bridge data measures one-way
    toll-direction vehicle crossings.
    """
)

transportation_df = pd.read_csv(
    "data/transportation.csv"
)

bridge_df = pd.DataFrame(bridge_data)

st.subheader("Bay Bridge Crossings Over Time")

st.line_chart(
    bridge_df.set_index("Month")
)

st.caption(
    "Source: Metropolitan Transportation Commission (MTC). "
    "Measure: one-way toll-direction vehicle crossings."
)

st.divider()

st.header("🚇 vs. 🚗 Transportation Recovery")

st.write(
    """
    How has public transit recovery compared with automobile traffic
    since the COVID-19 pandemic?
    """
)

comparison_month = st.selectbox(
    "Choose a month:",
    bridge_df["Month"],
    index=5
)

bart_value = bart_df.loc[
    bart_df["Month"] == comparison_month, "2026"
].iloc[0]

bart_2019 = bart_df.loc[
    bart_df["Month"] == comparison_month, "2019"
].iloc[0]

bridge_value = bridge_df.loc[
    bridge_df["Month"] == comparison_month, "2026"
].iloc[0]

bridge_2019 = bridge_df.loc[
    bridge_df["Month"] == comparison_month, "2019"
].iloc[0]

bart_recovery = (bart_value / bart_2019) * 100
bridge_recovery = (bridge_value / bridge_2019) * 100

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🚇 BART Recovery",
        f"{bart_recovery:.1f}%",
        f"{bart_recovery - 100:+.1f}% vs. 2019"
    )

with col2:
    st.metric(
        "🚗 Bay Bridge Recovery",
        f"{bridge_recovery:.1f}%",
        f"{bridge_recovery - 100:+.1f}% vs. 2019"
    )

st.write(
    f"""
    For **{comparison_month} 2026**, BART ridership was
    **{bart_recovery:.1f}%** of its {comparison_month} 2019 level,
    while Bay Bridge traffic was **{bridge_recovery:.1f}%** of its
    {comparison_month} 2019 level.
    """
)
