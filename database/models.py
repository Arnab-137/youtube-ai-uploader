from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    filename = Column(String(255), unique=True, nullable=False, index=True)

    title = Column(Text)
    description = Column(Text)
    tags = Column(Text)

    playlist = Column(String(255))
    privacy = Column(String(50), default="Private")
    language = Column(String(50), default="English")
    category = Column(String(100), default="Sports")

    made_for_kids = Column(Boolean, default=False)

    status = Column(String(30), default="Pending")

    youtube_id = Column(String(50))

    created_at = Column(DateTime, default=datetime.utcnow)
    uploaded_at = Column(DateTime, nullable=True)

