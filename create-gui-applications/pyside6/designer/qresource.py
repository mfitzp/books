import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon

import resources  # Import the compiled resource file.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        b = QPushButton("My button")

        icon = QIcon(":/icons/penguin.png")
        b.setIcon(icon)
        self.setCentralWidget(b)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
