import sys

import PySide6  # Required to enable the features.
from __feature__ import snake_case, true_property
from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.table.column_count = 2

        self.text = QLineEdit()

        self.button = QPushButton()
        self.button.text = "Insert item"
        self.button.enabled = True
        self.button.pressed.connect(self.add_item)

        layout = QVBoxLayout()
        layout.add_widget(self.table)
        layout.add_widget(self.text)
        layout.add_widget(self.button)

        self.set_layout(layout)

    def add_item(self):
        text = self.text.text
        item = QTableWidgetItem(text)
        self.table.insert_row(0)
        self.table.set_item(0, 0, item)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
