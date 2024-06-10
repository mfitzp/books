import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("My simple app.")
        button.setIcon(QIcon(os.path.join(basedir, "icon.svg")))
        button.pressed.connect(self.close)

        self.setCentralWidget(button)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "icon.svg")))
window = MainWindow()
window.show()
app.exec()
