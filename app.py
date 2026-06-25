import sys

from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("YouTube AI Uploader")
label.resize(500, 200)
label.show()

sys.exit(app.exec())

