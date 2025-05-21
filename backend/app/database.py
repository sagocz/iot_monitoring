import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        break
    except Exception as e:
        print(f"[database.py] DB connection failed ({i+1}/10), retrying in 3s...")
        time.sleep(3)
else:
    raise RuntimeError("Could not connect to the database after 10 attempts.")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
