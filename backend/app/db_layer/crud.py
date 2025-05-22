from datetime import datetime

from sqlalchemy.orm import Session

from app_models.db_models import SensorData
from app_models.schemas import SensorDataIn

def create_sensor_data(db: Session, data: SensorDataIn):
    new_data = SensorData(
        sensor_id=data.sensor_id,
        temperature=data.temperature,
        pressure=data.pressure,
        timestamp=datetime.fromtimestamp(data.timestamp),
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def get_last_sensor_data(db: Session, limit: int = 12):
    data = db.query(SensorData).order_by(SensorData.timestamp.desc()).limit(limit).all()
    return list(reversed(data))
