import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
)

class MainWindow(QMainWindow):
    # end::MainWindow[]
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    # tag::button_clicked[]

    # __init__ skipped for clarity
    def button_clicked(self, is_checked):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        # Look up the button enum entry for the result.
        button = QMessageBox.StandardButton(button)

        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")

    # end::button_clicked[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
