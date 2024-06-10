import os
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader

loader = QUiLoader()
basedir = os.path.dirname(__file__)


def mainwindow_setup(w):
    w.setWindowTitle("MainWindow Title")


app = QApplication(sys.argv)
window = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
mainwindow_setup(window)
window.show()
app.exec_()
