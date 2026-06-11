from componentb_ui import Ui_ComponentB

from PySide6.QtWidgets import QWidget

class ComponentB(QWidget, Ui_ComponentB):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dial.valueChanged.connect(self.handle_dial_changed)

    def handle_dial_changed(self, value):
        print(value)
