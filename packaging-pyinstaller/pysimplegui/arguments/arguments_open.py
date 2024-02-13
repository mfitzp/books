import PySimpleGUI as sg
import sys


if __file__ in sys.argv:  # <1>
    sys.argv.remove(__file__)

text = ""
if sys.argv:  # <2>
    filename = sys.argv[0]  # <3>
    with open(filename, "r") as f:
        text = f.read()

layout = [
    [sg.Text(text)],
]

window = sg.Window("Hello World", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()
