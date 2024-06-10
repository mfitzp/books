import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, is_checked):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Dialog")
        dlg.setText("Button order is platform-dependent.")
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
