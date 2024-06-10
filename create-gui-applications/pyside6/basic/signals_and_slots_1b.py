import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)  # <1>


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # <2>

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, is_checked):
        print("Checked?", is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
