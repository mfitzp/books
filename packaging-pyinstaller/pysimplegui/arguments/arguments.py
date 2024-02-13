import PySimpleGUI as sg
import sys


layout = []
for arg in sys.argv:  # <1>
    layout.append(
        [sg.Text(arg)],
    )

window = sg.Window("Hello World", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()
