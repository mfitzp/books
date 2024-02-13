import os
import wx

basedir = os.path.dirname(__file__)


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))

        image = wx.Bitmap(os.path.join(basedir, "icon.ico"))
        self.button = wx.Button(self, label="My simple app.")
        self.button.SetBitmap(image)
        self.Bind(
            wx.EVT_BUTTON, self.handle_button_click, self.button
        )

        self.sizer = wx.BoxSizer(wx.VERTICAL)
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
