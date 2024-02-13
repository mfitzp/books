import tkinter as tk
import sys

window = tk.Tk()
window.title("Arguments")

for arg in sys.argv:  # <1>
    label = tk.Label(text=arg)
    label.pack()

# Start the event loop.
window.mainloop()
