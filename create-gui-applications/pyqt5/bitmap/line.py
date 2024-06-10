import sys

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap
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

    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        painter.drawLine(10, 10, 300, 200)  # <3>
        painter.end()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
