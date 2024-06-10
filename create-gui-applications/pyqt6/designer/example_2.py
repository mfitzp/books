import os
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join(basedir, "mainwindow.ui"), self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
