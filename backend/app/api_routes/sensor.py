from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db_layer import crud
from db_layer.session import get_db
from app_models.schemas import SensorDataIn

router = APIRouter()

@router.post("/data")
async def receive_data(data: SensorDataIn, db: Session = Depends(get_db)):
    try:
        new_data = crud.create_sensor_data(db, data)
        return {"status": "success", "id": new_data.id}
    except Exception as e:
        return {"error": str(e)}

@router.get("/plot-data")
def get_plot_data(db: Session = Depends(get_db)):
    data = crud.get_last_sensor_data(db)
    result = [
        {
            "timestamp": d.timestamp.isoformat(),
            "temperature": d.temperature,
            "pressure": d.pressure,
        }
        for d in data
    ]
    return JSONResponse(content=result)
