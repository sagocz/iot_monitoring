from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

class SensorData(BaseModel):
    sensor_id: int
    timestamp: datetime
    temperature: float
    pressure: float

@app.post("/data")
async def receive_data(data: SensorData):
    print(f"Received data: {data}")
    # TODO: Save to database later
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "ok"}