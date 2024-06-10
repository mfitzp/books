import sys

from PySide6.QtCore import (
    QObject,
    QRunnable,
    Slot,
)
from PySide6.QtWidgets import QApplication, QMainWindow


class WorkerSignals(QObject):
    pass


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Store constructor arguments (re-used for processing)
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
