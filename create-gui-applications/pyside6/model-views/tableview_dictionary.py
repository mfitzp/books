import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QTableView
from PySide6.QtCore import Qt, QAbstractTableModel


class DictionaryTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Look up the key by header index.
            column = index.column()
            column_key = self._headers[column]
            return self._data[index.row()][column_key]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                return str(section)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [
            {"a": 4, "b": 9, "c": 2},
            {"a": 1, "b": 0, "c": 0},
            {"a": 3, "b": 5, "c": 0},
            {"a": 3, "b": 3, "c": 2},
            {"a": 7, "b": 8, "c": 9},
        ]

        headers = ["a", "b", "c"]

        self.model = DictionaryTableModel(data, headers)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
