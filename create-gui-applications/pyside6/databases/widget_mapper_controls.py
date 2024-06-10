import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDataWidgetMapper,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        form = QFormLayout()

        self.track_id = QSpinBox()
        self.track_id.setRange(0, 2147483647)
        self.track_id.setDisabled(True)
        self.name = QLineEdit()
        self.album = QComboBox()
        self.media_type = QComboBox()
        self.genre = QComboBox()
        self.composer = QLineEdit()

        self.milliseconds = QSpinBox()
        self.milliseconds.setRange(0, 2147483647)
        self.milliseconds.setSingleStep(1)

        self.bytes = QSpinBox()
        self.bytes.setRange(0, 2147483647)
        self.bytes.setSingleStep(1)

        self.unit_price = QDoubleSpinBox()
        self.unit_price.setRange(0, 999)
        self.unit_price.setSingleStep(0.01)
        self.unit_price.setPrefix("$")

        form.addRow(QLabel("Track ID"), self.track_id)
        form.addRow(QLabel("Track name"), self.name)
        form.addRow(QLabel("Composer"), self.composer)
        form.addRow(QLabel("Milliseconds"), self.milliseconds)
        form.addRow(QLabel("Bytes"), self.bytes)
        form.addRow(QLabel("Unit Price"), self.unit_price)

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join("Chinook_Sqlite.sqlite"))
        self.db.open()

        self.model = QSqlTableModel(db=self.db)

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)

        self.mapper.addMapping(self.track_id, 0)
        self.mapper.addMapping(self.name, 1)
        self.mapper.addMapping(self.composer, 5)
        self.mapper.addMapping(self.milliseconds, 6)
        self.mapper.addMapping(self.bytes, 7)
        self.mapper.addMapping(self.unit_price, 8)

        self.model.setTable("Track")
        self.model.select()

        self.mapper.toFirst()

        # tag::controls[]
        self.setMinimumSize(QSize(400, 400))

        controls = QHBoxLayout()

        prev_rec = QPushButton("Previous")
        prev_rec.clicked.connect(self.mapper.toPrevious)

        next_rec = QPushButton("Next")
        next_rec.clicked.connect(self.mapper.toNext)

        save_rec = QPushButton("Save Changes")
        save_rec.clicked.connect(self.mapper.submit)

        controls.addWidget(prev_rec)
        controls.addWidget(next_rec)
        controls.addWidget(save_rec)

        layout.addLayout(form)
        layout.addLayout(controls)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # end::controls[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
