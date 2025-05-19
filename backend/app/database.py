import os
import boto3
import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# --- PostgreSQL ---
POSTGRES_USER = os.getenv("POSTGRES_USER", "iot_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "iot_pass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "iot_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = (
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# --- DynamoDB ---
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT", "http://localhost:8001")

dynamodb_resource = boto3.resource(
    "dynamodb",
    region_name="us-west-2",
    endpoint_url=DYNAMODB_ENDPOINT,
)
