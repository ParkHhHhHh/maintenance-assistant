from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
from preprocessing import load_data, preprocess

def train_model():
    df = load_data("data/vehicle_logs_mock.csv")
    df = preprocess(df)

    X = df[["mileage", "engine_hours", "usage_ratio"]]
    y = df["days_until_maintenance"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model R^2 score: {score:.3f}")

    joblib.dump(model, "model.pkl")
    print("Model saved as model.pkl")

if __name__ == "__main__":
    train_model()
