from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

# Database URL (can override with environment variable)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgresql%40123%23@localhost/export_catalog",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency helper for FastAPI (importable from main)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
