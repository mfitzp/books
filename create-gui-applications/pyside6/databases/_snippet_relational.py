from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel

model = QSqlRelationalTableModel(db=db)

relation = QSqlRelation('<related_table>', '<related_table_foreign_key_column', '<column_to_display>')
model.setRelation(<column>, relation)
