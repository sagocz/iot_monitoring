from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, SensorData, SensorDataIn

DIR = Path(__file__).parent
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


@app.get("/plot-data")
def get_plot_data(db: Session = Depends(get_db)):
    data = db.query(SensorData).order_by(SensorData.timestamp.desc()).limit(12).all()
    data.reverse()
    result = [
        {
            "timestamp": d.timestamp.isoformat(),
            "temperature": d.temperature,
            "pressure": d.pressure,
        }
        for d in data
    ]
    return JSONResponse(content=result)


app.mount("/static", StaticFiles(directory=DIR / "static"), name="static")
templates = Jinja2Templates(directory=DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
