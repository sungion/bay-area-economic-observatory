import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bay Area Economic Observatory",
    page_icon="📊",
    layout="wide"
)

# =========================
# TITLE
# =========================

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
    st.metric("Data Coverage", "2019–2026")


# =========================
# BART DATA
# =========================

st.divider()

st.header("🚇 BART Ridership")

st.write(
    """
    BART ridership is measured by average weekday exits
    from all BART stations.
    """
)

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


# =========================
# BART GRAPH
# =========================

st.subheader("Average Weekday BART Station Exits")

st.line_chart(
    bart_df.set_index("Month")
)

st.caption(
    "Source: Metropolitan Transportation Commission (MTC). "
    "Data represents average weekday BART station exits."
)


# =========================
# BART YEAR COMPARISON
# =========================

st.divider()

st.subheader("📊 Compare BART Ridership Across Years")

comparison_year = st.selectbox(
    "Choose a comparison year:",
    ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]
)

latest_row = bart_df["2026"].last_valid_index()
latest_month = bart_df.loc[latest_row, "Month"]

latest = bart_df.loc[latest_row, "2026"]
comparison = bart_df.loc[latest_row, comparison_year]

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


# =========================
# BAY BRIDGE DATA
# =========================

st.divider()

st.header("🚗 Bay Bridge Traffic")

st.write(
    """
    The San Francisco–Oakland Bay Bridge data measures one-way
    toll-direction vehicle crossings.
    """
)

bridge_data = {
    "Month": months,

    "2019": [
        3913767, 3587902, 4058925, 3976731,
        4040558, 4006902, 4063748, 4113916,
        3948426, 4047327, 3847809, 3882964
    ],

    "2020": [
        3878683, 3722539, 2882649, 1996243,
        2673380, 3036424, 3294706, 3382756,
        3282056, 3504554, 3192647, 3111694
    ],

    "2021": [
        3041330, 2989816, 3532498, 3522492,
        3671838, 3673837, 3803940, 3737917,
        3618241, 3700292, 3546027, 3529143
    ],

    "2022": [
        3325322, 3286568, 3717879, 3634689,
        3729564, 3622401, 3739359, 3803975,
        3649505, 3754261, 3513877, 3513520
    ],

    "2023": [
        3383633, 3199618, 3568295, 3649730,
        3763446, 3673225, 3711557, 3795223,
        3613710, 3686944, 3399365, 3573283
    ],

    "2024": [
        3462422, 3332318, 3650729, 3650435,
        3706897, 3619233, 3710452, 3754439,
        3597563, 3705411, 3439752, 3559559
    ],

    "2025": [
        3527140, 3239106, 3641671, 3610238,
        3702144, 3581985, 3687703, 3703249,
        3547272, 3691034, 3477742, 3551661
    ],

    "2026": [
        3493358, 3263952, 3664123, 3510030,
        3659694, 3585866, None, None,
        None, None, None, None
    ]
}

bridge_df = pd.DataFrame(bridge_data)


# =========================
# BAY BRIDGE GRAPH
# =========================

st.subheader("Bay Bridge Crossings Over Time")

st.line_chart(
    bridge_df.set_index("Month")
)

st.caption(
    "Source: Metropolitan Transportation Commission (MTC). "
    "Measure: one-way toll-direction vehicle crossings."
)


# =========================
# BART VS BAY BRIDGE
# =========================

st.divider()

st.header("🚇 vs. 🚗 Transportation Recovery")

st.write(
    """
    Compare how public transit and automobile traffic have recovered
    relative to the same month in a previous year.
    """
)

recovery_year = st.selectbox(
    "Choose a recovery comparison year:",
    ["2019", "2020", "2021", "2022", "2023", "2024", "2025"],
    index=0,
    key="recovery_year"
)

# 2026 data currently extends through June
latest_row = bart_df["2026"].last_valid_index()
latest_month = bart_df.loc[latest_row, "Month"]

# Get BART values
bart_2026 = bart_df.loc[
    bart_df["Month"] == latest_month, "2026"
].iloc[0]

bart_comparison = bart_df.loc[
    bart_df["Month"] == latest_month, recovery_year
].iloc[0]

# Get Bay Bridge values
bridge_2026 = bridge_df.loc[
    bridge_df["Month"] == latest_month, "2026"
].iloc[0]

bridge_comparison = bridge_df.loc[
    bridge_df["Month"] == latest_month, recovery_year
].iloc[0]

# Calculate recovery percentages
bart_recovery = (bart_2026 / bart_comparison) * 100
bridge_recovery = (bridge_2026 / bridge_comparison) * 100

# Calculate percentage changes
bart_change = bart_recovery - 100
bridge_change = bridge_recovery - 100

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🚇 BART Recovery",
        f"{bart_recovery:.1f}%",
        f"{bart_change:+.1f}% vs. {recovery_year}"
    )

with col2:
    st.metric(
        "🚗 Bay Bridge Recovery",
        f"{bridge_recovery:.1f}%",
        f"{bridge_change:+.1f}% vs. {recovery_year}"
    )

st.write(
    f"""
    In **{latest_month} 2026**, BART average weekday station exits
    were **{bart_recovery:.1f}%** of the {recovery_year}
    level for the same month.

    Bay Bridge traffic was **{bridge_recovery:.1f}%** of its
    {recovery_year} level for the same month.
    """
)

st.caption(
    f"Comparison uses {latest_month} because it is the latest month "
    "currently available in the 2026 dataset."
)

# =========================
# BAY AREA ECONOMIC INDICATORS
# =========================

