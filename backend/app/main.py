from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api_routes import sensor
from app_models.db_models import Base
from db_layer.database import engine

DIR = Path(__file__).parent

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sensor.router)

app.mount("/static", StaticFiles(directory=DIR / "static"), name="static")
templates = Jinja2Templates(directory=DIR / "templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
