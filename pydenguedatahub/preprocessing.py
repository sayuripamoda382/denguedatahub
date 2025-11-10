import pandas as pd

def preprocess_srilanka_weekly(df):
    """
    Preprocess Sri Lanka weekly dengue dataset.

    Returns:
        national_weekly (DataFrame): weekly national cases with a 'date' column
        district_weekly (DataFrame): weekly district cases with a 'date' column
        national_yearly (DataFrame): yearly national aggregated cases
        district_yearly (DataFrame): yearly district aggregated cases
    """
    df = df.copy()

    # Convert dates to datetime
    df["start.date"] = pd.to_datetime(df["start.date"])
    df["end.date"] = pd.to_datetime(df["end.date"])

    # Weekly National
    national_weekly = df.groupby("start.date", as_index=False)["cases"].sum()

    # Weekly District
    district_weekly = df.groupby(["district", "start.date"], as_index=False)["cases"].sum()

    # Yearly National
    national_yearly = df.groupby("year", as_index=False)["cases"].sum()

    # Yearly District
    district_yearly = df.groupby(["year", "district"], as_index=False)["cases"].sum()

    return national_weekly, district_weekly, national_yearly, district_yearly
