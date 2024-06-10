import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, e):
        pos = e.position()
        if self.last_x is None:  # First event.
            self.last_x = pos.x()
            self.last_y = pos.y()
            return  # Ignore the first time.

        painter = QPainter(self.canvas)
        p = painter.pen()
        p.setWidth(4)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, pos.x(), pos.y())
        painter.end()
        self.label.setPixmap(self.canvas)

        # Update the origin for next time.

        self.last_x = pos.x()
        self.last_y = pos.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
