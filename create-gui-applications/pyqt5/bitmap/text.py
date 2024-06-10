import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)  # <1>
        canvas.fill(Qt.white)  # <2>
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    # tag::draw_something[]
    def draw_something(self):
        painter = QPainter(self.label.pixmap())

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor("green"))
        painter.setPen(pen)

        font = QFont()
        font.setFamily("Times")
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, "Hello, world!")
        painter.end()

    # end::draw_something[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
