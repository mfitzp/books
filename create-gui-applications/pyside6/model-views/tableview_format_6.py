import os

import sys
from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QTableView
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QAbstractTableModel



basedir = os.path.dirname(__file__)


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
