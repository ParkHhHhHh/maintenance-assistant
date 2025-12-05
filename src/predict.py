import joblib
import pandas as pd
from feature_engineering import add_features
from preprocessing import preprocess

def predict(input_dict: dict):
    model = joblib.load("model.pkl")
    df = pd.DataFrame([input_dict])
    df = preprocess(df)
    df = add_features(df)
    X = df[["mileage", "engine_hours", "usage_ratio", "temp_stress"]]
    return model.predict(X)[0]
