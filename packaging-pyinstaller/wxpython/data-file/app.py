import os
import wx

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))

        self.label = wx.StaticText(self, label="My simple app.")
        self.button = wx.Button(self, label="Push")
        self.Bind(
            wx.EVT_BUTTON, self.handle_button_click, self.button
        )

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label)
        self.sizer.Add(self.button)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.Show()

    def handle_button_click(self, event):
        self.Close()


app = wx.App(False)
w = MainWindow(None, "Hello World")
w.SetIcon(wx.Icon(os.path.join(basedir, "icon.ico")))
app.MainLoop()
