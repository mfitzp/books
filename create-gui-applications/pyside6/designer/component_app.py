import sys

from componenta import ComponentA
from componentb import ComponentB
from mainwindow_tabs_ui import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.component_a = ComponentA()
        self.component_b = ComponentB()

        # Get central widget from window.
        widget = self.centralWidget()

        # Get layout from central Widget.
        layout = widget.layout()

        layout.addWidget(self.component_a)
        layout.addWidget(self.component_b)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
