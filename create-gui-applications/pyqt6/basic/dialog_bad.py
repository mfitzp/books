import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
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
        dlg.setWindowTitle("Error!")
        dlg.setText("There is an error")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
