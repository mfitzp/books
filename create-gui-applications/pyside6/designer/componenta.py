from componenta_ui import Ui_ComponentA

from PySide6.QtWidgets import QWidget

class ComponentA(QWidget, Ui_ComponentA):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(
            self.handle_lineedit_changed
        )

    def handle_lineedit_changed(self, s):
        print(s)
