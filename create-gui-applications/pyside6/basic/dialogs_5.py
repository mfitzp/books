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

    # tag::button_clicked[]
    def button_clicked(self, is_checked):

        button = QMessageBox.question(
            self, "Question dialog", "The longer message"
        )

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")

    # end::button_clicked[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
