import sys

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap
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
        pen.setWidth(15)
        pen.setColor(QColor("blue"))
        painter.setPen(pen)
        painter.drawLine(QPoint(100, 100), QPoint(300, 200))
        painter.end()

    # end::draw_something[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
