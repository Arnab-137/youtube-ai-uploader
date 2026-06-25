from sqlalchemy import func

from database.db import get_session
from database.models import Video


class VideoRepository:
    def __init__(self):
        self.session = get_session()

    def count_all(self):
        return self.session.query(Video).count()

    def count_pending(self):
        return (
            self.session.query(Video)
            .filter(Video.status == "Pending")
            .count()
        )

    def count_uploaded(self):
        return (
            self.session.query(Video)
            .filter(Video.status == "Uploaded")
            .count()
        )

    def count_failed(self):
        return (
            self.session.query(Video)
            .filter(Video.status == "Failed")
            .count()
        )

    def get_next_video(self):
        return (
            self.session.query(Video)
            .filter(Video.status == "Pending")
            .order_by(Video.id)
            .first()
        )
