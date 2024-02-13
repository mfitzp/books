import tkinter as tk
import sys

window = tk.Tk()
window.title("Text viewer")


if __file__ in sys.argv:  # <1>
    sys.argv.remove(__file__)


def open_file(filename):
    with open(filename, "r") as f:
        return f.read()


text = ""
if sys.argv:  # <2>
    filename = sys.argv[0]  # <3>
    text = open_file(filename)


textbox = tk.Text()
textbox.insert(tk.END, text)
textbox.pack()

# Start the event loop.
window.mainloop()
