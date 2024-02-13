import base64
import os

import PySimpleGUI as sg

basedir = os.path.dirname(__file__)


def icon(filename):
    path = os.path.join(basedir, filename)
    with open(path, "rb") as f:
        return base64.b64encode(f.read())


layout = [
    [
        sg.Button(
            "My simple app.",
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
    if event == sg.WIN_CLOSED or event == "My simple app.":
        break

window.close()
