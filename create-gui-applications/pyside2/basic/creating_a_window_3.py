from PySide2.QtWidgets import QApplication, QMainWindow

import sys


app = QApplication(sys.argv)

window = QMainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
