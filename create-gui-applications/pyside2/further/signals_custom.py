import sys

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    message = Signal(str)  # <1>
    value = Signal(int, str, int)  # <2>
    another = Signal(list)  # <3>
    onemore = Signal(dict)  # <4>
    anything = Signal(object)  # <5>

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

app.exec_()
