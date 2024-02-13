import PySimpleGUI as sg
import os
import base64

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


def icon(filename):
    path = os.path.join(basedir, "icons", filename)
    with open(path, "rb") as f:
        return base64.b64encode(f.read())


layout = [
    [sg.Text("My simple app.")],
    [
        sg.Button(
            "Push",
            image_data=icon("icon.png"),
        )
    ],
]

window = sg.Window(
    "Hello World", layout, icon=os.path.join(basedir, "icon.ico")
)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Push":
        break

window.close()
