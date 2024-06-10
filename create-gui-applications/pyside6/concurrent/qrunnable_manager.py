import random
import sys
import time
import uuid

from PySide6.QtCore import (
    QAbstractListModel,
    QObject,
    QRect,
    QRunnable,
    Qt,
    QThreadPool,
    QTimer,
    Signal,
    Slot,
)
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtWidgets import (
    QApplication,
    QListView,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QStyledItemDelegate,
    QVBoxLayout,
    QWidget,
)

STATUS_WAITING = "waiting"
STATUS_RUNNING = "running"
STATUS_ERROR = "error"
STATUS_COMPLETE = "complete"


STATUS_COLORS = {
    STATUS_RUNNING: "#33a02c",
    STATUS_ERROR: "#e31a1c",
    STATUS_COMPLETE: "#b2df8a",
}

DEFAULT_STATE = {"progress": 0, "status": STATUS_WAITING}

class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress

    """

    error = Signal(str, str)
    result = Signal(str, object)  # We can send anything back.

    finished = Signal(str)
    progress = Signal(str, int)
    status = Signal(str, str)


class Worker(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals and wrap-up.

    :param args: Arguments to pass for the worker
    :param kwargs: Keywords to pass for the worker

    """

    def __init__(self, *args, **kwargs):
        super().__init__()

        # Store constructor arguments (re-used for processing).
        self.signals = WorkerSignals()

        # Give this job a unique ID.
        self.job_id = str(uuid.uuid4())

        # The arguments for the worker
        self.args = args
        self.kwargs = kwargs

        self.signals.status.emit(self.job_id, STATUS_WAITING)

    @Slot()
    def run(self):
        """
        Initialize the runner function with passed args, kwargs.
        """

        self.signals.status.emit(self.job_id, STATUS_RUNNING)

        x, y = self.args

        try:

            value = random.randint(0, 100) * x
            delay = random.random() / 10
            result = []

            for n in range(100):
                # Generate some numbers.
                value = value / y
                y -= 1

                # The following will sometimes throw a division by zero error.
                result.append(value)

                # Pass out the current progress.
                self.signals.progress.emit(self.job_id, n + 1)
                time.sleep(delay)

        except Exception as e:
            print(e)
            # We swallow the error and continue.
            self.signals.error.emit(self.job_id, str(e))
            self.signals.status.emit(self.job_id, STATUS_ERROR)

        else:
            self.signals.result.emit(self.job_id, result)
            self.signals.status.emit(self.job_id, STATUS_COMPLETE)

        self.signals.finished.emit(self.job_id)




class WorkerManager(QAbstractListModel):
    """
    Manager to handle our worker queues and state.
    Also functions as a Qt data model for a view
    displaying progress for each worker.

    """

    _workers = {}
    _state = {}

    status = Signal(str)

    def __init__(self):
        super().__init__()

        # Create a threadpool for our workers.
        self.threadpool = QThreadPool()
        # self.threadpool.setMaxThreadCount(1)
        self.max_threads = self.threadpool.maxThreadCount()
        print(
            "Multithreading with maximum %d threads" % self.max_threads
        )

        self.status_timer = QTimer()
        self.status_timer.setInterval(100)
        self.status_timer.timeout.connect(self.notify_status)
        self.status_timer.start()

    def notify_status(self):
        n_workers = len(self._workers)
        running = min(n_workers, self.max_threads)
        waiting = max(0, n_workers - self.max_threads)
        self.status.emit(
            "{} running, {} waiting, {} threads".format(
                running, waiting, self.max_threads
            )
        )

    def enqueue(self, worker):
        """
        Enqueue a worker to run (at some point) by passing it to the QThreadPool.
        """
        worker.signals.error.connect(self.receive_error)
        worker.signals.status.connect(self.receive_status)
        worker.signals.progress.connect(self.receive_progress)
        worker.signals.finished.connect(self.done)

        self.threadpool.start(worker)
        self._workers[worker.job_id] = worker

        # Set default status to waiting, 0 progress.
        self._state[worker.job_id] = DEFAULT_STATE.copy()

        self.layoutChanged.emit()

    def receive_status(self, job_id, status):
        self._state[job_id]["status"] = status
        self.layoutChanged.emit()

    def receive_progress(self, job_id, progress):
        self._state[job_id]["progress"] = progress
        self.layoutChanged.emit()

    def receive_error(self, job_id, message):
        print(job_id, message)

    def done(self, job_id):
        """
        Task/worker complete. Remove it from the active workers
        dictionary. We leave it in worker_state, as this is used to
        to display past/complete workers too.
        """
        del self._workers[job_id]
        self.layoutChanged.emit()

    def cleanup(self):
        """
        Remove any complete/failed workers from worker_state.
        """
        for job_id, s in list(self._state.items()):
            if s["status"] in (STATUS_COMPLETE, STATUS_ERROR):
                del self._state[job_id]
        self.layoutChanged.emit()

    # Model interface
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            job_ids = list(self._state.keys())
            job_id = job_ids[index.row()]
            return job_id, self._state[job_id]

    def rowCount(self, index):
        return len(self._state)




class ProgressBarDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # data is our status dict, containing progress, id, status
        job_id, data = index.model().data(index, Qt.DisplayRole)
        if data["progress"] > 0:
            color = QColor(STATUS_COLORS[data["status"]])

            brush = QBrush()
            brush.setColor(color)
            brush.setStyle(Qt.SolidPattern)

            width = option.rect.width() * data["progress"] / 100

            rect = QRect(
                option.rect
            )  # Copy of the rect, so we can modify.
            rect.setWidth(width)

            painter.fillRect(rect, brush)

        pen = QPen()
        pen.setColor(Qt.black)
        painter.drawText(option.rect, Qt.AlignLeft, job_id)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.workers = WorkerManager()

        self.workers.status.connect(self.statusBar().showMessage)

        layout = QVBoxLayout()

        self.progress = QListView()
        self.progress.setModel(self.workers)
        delegate = ProgressBarDelegate()
        self.progress.setItemDelegate(delegate)

        layout.addWidget(self.progress)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        start = QPushButton("Start a worker")
        start.pressed.connect(self.start_worker)

        clear = QPushButton("Clear")
        clear.pressed.connect(self.workers.cleanup)

        layout.addWidget(self.text)
        layout.addWidget(start)
        layout.addWidget(clear)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)


    # tag::startWorker[]
    def start_worker(self):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)

        w = Worker(x, y)
        w.signals.result.connect(self.display_result)
        w.signals.error.connect(self.display_result)

        self.workers.enqueue(w)

    # end::startWorker[]

    def display_result(self, job_id, data):
        self.text.appendPlainText("WORKER %s: %s" % (job_id, data))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
