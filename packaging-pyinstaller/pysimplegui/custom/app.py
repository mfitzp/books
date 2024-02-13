import PySimpleGUI as sg


layout = [[sg.Button("My simple app.")]]

window = sg.Window("Hello World", layout, icon="icon.ico")

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "My simple app.":
        break

window.close()
