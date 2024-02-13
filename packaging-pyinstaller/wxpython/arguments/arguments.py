import wx
import sys


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        for arg in sys.argv:  # <1>
            label = wx.StaticText(self, label=arg)
            self.sizer.Add(label)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.Show()

    def handle_button_click(self, event):
        self.Close()


app = wx.App(False)
w = MainWindow(None, "Arguments")
app.MainLoop()
