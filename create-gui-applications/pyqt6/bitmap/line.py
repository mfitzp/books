import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)  # <1>
        self.canvas.fill(Qt.GlobalColor.white)  # <2>
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.canvas)
        painter.drawLine(10, 10, 300, 200)  # <3>
        painter.end()
        self.label.setPixmap(self.canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
