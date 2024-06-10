import os

from PyQt5.QtSql import QSqlDatabase

basedir = os.path.dirname(__file__)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName(os.path.join(basedir, "Chinook_Sqlite.sqlite"))
db.open()
