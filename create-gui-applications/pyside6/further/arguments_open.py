from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()

        print(sys.argv)

        if len(sys.argv) > 1:  # <1>
            filename = sys.argv[1]  # <2>
            self.open_file(filename)

        self.setCentralWidget(self.editor)
        self.setWindowTitle("Text viewer")

    def open_file(self, fn):

        with open(fn, "r") as f:
            text = f.read()

        self.editor.setPlainText(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
