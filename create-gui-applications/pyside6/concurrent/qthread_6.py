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

    def send_data(self, add, multiply):
        """
        Receive data onto internal variable.
        """
        self.input_add = add
        self.input_multiply = multiply
        self.waiting_for_data = False

    def stop(self):
        self.is_running = False



class MainWindow(QMainWindow):
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

    def submit_data(self):
        # Submit the value in the numeric_input widget to the thread.
        self.thread.send_data(
            self.add_input.value(), self.mult_input.value()
        )

    def thread_has_finished(self):
        print("Thread has finished.")

    # end::mainwindow[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
