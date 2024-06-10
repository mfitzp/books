import sys

from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.table.setColumnCount(2)

        self.text = QLineEdit()

        self.button = QPushButton()
        self.button.setText("Insert item")
        self.button.setEnabled(True)
        self.button.pressed.connect(self.add_item)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.text)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def add_item(self):
        text = self.text.text()
        item = QTableWidgetItem(text)
        self.table.insertRow(0)
        self.table.setItem(0, 0, item)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
