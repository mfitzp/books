import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)

        self.last_position = None

    def mouseMoveEvent(self, e):
        pos = e.position()
        if self.last_position is None:  # First event.
            self.last_position = pos
            return  # Ignore the first time.

        painter = QPainter(self.canvas)
        p = painter.pen()
        p.setWidth(4)
        painter.setPen(p)
        painter.drawLine(self.last_position, pos)
        painter.end()
        self.label.setPixmap(self.canvas)

        # Update the origin for next time.
        self.last_position = pos

    def mouseReleaseEvent(self, e):
        self.last_position = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
