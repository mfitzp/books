import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap
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
        painter.drawPoint(200, 150)
        painter.end()

    # end::draw_something[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
