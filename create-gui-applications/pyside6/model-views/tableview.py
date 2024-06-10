import sys


from PySide6.QtWidgets import QMainWindow, QApplication, QTableView
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QAbstractTableModel

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            return self._data[index.row()][index.column()]

        if role == Qt.BackgroundRole and index.column() == 1:
            # See below for the data structure.
            return QColor("blue")

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
