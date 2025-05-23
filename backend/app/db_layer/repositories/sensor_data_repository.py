from sqlalchemy.orm import Session
from datetime import datetime
from db_layer.models import SensorData
from db_layer.schemas.sensor_data import SensorDataIn

class SensorDataRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: SensorDataIn) -> SensorData:
        obj = SensorData(
            sensor_id=data.sensor_id,
            temperature=data.temperature,
            pressure=data.pressure,
            timestamp=datetime.fromtimestamp(data.timestamp)
        )
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_last(self, limit: int = 12) -> list[SensorData]:
        return list(
            reversed(
                self.db.query(SensorData)
                       .order_by(SensorData.timestamp.desc())
                       .limit(limit)
                       .all()
            )
        )
