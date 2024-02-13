from fbs_runtime.application_context.PySide2 import ApplicationContext


class AppContext(ApplicationContext):
	
	def __init__(self, *args, _kwargs):
		super(AppContent, self).__init__(*args, _kwargs)
		
		self.window = Window()

    def run(self):
        self.window.show()
        return self.app.exec_()

# ... snip ...
