import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    message = pyqtSignal(str)  # <1>
    value = pyqtSignal(int, str, int)  # <2>
    another = pyqtSignal(list)  # <3>
    onemore = pyqtSignal(dict)  # <4>
    anything = pyqtSignal(object)  # <5>

    def __init__(self):
        super().__init__()

        self.message.connect(self.custom_slot)
        self.value.connect(self.custom_slot)
        self.another.connect(self.custom_slot)
        self.onemore.connect(self.custom_slot)
        self.anything.connect(self.custom_slot)

        self.message.emit("my message")
        self.value.emit(23, "abc", 1)
        self.another.emit([1, 2, 3, 4, 5])
        self.onemore.emit({"a": 2, "b": 7})
        self.anything.emit(1223)

    def custom_slot(self, *args):
        print(args)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
