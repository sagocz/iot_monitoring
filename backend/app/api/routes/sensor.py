from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from db_layer.schemas.sensor_data import SensorDataIn
from db_layer.repositories.sensor_data_repository import SensorDataRepository
from db_layer.dependencies import get_sensor_data_repository

router = APIRouter()


@router.post("/data")
async def receive_data(
    data: SensorDataIn,
    repo: SensorDataRepository = Depends(get_sensor_data_repository),
):
    try:
        new_data = repo.create(data)
        return {"status": "success", "id": new_data.id}
    except Exception as e:
        return {"error": str(e)}


@router.get("/plot-data")
def get_plot_data(
    repo: SensorDataRepository = Depends(get_sensor_data_repository),
):
    data = repo.get_last()
    result = [
        {
            "timestamp": d.timestamp.isoformat(),
            "temperature": d.temperature,
            "pressure": d.pressure,
        }
        for d in data
    ]
    return JSONResponse(content=result)
