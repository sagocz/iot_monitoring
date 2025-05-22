from pydantic import BaseModel

class SensorDataIn(BaseModel):
    sensor_id: int
    timestamp: float
    temperature: float
    pressure: float