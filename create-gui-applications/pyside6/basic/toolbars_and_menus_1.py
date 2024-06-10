import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        # Optional: to prevent this toolbar being removed.
        # toolbar.toggleViewAction().setEnabled(False)
        self.addToolBar(toolbar)

    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
