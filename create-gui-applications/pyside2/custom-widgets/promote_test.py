import random
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
