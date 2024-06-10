import os
import sys
from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QTableView
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QAbstractTableModel

basedir = os.path.dirname(__file__)

# 11 values; middle = light gray
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
# colors = ["#67001f","#b2182b","#d6604d","#f4a582","#fddbc7","#f7f7f7","#d1e5f0","#92c5de","#4393c3","#2166ac","#053061"]


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")

            return value

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QIcon(
                    os.path.join(basedir, "calendar.png")
                )

            if isinstance(value, bool):
                if value:
                    return QIcon(
                        os.path.join(basedir, "tick.png")
                    )

                return QIcon(os.path.join(basedir, "cross.png"))

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime(2019, 5, 4), 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
