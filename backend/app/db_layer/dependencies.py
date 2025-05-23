from fastapi import Depends
from sqlalchemy.orm import Session
from db_layer.repositories.sensor_data_repository import SensorDataRepository
from core.database import get_db


def get_sensor_data_repository(db: Session = Depends(get_db)) -> SensorDataRepository:
    return SensorDataRepository(db)
