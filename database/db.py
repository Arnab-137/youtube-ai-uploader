from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base

DATABASE_URL = "sqlite:///youtube_uploader.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()
