import psutil
from tkinter import *
from tkinter import ttk
import time

battery_data = psutil.sensors_battery()
battery_percent = battery_data.percent

# Configure the main frame window

root = Tk()
root.title("Battery Status")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(200, 70)
root.maxsize(400, 70)
root.geometry("200x70")  # Default size

if battery_data.percent >= 66:
    root.iconbitmap("resources/1.ico")
elif 33 <= battery_data.percent < 66:
    root.iconbitmap("resources/2.ico")
elif battery_data.percent < 33:
    root.iconbitmap("resources/3.ico")

# Design
battery_percentage = ttk.Label(mainframe, text="Battery Percentage").grid(
    column=1, row=1, sticky=(W, E), pady=5
)
battery_pluggable = ttk.Label(mainframe, text="Is plugged?").grid(
    column=1, row=3, sticky=(W, E), pady=5
)
separator_hor = ttk.Separator(mainframe, orient="horizontal").grid(
    column=1, row=2, sticky=(W, E), columnspan=50
)
separator_ver = ttk.Separator(mainframe, orient="vertical").grid(
    column=2, row=1, sticky=(N, S), rowspan=50
)  # Not necessary to be 50


# Second column
if battery_data.power_plugged:
    ttk.Label(mainframe, text="Yes").grid(column=3, row=3, sticky=(W, E), pady=5)
else:
    ttk.Label(mainframe, text="Nah").grid(column=3, row=3, sticky=(W, E), pady=5)

# why do you do this to me
x = "{}%".format(battery_data.percent)
ttk.Label(mainframe, text=x).grid(column=3, row=1, sticky=(W, E), pady=5)


# Loop to keep it running
root.mainloop()
