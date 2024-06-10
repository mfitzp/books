from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

import sys


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLCDNumber,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QWidget,  # <1>
    QVBoxLayout,  # <2>
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            widget = w(self)
            widget.setAutoFillBackground(True)
            layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
app.setStyle("Fusion")

darkPalette = app.palette()
darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
darkPalette.setColor(QPalette.WindowText, Qt.white)
darkPalette.setColor(
    QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127)
)
darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
darkPalette.setColor(QPalette.ToolTipText, Qt.white)
darkPalette.setColor(QPalette.Text, Qt.white)
darkPalette.setColor(
    QPalette.Disabled, QPalette.Text, QColor(127, 127, 127)
)
darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ButtonText, Qt.white)
darkPalette.setColor(
    QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127)
)
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(
    QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80)
)
darkPalette.setColor(QPalette.HighlightedText, Qt.white)
darkPalette.setColor(
    QPalette.Disabled,
    QPalette.HighlightedText,
    QColor(127, 127, 127),
)

window = MainWindow()  # Replace with your custom mainwindow.
window.show()

app.setPalette(darkPalette)


app.exec()
