import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.status = self.statusBar()
        self.setFixedSize(QSize(200, 100))
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    # tag::mousePressEvent[]
    def mousePressEvent(self, e):
        route = {  # <1>
            Qt.LeftButton: self.left_mousePressEvent,
            Qt.MiddleButton: self.middle_mousePressEvent,
            Qt.RightButton: self.right_mousePressEvent,
        }
        button = e.button()
        fn = route[button]  # <2>
        return fn(e)  # <3>

    def left_mousePressEvent(self, e):
        self.label.setText("mousePressEvent LEFT")
        if e.x() < 100:
            self.status.showMessage("Left click on left")
            self.move(self.x() - 10, self.y())
        else:
            self.status.showMessage("Left click on right")
            self.move(self.x() + 10, self.y())

    def middle_mousePressEvent(self, e):
        self.label.setText("mousePressEvent MIDDLE")

    def right_mousePressEvent(self, e):
        if e.x() < 100:
            self.status.showMessage("Right click on left")
            print("Something else here.")
            self.move(10, 10)
        else:
            self.status.showMessage("Right click on right")
            self.move(400, 400)

    # end::mousePressEvent[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
