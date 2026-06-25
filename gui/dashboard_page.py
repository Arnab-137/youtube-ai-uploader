from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
)

from database.repository import VideoRepository


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.repo = VideoRepository()

        self.layout = QVBoxLayout(self)

        self.title = QLabel("YouTube AI Studio")
        self.title.setStyleSheet(
            "font-size:28px;font-weight:bold;"
        )

        self.layout.addWidget(self.title)

        self.grid = QGridLayout()

        self.total = QLabel()
        self.pending = QLabel()
        self.uploaded = QLabel()
        self.failed = QLabel()
        self.next_video = QLabel()

        self.grid.addWidget(self.total, 0, 0)
        self.grid.addWidget(self.pending, 0, 1)

        self.grid.addWidget(self.uploaded, 1, 0)
        self.grid.addWidget(self.failed, 1, 1)

        self.grid.addWidget(self.next_video, 2, 0)

        self.layout.addLayout(self.grid)

        self.refresh_btn = QPushButton("Refresh")

        self.refresh_btn.clicked.connect(
            self.refresh
        )

        self.layout.addWidget(self.refresh_btn)

        self.refresh()

    def refresh(self):

        total = self.repo.count_all()

        pending = self.repo.count_pending()

        uploaded = self.repo.count_uploaded()

        failed = self.repo.count_failed()

        next_video = self.repo.get_next_video()

        self.total.setText(
            f"Videos : {total}"
        )

        self.pending.setText(
            f"Pending : {pending}"
        )

        self.uploaded.setText(
            f"Uploaded : {uploaded}"
        )

        self.failed.setText(
            f"Failed : {failed}"
        )

        if next_video:

            self.next_video.setText(
                f"Next : {next_video.filename}"
            )

        else:

            self.next_video.setText(
                "Next : None"
            )
