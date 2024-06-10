import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")  # <1>
        self.button.setCheckable(True)
        self.button.released.connect(
            self.the_button_was_released
        )  # <2>
        self.button.setChecked(self.button_is_checked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()  # <3>

        print(self.button_is_checked)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
