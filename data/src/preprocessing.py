import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """CSV 파일을 로드하는 간단한 함수."""
    df = pd.read_csv(path)
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """결측치 처리 + 파생 변수 생성."""
    df = df.copy()
    df = df.fillna(0)

    # 사용 비율 파생 변수
    df["usage_ratio"] = df["mileage"] / (df["engine_hours"] + 1)

    return df

if __name__ == "__main__":
    df_logs = load_data("data/vehicle_logs_mock.csv")
    df_processed = preprocess(df_logs)
    print(df_processed.head())
