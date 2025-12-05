import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["usage_ratio"] = df["mileage"] / (df["engine_hours"] + 1)
    df["temp_stress"] = df["temperature"].apply(lambda x: 1 if x > 32 else 0)
    return df
