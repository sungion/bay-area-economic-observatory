import pandas as pd


def calculate_correlation(
    df,
    variable_x,
    variable_y
):
    """
    Calculate Pearson correlation between two variables.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset containing the variables.
    variable_x : str
        First variable.
    variable_y : str
        Second variable.

    Returns
    -------
    float
        Pearson correlation coefficient.
    """

    correlation = df[
        [variable_x, variable_y]
    ].corr().iloc[0, 1]

    return correlation


def merge_income_and_commute(
    income_df,
    commute_df
):
    """
    Combine county-level income and commute datasets.
    """

    merged_df = pd.merge(
        income_df[
            ["County", "Median Household Income"]
        ],
        commute_df[
            ["County", "Mean Commute Time"]
        ],
        on="County",
        how="inner"
    )

    return merged_df
