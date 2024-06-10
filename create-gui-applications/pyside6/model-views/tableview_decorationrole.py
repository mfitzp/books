import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QTableView
from PySide6.QtGui import QColor, QBrush
from PySide6.QtCore import Qt, QAbstractTableModel

# Color range -5 to +5; 0 = light gray
colors = [
    "#67001f",
    "#b2182b",
    "#d6604d",
    "#f4a582",
    "#fddbc7",
    "#f7f7f7",
    "#d1e5f0",
    "#92c5de",
    "#4393c3",
    "#2166ac",
    "#053061",
]


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            return self._data[index.row()][index.column()]

        elif role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            # Limit to range, + 5 to 0..11 list indexes Python
            color_ix = ((min(max(-5, value), 5) + 5) * -1) + 10
            return QBrush(QColor(colors[color_ix]))

        # elif role == Qt.DecorationRole:
        #   if self._data[index.row()][index.column()] < 0:
        #       return QtGui.QColor('red')

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
