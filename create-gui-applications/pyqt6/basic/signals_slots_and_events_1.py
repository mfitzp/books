from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title will be passed to the function.
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is discarded in the lambda and the
        # function is called without parameters.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter. Extra data is passed from
        # within the lambda.
        self.windowTitleChanged.connect(
            lambda x: self.my_custom_fn(x, 25)
        )

        # This sets the window title which will trigger all the above signals
        # sending the new title to the attached functions or lambdas as the
        # first parameter.
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

    # SLOT: This accepts a string, e.g. the window title, and prints it
    def onWindowTitleChange(self, s):
        print(s)

    # SLOT: This has default parameters and can be called without a value
    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)



# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
