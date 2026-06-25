from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("📊 Dashboard")
        title.setStyleSheet("font-size:28px;font-weight:bold;")

        layout.addWidget(title)

        layout.addWidget(QLabel("Videos Found : 0"))
        layout.addWidget(QLabel("Uploaded : 0"))
        layout.addWidget(QLabel("Failed : 0"))
        layout.addWidget(QLabel("Next Upload : --"))
