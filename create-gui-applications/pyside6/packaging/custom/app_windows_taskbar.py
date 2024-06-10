from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtGui import QIcon

import sys, os

basedir = os.path.dirname(__file__)

try:  # <1>
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"  # <2>
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


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
