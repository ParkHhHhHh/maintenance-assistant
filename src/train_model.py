from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
from preprocessing import load_data, preprocess
from feature_engineering import add_features

def train():
    df = load_data("data/vehicle_logs_mock.csv")
    df = preprocess(df)
    df = add_features(df)

    X = df[["mileage", "engine_hours", "usage_ratio", "temp_stress"]]
    y = df["days_until_maintenance"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    print("Model score:", model.score(X_test, y_test))

    joblib.dump(model, "model.pkl")
    print("Model saved → model.pkl")

if __name__ == "__main__":
    train()
