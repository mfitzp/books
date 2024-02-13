import wx
import sys


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 300))
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.sizer.Add(self.text, wx.EXPAND, wx.EXPAND)

        if __file__ in sys.argv:  # <1>
            sys.argv.remove(__file__)

        if sys.argv:  # <2>
            filename = sys.argv[0]  # <3>
            self.text.LoadFile(filename)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.Show()


app = wx.App(False)
w = MainWindow(None, "Text viewer")
app.MainLoop()
