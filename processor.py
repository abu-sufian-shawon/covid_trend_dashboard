import pandas as pd
import numpy as np

def process_data(raw_json):
    timeline = raw_json["timeline"]

    df = pd.DataFrame({
        "date": timeline["cases"].keys(),
        "cases": timeline["cases"].values(),
        "deaths": timeline["deaths"].values(),
        "recovered": timeline["recovered"].values()
    })

    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    df["daily_cases"] = df["cases"].diff().fillna(0)
    df["daily_deaths"] = df["deaths"].diff().fillna(0)
    df["daily_recovered"] = df["recovered"].diff().fillna(0)

    df["cases_7day_avg"] = df["daily_cases"].rolling(7).mean()
    df["growth_rate"] = (df["daily_cases"] / df["cases"].shift(1)) * 100

    df.replace([np.inf, -np.inf], 0, inplace=True)
    df.fillna(0, inplace=True)

    return df
