import sys
import random

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QMainWindow,
    QSpinBox,
    QWidget,
    QPushButton,
)

# Model is a simple dictionary to start.
model = {
    "name": "Johnina Smith",
    "age": 10,
    "favorite_icecream": "Vanilla",
}

# We store the backups as a simple list.
backups = []


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QFormLayout()

        # Dictionary to store the form data, with default data.
        self.name = QLineEdit()
        self.name.textChanged.connect(self.handle_name_changed)
        self.age = QSpinBox()
        self.age.setRange(0, 200)
        self.age.valueChanged.connect(self.handle_age_changed)
        self.icecream = QComboBox()
        self.icecream.addItems(["Vanilla", "Strawberry", "Chocolate"])
        self.icecream.currentTextChanged.connect(self.handle_icecream_changed)

        self.save_btn = QPushButton("Save")
        self.save_btn.pressed.connect(self.handle_save_btn)
        self.restore_btn = QPushButton("Restore")
        self.restore_btn.pressed.connect(self.handle_restore_btn)

        layout.addRow("Name", self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favorite Ice cream", self.icecream)
        layout.addRow(self.save_btn)
        layout.addRow(self.restore_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.update_ui() # <1>

    def update_ui(self): # <2>
        """ Synchronise the UI with the current model state. """
        self.name.setText(model["name"])
        self.age.setValue(model["age"])
        self.icecream.setCurrentText(model["favorite_icecream"])

    def handle_name_changed(self, name):
        model["name"] = name
        self.update_ui() # <3>

    def handle_age_changed(self, age):
        model["age"] = age
        self.update_ui()

    def handle_icecream_changed(self, icecream):
        model["favorite_icecream"] = icecream
        self.update_ui()

    def handle_save_btn(self):
        # Save a copy of the current model (if we don't copy,
        # changes will modify the backup!)
        backups.append(model.copy())
        print("SAVE:", model)
        print("BACKUPS:", len(backups))

    def handle_restore_btn(self):
        # Randomly get a backup.
        if not backups:
            return # Ignore if empty.
        random.shuffle(backups)
        backup = backups.pop() # Remove a backup.
        model.update(backup) # Overwrite the data in the model.
        self.update_ui()
        print("RESTORE:", model)
        print("BACKUPS:", len(backups))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
