import sys

from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def item_changed(self, i):  # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
