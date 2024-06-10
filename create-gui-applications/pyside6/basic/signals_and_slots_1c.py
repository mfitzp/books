import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True  # <1>

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)  # <2>

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_toggled(self, is_checked):
        self.button_is_checked = is_checked  # <3>

        print(self.button_is_checked)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
