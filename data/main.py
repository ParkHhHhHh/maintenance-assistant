from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI(title="Military Vehicle Maintenance Assistant API")

class VehicleStatus(BaseModel):
    mileage: float
    engine_hours: float

@app.get("/")
def root():
    return {"status": "Maintenance Assistant API Running"}

@app.post("/predict")
def get_prediction(status: VehicleStatus):
    usage_ratio = status.mileage / (status.engine_hours + 1)
    result = predict({
        "mileage": status.mileage,
        "engine_hours": status.engine_hours,
        "usage_ratio": usage_ratio
    })
    return {
        "predicted_days_until_maintenance": result
    }
