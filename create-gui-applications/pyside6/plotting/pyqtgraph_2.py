import sys


from PySide6.QtWidgets import QMainWindow, QApplication
import pyqtgraph as pg  # import PyQtGraph after PySide6


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.graphWidget.setBackground("w")
        self.graphWidget.plot(hour, temperature)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
