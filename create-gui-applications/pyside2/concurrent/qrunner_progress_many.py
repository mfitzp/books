import random
import sys
import time
import uuid

from PySide2.QtCore import QObject, QRunnable, QThreadPool, QTimer, Signal, Slot
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    progress
        int progress complete,from 0-100
    """

    progress = Signal(str, int)
    finished = Signal(str)


class Worker(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.
    """

    def __init__(self):
        super().__init__()
        self.job_id = uuid.uuid4().hex  # <1>
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        total_n = 1000
        delay = random.random() / 100  # Random delay value.
        for n in range(total_n):
            progress_pc = int(100 * float(n + 1) / total_n)  # <2>
            self.signals.progress.emit(self.job_id, progress_pc)
            time.sleep(delay)

        self.signals.finished.emit(self.job_id)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.progress = QProgressBar()

        button = QPushButton("START IT UP")
        button.pressed.connect(self.execute)

        self.status = QLabel("0 workers")

        layout.addWidget(self.progress)
        layout.addWidget(button)
        layout.addWidget(self.status)

        w = QWidget()
        w.setLayout(layout)

        # Dictionary holds the progress of current workers.
        self.worker_progress = {}

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
        )

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.refresh_progress)
        self.timer.start()

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        worker.signals.finished.connect(self.cleanup)  # <3>

        # Execute
        self.threadpool.start(worker)

    def cleanup(self, job_id):
        if job_id in self.worker_progress:
            del self.worker_progress[job_id]  # <4>

            # Update the progress bar if we've removed a value.
            self.refresh_progress()

    def update_progress(self, job_id, progress):
        self.worker_progress[job_id] = progress

    def calculate_progress(self):
        if not self.worker_progress:
            return 0

        return sum(v for v in self.worker_progress.values()) / len(self.worker_progress)

    def refresh_progress(self):
        # Calculate total progress.
        progress = self.calculate_progress()
        print(self.worker_progress)
        self.progress.setValue(progress)
        self.status.setText("%d workers" % len(self.worker_progress))


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
