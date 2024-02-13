import subprocess
import sys
import time
import traceback
import uuid
from collections import namedtuple

from PySide2.QtCore import (QObject, QRunnable, Qt, QThreadPool, QTimer,
                          Signal, Slot)
from PySide2.QtWidgets import (
    QApplication, QLineEdit, QMainWindow, QPushButton, QSpinBox, QVBoxLayout,
    QWidget)


def extract_vars(l):
    """
    Extracts variables from lines, looking for lines
    containing an equals, and splitting into key=value.
    """    
    data = {}
    for s in l.splitlines():
        if '=' in s:
            name, value = s.split('=')
            data[name] = value  

    data['number_of_lines'] = len(l)
    return data
    

class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished: No data
    result: dict
    """

    result = Signal(dict)  # Send back the output as dictionary.
    finished = Signal()


class SubProcessWorker(QRunnable):
    """
    ProcessWorker worker thread

    Inherits from QRunnable to handle worker thread setup, signals and wrap-up.
    
    :param command: command to execute with `subprocess`.

    """

    def __init__(self, command, process_result=None):
        super().__init__()

        # Store constructor arguments (re-used for processing).
        self.signals = WorkerSignals()

        # The command to be executed.
        self.command = command

        # The post-processing fn.
        self.process_result = process_result

    @Slot()
    def run(self):
        """
        Execute the command, returning the result.
        """
        output = subprocess.getoutput(self.command)

        if self.process_result:
            output = self.process_result(output)

        self.signals.result.emit(output)
        self.signals.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Some buttons
        layout = QVBoxLayout()

        self.name = QLineEdit()
        layout.addWidget(self.name)

        self.country = QLineEdit()
        layout.addWidget(self.country)

        self.website = QLineEdit()
        layout.addWidget(self.website)

        self.number_of_lines = QSpinBox()
        layout.addWidget(self.number_of_lines)

        btn_run = QPushButton("Execute")
        btn_run.clicked.connect(self.start)

        layout.addWidget(btn_run)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        # Thread runner
        self.threadpool = QThreadPool()

        self.show()

    def start(self):
        # Create a runner
        self.runner = SubProcessWorker(
            "python dummy_script.py", process_result=extract_vars
        )
        self.runner.signals.result.connect(self.result)
        self.threadpool.start(self.runner)

    def result(self, data):
        print(data)
        self.name.setText(data['name'])
        self.country.setText(data['country'])
        self.website.setText(data['website'])
        self.number_of_lines.setValue(data['number_of_lines'])


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
