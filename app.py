import streamlit as st

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

st.header("Transportation in the Bay Area")

st.write(
    """
    This project examines transportation, economic activity, and
    regional differences across the San Francisco Bay Area using
    publicly available data.
    """
)

st.info(
    "Research focus: Why do transportation costs and service patterns "
    "differ between the Bay Area, Seoul, and Portland?"
)

st.divider()

st.header("BART Ridership")

st.write(
    "BART ridership is one indicator of transportation activity "
    "in the Bay Area."
)

st.info(
    "Official transportation data will be integrated here."
)
