import pandas as pd
import streamlit as st


BAY_AREA_COUNTIES = {
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


def get_census_key():
    return st.secrets["CENSUS_API_KEY"]


def get_income_data():
    key = get_census_key()

    url = (
        "https://api.census.gov/data/2024/acs/acs5"
        "?get=NAME,B19013_001E"
        "&for=county:*"
        "&in=state:06"
        f"&key={key}"
    )

    response = pd.read_json(url)

    response.columns = response.iloc[0]
    response = response.iloc[1:].reset_index(drop=True)

    df = response[
        response["county"].isin(BAY_AREA_COUNTIES.values())
    ].copy()

    fips_to_county = {
        value: name
        for name, value in BAY_AREA_COUNTIES.items()
    }

    df["County"] = df["county"].map(fips_to_county)

    df["Median Household Income"] = pd.to_numeric(
        df["B19013_001E"],
        errors="coerce"
    )

    return df[
        ["County", "Median Household Income"]
    ].sort_values("County")


def get_commute_data():
    key = get_census_key()

    url = (
        "https://api.census.gov/data/2024/acs/acs5/profile"
        "?get=NAME,DP03_0025E"
        "&for=county:*"
        "&in=state:06"
        f"&key={key}"
    )

    response = pd.read_json(url)

    response.columns = response.iloc[0]
    response = response.iloc[1:].reset_index(drop=True)

    df = response[
        response["county"].isin(BAY_AREA_COUNTIES.values())
    ].copy()

    fips_to_county = {
        value: name
        for name, value in BAY_AREA_COUNTIES.items()
    }

    df["County"] = df["county"].map(fips_to_county)

    df["Mean Commute Time"] = pd.to_numeric(
        df["DP03_0025E"],
        errors="coerce"
    )

    return df[
        ["County", "Mean Commute Time"]
    ].sort_values("County")

def get_transportation_mode_data():
    key = get_census_key()

    url = (
        "https://api.census.gov/data/2024/acs/acs5"
        "?get=NAME,B08301_001E,B08301_003E,B08301_004E,"
        "B08301_010E,B08301_018E"
        "&for=county:*"
        "&in=state:06"
        f"&key={key}"
    )

    response = pd.read_json(url)

    response.columns = response.iloc[0]
    response = response.iloc[1:].reset_index(drop=True)

    df = response[
        response["county"].isin(BAY_AREA_COUNTIES.values())
    ].copy()

    fips_to_county = {
        value: name
        for name, value in BAY_AREA_COUNTIES.items()
    }

    df["County"] = df["county"].map(fips_to_county)

    # Total workers
    df["Total Workers"] = pd.to_numeric(
        df["B08301_001E"],
        errors="coerce"
    )

    # Drive alone
    df["Drive Alone"] = pd.to_numeric(
        df["B08301_003E"],
        errors="coerce"
    )

    # Carpooled
    df["Carpooled"] = pd.to_numeric(
        df["B08301_004E"],
        errors="coerce"
    )

    # Public transportation
    df["Public Transportation"] = pd.to_numeric(
        df["B08301_010E"],
        errors="coerce"
    )

    # Worked at home
    df["Worked at Home"] = pd.to_numeric(
        df["B08301_018E"],
        errors="coerce"
    )

    # Convert counts to percentages
    df["Drive Alone (%)"] = (
        df["Drive Alone"] / df["Total Workers"] * 100
    )

    df["Carpooled (%)"] = (
        df["Carpooled"] / df["Total Workers"] * 100
    )

    df["Public Transportation (%)"] = (
        df["Public Transportation"]
        / df["Total Workers"]
        * 100
    )

    df["Worked at Home (%)"] = (
        df["Worked at Home"]
        / df["Total Workers"]
        * 100
    )

    return df[
        [
            "County",
            "Drive Alone (%)",
            "Carpooled (%)",
            "Public Transportation (%)",
            "Worked at Home (%)"
        ]
    ].sort_values("County")
