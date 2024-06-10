import os
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(basedir, "Chinook_Sqlite.sqlite"))
        self.db.open()

        self.model = QSqlTableModel(db=self.db)

        self.table.setModel(self.model)

        # tag::titles[]
        self.model.setTable("Track")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, "Album (ID)")
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, "Media Type (ID)")
        self.model.setHeaderData(4, Qt.Orientation.Horizontal, "Genre (ID)")
        self.model.setHeaderData(5, Qt.Orientation.Horizontal, "Composer")
        self.model.select()
        # end::titles[]

        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
