import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)  # <1>
        canvas.fill(Qt.white)  # <2>

        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
