import sys

from random import choice, randint  # <1>

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    # tag::draw_something[]
    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            painter.drawPoint(
                200 + randint(-100, 100),
                150 + randint(-100, 100),  # x  # y
            )
        painter.end()

    # end::draw_something[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