st.divider()

st.header("💰 Bay Area Economic Indicators")

st.write(
    """
    Median household income provides economic context for
    transportation patterns across the Bay Area's nine counties.
    Data is retrieved directly from the U.S. Census Bureau's
    American Community Survey.
    """
)

# 9-county Bay Area FIPS codes
counties = {
    "Alameda": "001",
    "Contra Costa": "013",
    "Marin": "041",
    "Napa": "055",
    "San Francisco": "075",
    "San Mateo": "081",
    "Santa Clara": "085",
    "Solano": "095",
    "Sonoma": "097"
}

# Census API key stored securely in Streamlit Secrets
census_key = st.secrets["CENSUS_API_KEY"]

# Census API URL
url = (
    "https://api.census.gov/data/2024/acs/acs5"
    "?get=NAME,B19013_001E"
    "&for=county:*"
    "&in=state:06"
    f"&key={census_key}"
)

try:
    census_response = pd.read_json(url)

    # First row contains column names
    census_response.columns = census_response.iloc[0]
    census_response = census_response.iloc[1:].reset_index(drop=True)

    # Keep only the nine Bay Area counties
    income_df = census_response[
        census_response["county"].isin(counties.values())
    ].copy()

    # Map FIPS codes to county names
    fips_to_county = {
        value: key for key, value in counties.items()
    }

    income_df["County"] = income_df["county"].map(fips_to_county)

    # Convert income to numbers
    income_df["Median Household Income"] = pd.to_numeric(
        income_df["B19013_001E"],
        errors="coerce"
    )

    # Sort alphabetically
    income_df = income_df.sort_values("County")

    # -------------------------
    # Chart
    # -------------------------

    st.subheader("Median Household Income by County")

    chart_data = income_df.set_index("County")[
        ["Median Household Income"]
    ]

    st.bar_chart(chart_data)

    # -------------------------
    # County selector
    # -------------------------

    selected_county = st.selectbox(
        "Select a county:",
        income_df["County"].tolist(),
        key="income_county"
    )

    selected_income = income_df.loc[
        income_df["County"] == selected_county,
        "Median Household Income"
    ].iloc[0]

    st.metric(
        f"{selected_county} County Median Household Income",
        f"${selected_income:,.0f}"
    )

    st.caption(
        "Source: U.S. Census Bureau, 2024 American Community Survey "
        "(ACS 5-Year Estimates), Table B19013."
    )

except Exception as e:
    st.error(
        "The Census data could not be loaded. "
        "Check that your Census API key is configured correctly "
        "in Streamlit Secrets."
    )
# =========================
# COMMUTING PATTERNS
# =========================

st.divider()

st.header("🚗 Commuting Patterns")

st.write(
    """
    Mean travel time to work provides context for transportation
    demand and regional differences across the Bay Area.
    """
)

# Census DP03:
# DP03_0025E = Mean travel time to work (minutes)

commute_url = (
    "https://api.census.gov/data/2024/acs/acs5/profile"
    "?get=NAME,DP03_0025E"
    "&for=county:*"
    "&in=state:06"
    f"&key={census_key}"
)

try:
    commute_response = pd.read_json(commute_url)

    commute_response.columns = commute_response.iloc[0]
    commute_response = commute_response.iloc[1:].reset_index(drop=True)

    commute_df = commute_response[
        commute_response["county"].isin(counties.values())
    ].copy()

    commute_df["County"] = commute_df["county"].map(
        fips_to_county
    )

    commute_df["Mean Commute Time"] = pd.to_numeric(
        commute_df["DP03_0025E"],
        errors="coerce"
    )

    commute_df = commute_df.sort_values("County")

    st.subheader("Average Commute Time by County")

    commute_chart = commute_df.set_index("County")[
        ["Mean Commute Time"]
    ]

    st.bar_chart(commute_chart)

    selected_commute_county = st.selectbox(
        "Select a county:",
        commute_df["County"].tolist(),
        key="commute_county"
    )

    selected_commute = commute_df.loc[
        commute_df["County"] == selected_commute_county,
        "Mean Commute Time"
    ].iloc[0]

    st.metric(
        f"{selected_commute_county} County Mean Commute",
        f"{selected_commute:.1f} minutes"
    )

    st.caption(
        "Source: U.S. Census Bureau, 2024 American Community Survey "
        "(ACS 5-Year Estimates), Data Profile DP03."
    )

except Exception as e:
    st.error(
        "The Census commute data could not be loaded."
    )

# =========================
# INCOME VS. COMMUTE TIME
# =========================

st.divider()

st.header("📈 Income vs. Commute Time")

st.write(
    """
    This analysis examines whether median household income is associated
    with average commute time across the nine Bay Area counties.
    Each point represents one county.
    """
)

# Merge income and commute datasets
analysis_df = pd.merge(
    income_df[["County", "Median Household Income"]],
    commute_df[["County", "Mean Commute Time"]],
    on="County"
)

st.subheader("County-Level Relationship")

st.scatter_chart(
    analysis_df,
    x="Median Household Income",
    y="Mean Commute Time"
)

# Calculate correlation
correlation = analysis_df[
    ["Median Household Income", "Mean Commute Time"]
].corr().iloc[0, 1]

st.metric(
    "Income–Commute Correlation",
    f"{correlation:.2f}"
)

st.caption(
    "Correlation measures the linear association between median household "
    "income and mean commute time across the nine Bay Area counties. "
    "Correlation does not imply causation."
)

st.dataframe(
    analysis_df,
    use_container_width=True,
    hide_index=True
)
