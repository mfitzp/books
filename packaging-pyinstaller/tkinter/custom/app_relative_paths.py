import os
import tkinter as tk

basedir = os.path.dirname(__file__)


window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()


button_icon = tk.PhotoImage(file=os.path.join(basedir, "icon.png"))
button = tk.Button(text="My simple app.", image=button_icon)
button.bind("<Button-1>", handle_button_press)
button.pack()

# Set window icon.
window.iconbitmap(os.path.join(basedir, "icon.ico"))

window.mainloop()
