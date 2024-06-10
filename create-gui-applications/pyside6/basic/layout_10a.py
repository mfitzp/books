import sys

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QMainWindow,
    QSpinBox,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QFormLayout()

        # Dictionary to store the form data.
        self.data = {}

        self.name = QLineEdit()
        self.name.textChanged.connect(self.handle_name_changed)
        self.age = QSpinBox()
        self.age.setRange(0, 200)
        self.age.valueChanged.connect(self.handle_age_changed)
        self.icecream = QComboBox()
        self.icecream.addItems(["Vanilla", "Strawberry", "Chocolate"])
        self.icecream.currentTextChanged.connect(self.handle_icecream_changed)

        layout.addRow("Name", self.name)
        # or layout.addRow(QLabel("Name"), self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favorite Ice cream", self.icecream)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def handle_name_changed(self, name):
        self.data["name"] = name
        print(self.data)

    def handle_age_changed(self, age):
        self.data["age"] = age
        print(self.data)

    def handle_icecream_changed(self, icecream):
        self.data["favorite_icecream"] = icecream
        print(self.data)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
