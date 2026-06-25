from pathlib import Path
from database.db import get_session
from database.models import Video
from utils.excel_reader import load_metadata


class QueueService:
    def __init__(self):
        self.session = get_session()

    def import_excel(self, excel_file="metadata.xlsx", videos_folder="videos"):
        rows = load_metadata(excel_file)

        # Get all actual video files
        video_files = sorted(
            [
                f for f in Path(videos_folder).iterdir()
                if f.is_file() and f.suffix.lower() in (
                    ".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"
                )
            ]
        )

        print(f"Found {len(video_files)} videos in folder.")

        imported = 0
        skipped = 0
        missing = 0

        # Match by order instead of filename
        for row, video_file in zip(rows, video_files):

            exists = (
                self.session.query(Video)
                .filter(Video.filename == video_file.name)
                .first()
            )

            if exists:
                skipped += 1
                continue

            video = Video(
                filename=video_file.name,
                title=row.get("title"),
                description=row.get("description"),
                tags=row.get("tags"),
                playlist=row.get("playlist"),
                privacy=row.get("privacy"),
                language=row.get("language"),
                category=row.get("category"),
                made_for_kids=str(row.get("made_for_kids")).lower() == "yes",
            )

            self.session.add(video)
            imported += 1

        self.session.commit()

        if len(rows) > len(video_files):
            missing = len(rows) - len(video_files)

        return {
            "imported": imported,
            "skipped": skipped,
            "missing": missing,
        }
