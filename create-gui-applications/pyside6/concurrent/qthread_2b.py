import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Thread(QThread):
    """
    Worker thread
    """

    result = Signal(str)

    @Slot()
    def run(self):
        """
        Your code goes in this method
        """
        print("Thread start")
        counter = 0
        while True:
            time.sleep(0.1)
            # Output the number as a formatted string.
            self.result.emit(f"The number is {counter}")
            counter += 1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create thread and start it.
        self.thread = Thread()
        self.thread.start()

        label = QLabel("Output will appear here")
        button = QPushButton("Kill thread")
        # Terminate (kill immediately) the thread.
        button.pressed.connect(self.thread.terminate)

        # Connect signal, so output appears on label.
        self.thread.result.connect(label.setText)
        self.thread.finished.connect(self.thread_has_finished)  # <1>

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        container.setLayout(layout)

        self.setCentralWidget(container)

    def thread_has_finished(self):
        print("Thread has finished.")
        print(
            self.thread,
            self.thread.isRunning(),
            self.thread.isFinished(),
        )  # <2>



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
