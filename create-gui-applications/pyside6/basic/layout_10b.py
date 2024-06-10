import sys

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLabel,
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

        # Dictionary to store the form data, with default data.
        self.data = {
            "name": "",
            "age": 0,
            "favorite_icecream": "",
        }

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

        # Empty label to show error messages.
        self.error = QLabel()
        layout.addWidget(self.error)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def handle_name_changed(self, name):
        self.data["name"] = name
        self.validate()

    def handle_age_changed(self, age):
        self.data["age"] = age
        self.validate()

    def handle_icecream_changed(self, icecream):
        self.data["favorite_icecream"] = icecream
        self.validate()

    def validate(self):
        if self.data["age"] > 10 and self.data["favorite_icecream"] == "Chocolate":
            self.error.setText("People over 10 aren't allowed chocolate ice cream")
            return  # We can only set one message.

        if self.data["age"] > 100:
            self.error.setText("Did you send a telegram?")
            return

        self.error.setText("")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
