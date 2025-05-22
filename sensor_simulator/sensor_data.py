from dataclasses import dataclass

@dataclass
class SensorData:
    sensor_id: int
    timestamp: float
    temperature: float
    pressure: float