from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

import sys


from PyQt6.QtWidgets import (
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
darkPalette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
darkPalette.setColor(
    QPalette.ColorRole.WindowText, Qt.GlobalColor.white
)
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.WindowText,
    QColor(127, 127, 127),
)
darkPalette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
darkPalette.setColor(
    QPalette.ColorRole.AlternateBase, QColor(66, 66, 66)
)
darkPalette.setColor(
    QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white
)
darkPalette.setColor(
    QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white
)
darkPalette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.Text,
    QColor(127, 127, 127),
)
darkPalette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
darkPalette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
darkPalette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
darkPalette.setColor(
    QPalette.ColorRole.ButtonText, Qt.GlobalColor.white
)
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.ButtonText,
    QColor(127, 127, 127),
)
darkPalette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
darkPalette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.Highlight,
    QColor(80, 80, 80),
)
darkPalette.setColor(
    QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white
)
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.HighlightedText,
    QColor(127, 127, 127),
)

window = MainWindow()  # Replace with your custom mainwindow.
window.show()

app.setPalette(darkPalette)


app.exec()
