from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon

import sys

app = QApplication(sys.argv)
button = QPushButton("Hello")
icon = QIcon.fromTheme("document-new")
button.setIcon(icon)
button.show()

app.exec_()
