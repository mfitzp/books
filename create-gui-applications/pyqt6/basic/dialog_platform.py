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
        dlg.setWindowTitle("Dialog")
        dlg.setText("Button order is platform-dependent.")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Ok
            | QMessageBox.StandardButton.Cancel
        )
        dlg.setIcon(QMessageBox.Icon.Information)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
