import time

from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from contextlib import contextmanager
from core.config import settings

class Database:
    def __init__(self, url: str):
        self._engine = create_engine(url, pool_pre_ping=True)
        self._SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine
        )

    @property
    def engine(self):
        return self._engine

    def create_all(self, base_model, retries: int = 10, delay: float = 2.0):
        for attempt in range(1, retries + 1):
            try:
                base_model.metadata.create_all(bind=self.engine)
                print("Database connected and tables created.")
                break
            except OperationalError as e:
                print(f"Attempt {attempt}/{retries} – Database not ready yet: {e}")
                if attempt == retries:
                    print("Could not connect to the database after retries.")
                    raise
                time.sleep(delay)

    @contextmanager
    def get_session(self) -> Session:
        db = self._SessionLocal()
        try:
            yield db
        finally:
            db.close()

db = Database(settings.database_url)

def get_db():
    with db.get_session() as session:
        yield session
