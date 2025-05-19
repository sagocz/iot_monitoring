from fastapi import FastAPI, Depends
from .database import AsyncSessionLocal, dynamodb_resource
from sqlalchemy.ext.asyncio import AsyncSession
import boto3

app = FastAPI()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@app.get("/")
async def root():
    return {"message": "IoT Monitoring Backend"}


@app.get("/pg_test")
async def test_postgres(session: AsyncSession = Depends(get_db)):
    result = await session.execute("SELECT 1;")
    return {"postgres_ok": result.scalar()}


@app.get("/dynamodb_test")
async def test_dynamodb():
    try:
        tables = list(dynamodb_resource.tables.all())
        return {"dynamodb_ok": [t.name for t in tables]}
    except Exception as e:
        return {"error": str(e)}
