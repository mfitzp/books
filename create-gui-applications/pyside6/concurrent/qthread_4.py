import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
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
        self.data = None
        self.is_running = True
        print("Thread start")
        counter = 0
        while self.is_running:
            while self.data is None:
                time.sleep(0.1)  # wait for data <1>.

            # Output the number as a formatted string.
            counter += self.data
            self.result.emit(f"The cumulative total is {counter}")
            self.data = None

    def send_data(self, data):
        """
        Receive data onto internal variable.
        """
        self.data = data

    def stop(self):
        self.is_running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create thread and start it.
        self.thread = Thread()
        self.thread.start()

        self.numeric_input = QSpinBox()
        button_input = QPushButton("Submit number")

        label = QLabel("Output will appear here")

        button_stop = QPushButton("Shutdown thread")
        # Shutdown the thread nicely.
        button_stop.pressed.connect(self.thread.stop)

        # Connect signal, so output appears on label.
        button_input.pressed.connect(self.submit_data)
        self.thread.result.connect(label.setText)
        self.thread.finished.connect(self.thread_has_finished)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.numeric_input)
        layout.addWidget(button_input)
        layout.addWidget(label)
        layout.addWidget(button_stop)
        container.setLayout(layout)

        self.setCentralWidget(container)

    def submit_data(self):
        # Submit the value in the numeric_input widget to the thread.
        self.thread.send_data(self.numeric_input.value())

    def thread_has_finished(self):
        print("Thread has finished.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
