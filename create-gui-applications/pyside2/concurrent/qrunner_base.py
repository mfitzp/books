import sys
import time
import traceback

from PySide2.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from PySide2.QtWidgets import QApplication, QMainWindow


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
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
