import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.fillna(0)
    return df
