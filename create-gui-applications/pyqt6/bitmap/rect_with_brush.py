import sys

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen, QPixmap
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

    # tag::draw_something[]
    def draw_something(self):
        painter = QPainter(self.canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("#376F9F"))
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor("#FFD141"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)

        painter.drawRects(
            QRect(50, 50, 100, 100),
            QRect(60, 60, 150, 100),
            QRect(70, 70, 100, 150),
            QRect(80, 80, 150, 100),
            QRect(90, 90, 100, 150),
        )
        painter.end()
        self.label.setPixmap(self.canvas)

    # end::draw_something[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
