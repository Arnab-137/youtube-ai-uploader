from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    filename = Column(String, unique=True, nullable=False)

    title = Column(Text)

    description = Column(Text)

    tags = Column(Text)

    playlist = Column(String)

    privacy = Column(String, default="private")

    language = Column(String, default="English")

    category = Column(String, default="Sports")

    made_for_kids = Column(Boolean, default=False)

    status = Column(String, default="Pending")

    upload_time = Column(DateTime)

    youtube_id = Column(String)
