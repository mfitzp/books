import sys
from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QTableView
from PySide6.QtGui import QIcon, QColor, QBrush
from PySide6.QtCore import Qt, QAbstractTableModel

# Color range -5 to +5; 0 = light gray
COLORS = [
    "#053061",
    "#2166ac",
    "#4393c3",
    "#92c5de",
    "#d1e5f0",
    "#f7f7f7",
    "#fddbc7",
    "#f4a582",
    "#d6604d",
    "#b2182b",
    "#67001f",
]


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # tag::data[]
    def data(self, index, role):
        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)  # Convert to integer for indexing.

                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)  # valaues > +5 become +5
                value = value + 5  # -5 becomes 0, +5 becomes + 10

                return QColor(COLORS[value])

        # existing `if role == Qt.DisplayRole:` block hidden
        # hidden for clarity.
        # end::data[]

        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [
            [4, 9, 2],
            [1, -1, -1],
            [3, 5, -5],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
