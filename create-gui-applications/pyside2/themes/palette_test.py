from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import Qt

import sys


app = QApplication(sys.argv)
palette = QPalette()
palette.setColor(QPalette.Window, QColor(0, 128, 255))
palette.setColor(QPalette.WindowText, Qt.white)
app.setPalette(palette)

window = QLabel("Palette Test")
window.show()

app.exec_()
