from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()

        if __file__ in sys.argv:  # <1>
            sys.argv.remove(__file__)

        if sys.argv:  # <2>
            filename = sys.argv[0]  # <3>
            self.open_file(filename)

        self.setCentralWidget(self.editor)
        self.setWindowTitle("Text viewer")

    def open_file(self, fn):

        with open(fn, "r") as f:
            text = f.read()

        self.editor.setPlainText(text)


app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()
