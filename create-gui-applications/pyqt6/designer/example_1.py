import os
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6 import uic

basedir = os.path.dirname(__file__)

app = QApplication(sys.argv)

window = uic.loadUi(os.path.join(basedir, "mainwindow.ui"))
window.show()
app.exec()
