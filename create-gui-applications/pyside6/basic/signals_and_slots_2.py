from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")  # <1>
        self.button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")  # <2>
        self.button.setEnabled(False)  # <3>


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
