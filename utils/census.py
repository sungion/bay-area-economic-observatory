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
