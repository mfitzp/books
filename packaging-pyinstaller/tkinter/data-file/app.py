import os
import tkinter as tk

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

window = tk.Tk()
window.title("Hello World")

label = tk.Label(text="My simple app.")
label.pack()


def handle_button_press(event):
    window.destroy()


button_icon = tk.PhotoImage(file=os.path.join(basedir, "icon.png"))
button = tk.Button(text="My simple app.", image=button_icon)
button.bind("<Button-1>", handle_button_press)
button.pack()

# Set window icon.
window.iconbitmap(os.path.join(basedir, "icon.ico"))

# Start the event loop.
window.mainloop()
