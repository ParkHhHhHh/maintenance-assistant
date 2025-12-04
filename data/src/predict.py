import joblib
import pandas as pd

def load_model(path: str = "model.pkl"):
    return joblib.load(path)

def predict(input_dict: dict) -> float:
    model = load_model()
    df = pd.DataFrame([input_dict])
    result = model.predict(df)[0]
    return float(result)

if __name__ == "__main__":
    sample = {
        "mileage": 10000,
        "engine_hours": 300,
        "usage_ratio": 10000 / (300 + 1),
    }
    print(predict(sample))
