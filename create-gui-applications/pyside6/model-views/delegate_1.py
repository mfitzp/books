import glob
import math
import sys
from collections import namedtuple

from PySide6.QtCore import QAbstractTableModel, QSize, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStyledItemDelegate,
    QTableView,
)

# Create a custom namedtuple class to hold our data.
preview = namedtuple("preview", "id title image")

NUMBER_OF_COLUMNS = 4
CELL_PADDING = 20  # all sides


class PreviewDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # data is our preview object
        data = index.model().data(index, Qt.DisplayRole)
        if data is None:
            return

        width = option.rect.width() - CELL_PADDING * 2
        height = option.rect.height() - CELL_PADDING * 2

        # option.rect holds the area we are painting on the widget (our table cell)
        # scale our pixmap to fit
        scaled = data.image.scaled(
            width,
            height,
            aspectRatioMode=Qt.KeepAspectRatio,
        )
        # Position in the middle of the area.
        x = CELL_PADDING + (width - scaled.width()) / 2
        y = CELL_PADDING + (height - scaled.height()) / 2

        painter.drawImage(
            option.rect.x() + x, option.rect.y() + y, scaled
        )

    def sizeHint(self, option, index):
        # All items the same size.
        return QSize(300, 200)


class PreviewModel(QAbstractTableModel):
    def __init__(self, todos=None):
        super().__init__()
        # .data holds our data for display, as a list of Preview objects.
        self.previews = []

    def data(self, index, role):
        try:
            data = self.previews[index.row() * 4 + index.column()]
        except IndexError:
            # Incomplete last row.
            return

        if role == Qt.DisplayRole:
            return data  # Pass the data to our delegate to draw.

        if role == Qt.ToolTipRole:
            return data.title

    def columnCount(self, index):
        return NUMBER_OF_COLUMNS

    def rowCount(self, index):
        n_items = len(self.previews)
        return math.ceil(n_items / NUMBER_OF_COLUMNS)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QTableView()
        self.view.horizontalHeader().hide()
        self.view.verticalHeader().hide()
        self.view.setGridStyle(Qt.NoPen)

        delegate = PreviewDelegate()
        self.view.setItemDelegate(delegate)
        self.model = PreviewModel()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)

        # Add a bunch of images.
        image_files = glob.glob("*.jpg")
        for n, fn in enumerate(image_files):
            image = QImage(fn)
            item = preview(n, fn, image)
            self.model.previews.append(item)
        self.model.layoutChanged.emit()

        self.view.resizeRowsToContents()
        self.view.resizeColumnsToContents()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
