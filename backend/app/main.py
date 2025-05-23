from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from api.routes import sensor
from core.database import db
from db_layer.base import Base

db.create_all(Base)
# Init DB schema

app = FastAPI(title="Sensor API")

app.include_router(sensor.router)

DIR = Path(__file__).parent
app.mount("/static", StaticFiles(directory=DIR / "static"), name="static")
templates = Jinja2Templates(directory=DIR / "templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
