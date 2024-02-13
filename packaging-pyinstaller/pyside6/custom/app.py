from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtGui import QIcon

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.svg"))
w = MainWindow()
app.exec()
