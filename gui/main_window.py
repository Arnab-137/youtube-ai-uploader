from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QStackedWidget,
)

from gui.dashboard import DashboardPage
from gui.settings import SettingsPage
from gui.history import HistoryPage
from gui.upload_queue import UploadQueuePage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube AI Uploader")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(220)

        pages = [
            "🏠 Dashboard",
            "📂 Upload Queue",
            "📜 History",
            "⚙ Settings",
        ]

        for p in pages:
            self.sidebar.addItem(QListWidgetItem(p))

        layout.addWidget(self.sidebar)

        self.stack = QStackedWidget()

        self.stack.addWidget(DashboardPage())
        self.stack.addWidget(UploadQueuePage())
        self.stack.addWidget(HistoryPage())
        self.stack.addWidget(SettingsPage())

        layout.addWidget(self.stack)

        self.sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)

        self.sidebar.setCurrentRow(0)
