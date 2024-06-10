from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
)

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for arg in sys.argv:  # <1>
            label = QLabel(arg)
            layout.addWidget(label)

        self.setLayout(layout)
        self.setWindowTitle("Arguments")


app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()
