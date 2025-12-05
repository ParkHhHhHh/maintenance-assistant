from predict import predict

def test_prediction_output():
    sample = {
        "mileage": 10000,
        "engine_hours": 300,
        "temperature": 30,
        "usage_ratio": 10000/301,
        "temp_stress": 0
    }
    output = predict(sample)
    assert isinstance(output, float)
