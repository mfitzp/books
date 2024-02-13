from fbs_runtime.application_context.PySide2 import (ApplicationContext,
                                                   cached_property)


class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def main_window(self):
        return MainWindow(self)  # Pass context to the window.

# ... snip ...
