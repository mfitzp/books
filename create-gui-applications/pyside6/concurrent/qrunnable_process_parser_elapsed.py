import re
import subprocess
import sys

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def timestr_to_seconds(s):
    """
    Convert a string in the format 00:00:00 into seconds.
    """
    hours, minutes, seconds = s.split(":")
    hours = int(hours) * 3600
    minutes = int(minutes) * 60
    seconds = int(seconds)
    return hours + minutes + seconds


total_re = re.compile("Total time: (\d\d:\d\d:\d\d)")
elapsed_re = re.compile("Elapsed time: (\d\d:\d\d:\d\d)")


def time_to_percent_parser(line):
    """
    Extract the elepsed time value and the total time value,
    and use them to calculate a % complete.
    """
    total_time = None
    elapsed_time = None

    output = "".join(line)  # Turn into a single string.

    m = total_re.findall(output)
    if m:
        # Should only be one of these.
        total_time = timestr_to_seconds(m[0])

    m = elapsed_re.findall(output)
    if m:
        # Get the last match (latest result) using -1 on the list.
        elapsed_time = timestr_to_seconds(m[-1])

    # If we have both the latest, and the target, we can calculate %.
    if total_time and elapsed_time:
        return int(100 * elapsed_time / total_time)




class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished: No data
    result: str
    """

    result = Signal(
        str
    )  # Send back the output from the process as a string.
    progress = Signal(
        int
    )  # Return an integer 0-100 showing the current progress.
    finished = Signal()


class SubProcessWorker(QRunnable):
    """
    ProcessWorker worker thread

    Inherits from QRunnable to handle worker thread setup, signals and wrap-up.

    :param command: command to execute with `subprocess`.

    """

    def __init__(self, command, parser=None):
        super().__init__()

        # Store constructor arguments (re-used for processing).
        self.signals = WorkerSignals()

        # The command to be executed.
        self.command = command

        # The parser function to extract the progress information.
        self.parser = parser

    # tag::workerRun[]
    @Slot()
    def run(self):
        """
        Initialize the runner function with passed args, kwargs.
        """

        result = []

        with subprocess.Popen(  # <1>
            self.command,
            bufsize=1,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # <2>
            universal_newlines=True,
        ) as proc:
            while proc.poll() is None:
                data = proc.stdout.readline()  # <3>
                result.append(data)
                if self.parser:  # <4>
                    value = self.parser(result)
                    if value:
                        self.signals.progress.emit(value)

        output = "".join(result)

        self.signals.result.emit(output)

    # end::workerRun[]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        btn_run = QPushButton("Execute")
        btn_run.clicked.connect(self.start)

        layout.addWidget(btn_run)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        # Thread runner
        self.threadpool = QThreadPool()


    # tag::start[]
    def start(self):
        # Create a runner
        self.runner = SubProcessWorker(
            command="python dummy_script.py",
            parser=time_to_percent_parser,
        )
        self.runner.signals.result.connect(self.result)
        self.runner.signals.progress.connect(self.progress.setValue)
        self.threadpool.start(self.runner)

    # end::start[]

    def result(self, s):
        self.text.appendPlainText(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
