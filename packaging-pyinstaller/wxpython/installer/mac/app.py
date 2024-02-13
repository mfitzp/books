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

        image = wx.Bitmap(
            os.path.join(basedir, "icons", "lightning.png")
        )
        self.button_close = wx.Button(self, label="Close")
        self.button_close.SetBitmap(image)
        self.Bind(
            wx.EVT_BUTTON, self.handle_close_button, self.button_close
        )

        image = wx.Bitmap(
            os.path.join(basedir, "icons", "uparrow.png")
        )
        self.button_maximize = wx.Button(self, label="Maximize")
        self.button_maximize.SetBitmap(image)
        self.Bind(
            wx.EVT_BUTTON,
            self.handle_maximize_button,
            self.button_maximize,
        )

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label)
        self.sizer.Add(self.button_close)
        self.sizer.Add(self.button_maximize)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.Show()

    def handle_close_button(self, event):
        self.Close()

    def handle_maximize_button(self, event):
        self.Maximize()


app = wx.App(False)
w = MainWindow(None, "Hello World")
w.SetIcon(wx.Icon(os.path.join(basedir, "icons", "icon.ico")))
app.MainLoop()
