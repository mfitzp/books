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
    # end::thread[]
    """
    Worker thread
    """

    result = Signal(str)

    def __init__(self, initial_counter):
        super().__init__()
        self.counter = initial_counter

    @Slot()
    def run(self):
        """
        Your code goes in this method
        """
        print("Thread start")
        self.is_running = True
        self.waiting_for_data = True
        while True:
            while self.waiting_for_data:
                if not self.is_running:
                    return  # Exit thread.
                time.sleep(0.1)  # wait for data <1>.

            # Output the number as a formatted string.
            self.counter += self.input_add
            self.counter *= self.input_multiply
            self.result.emit(f"The cumulative total is {self.counter}")
            self.waiting_for_data = True

    # tag::data_methods[]
    def send_add(self, add):
        self.input_add = add

    def send_multiply(self, multiply):
        self.input_multiply = multiply

    def calculate(self):
        self.waiting_for_data = False  # Release the lock & calculate.

    # end::data_methods[]
    def stop(self):
        self.is_running = False


class MainWindow(QMainWindow):
    # end::mainwindow[]
    def __init__(self):
        super().__init__()

        # Create thread and start it.
        self.thread = Thread(500)
        self.thread.start()

        self.add_input = QSpinBox()
        self.mult_input = QSpinBox()
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
        layout.addWidget(self.add_input)
        layout.addWidget(self.mult_input)
        layout.addWidget(button_input)
        layout.addWidget(label)
        layout.addWidget(button_stop)
        container.setLayout(layout)

        self.setCentralWidget(container)

    # tag::submit_data[]
    def submit_data(self):
        # Submit the value in the numeric_input widget to the thread.
        self.thread.send_add(self.add_input.value())
        self.thread.send_multiply(self.mult_input.value())
        self.thread.calculate()

    # end::submit_data[]

    def thread_has_finished(self):
        print("Thread has finished.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
