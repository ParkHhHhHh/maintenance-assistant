from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI(title="Military Vehicle Maintenance Assistant API")

class VehicleStatus(BaseModel):
    mileage: float
    engine_hours: float
    temperature: float

@app.get("/")
def root():
    return {"status": "API Running"}

@app.post("/predict")
def get_prediction(data: VehicleStatus):
    usage_ratio = data.mileage / (data.engine_hours + 1)
    response = predict({
        "mileage": data.mileage,
        "engine_hours": data.engine_hours,
        "temperature": data.temperature,
        "usage_ratio": usage_ratio,
        "temp_stress": 1 if data.temperature > 32 else 0
    })
    return {
        "predicted_days_until_next_maintenance": float(response)
    }
