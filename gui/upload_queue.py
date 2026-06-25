from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)

from utils.video_scanner import scan_folder


class UploadQueuePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.info = QLabel("No folder selected")

        self.button = QPushButton("📂 Select Video Folder")

        self.table = QTableWidget()

        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels(
            ["Filename", "Status"]
        )

        layout.addWidget(self.info)
        layout.addWidget(self.button)
        layout.addWidget(self.table)

        self.button.clicked.connect(self.choose_folder)

    def choose_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Choose Folder"
        )

        if not folder:
            return

        videos = scan_folder(folder)

        self.info.setText(
            f"Found {len(videos)} videos"
        )

        self.table.setRowCount(len(videos))

        for row, video in enumerate(videos):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(video.name)
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem("Waiting")
            )
