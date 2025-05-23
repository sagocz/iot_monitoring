from sqlalchemy.orm import Session
from db_layer.repositories.sensor_data_repository import SensorDataRepository
from db_layer.schemas.sensor_data import SensorDataIn


class SensorDataService:
    def __init__(self, db: Session):
        self.repo = SensorDataRepository(db)

    def create_sensor_data(self, data: SensorDataIn):
        return self.repo.create(data)

    def get_last_sensor_data(self, limit: int = 12):
        return self.repo.get_last(limit)
