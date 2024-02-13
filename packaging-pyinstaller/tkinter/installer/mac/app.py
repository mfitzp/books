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


button_close_icon = tk.PhotoImage(
    file=os.path.join(basedir, "icons", "lightning.png")
)
button_close = tk.Button(
    text="Close",
    image=button_close_icon,
)
button_close.bind("<Button-1>", handle_button_press)
button_close.pack()

button_maximimize_icon = tk.PhotoImage(
    file=os.path.join(basedir, "icons", "uparrow.png")
)
button_maximize = tk.Button(
    text="Maximize",
    image=button_maximimize_icon,
)
button_maximize.bind("<Button-1>", handle_button_press)
button_maximize.pack()

# Set window icon.
window.iconbitmap(os.path.join(basedir, "icons", "icon.ico"))

# Start the event loop.
window.mainloop()
