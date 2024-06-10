import os
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

basedir = os.path.dirname(__file__)

loader = QUiLoader()

app = QApplication(sys.argv)
window = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
window.show()
app.exec()
