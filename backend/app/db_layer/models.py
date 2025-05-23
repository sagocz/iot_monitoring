from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime

from db_layer.base import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, nullable=False)
    temperature = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
