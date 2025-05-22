from datetime import datetime

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.models import Base, SensorData, SensorDataIn

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/data")
async def receive_data(data: SensorDataIn, db: Session = Depends(get_db)):
    try:
        new_data = SensorData(
            sensor_id=data.sensor_id,
            temperature=data.temperature,
            pressure=data.pressure,
            timestamp=datetime.fromtimestamp(data.timestamp),
        )
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return {"status": "success", "id": new_data.id}
    except Exception as e:
        return {"error": str(e)}
