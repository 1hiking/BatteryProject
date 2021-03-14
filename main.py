import psutil
from tkinter import *
from tkinter import ttk

battery_data = psutil.sensors_battery()


# Logic
def print_percentage():
    print('{}%'.format(battery_data.percent))  # why do you do this to me


def print_status_plugged():
    print(battery_data.power_plugged)


# Configure the main frame window
root = Tk()
root.title("Battery Status")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(300, 100)

if battery_data.percent >= 75:
    root.iconbitmap("resources/1.ico")
elif 50 <= battery_data.percent < 75:
    root.iconbitmap("resources/2.ico")
elif 25 <= battery_data.percent < 50:
    root.iconbitmap("resources/3.ico")
elif battery_data.percent < 25:
    root.iconbitmap("resources/4.ico")

# Design
ttk.Label(mainframe, text="Battery Percentage").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Is plugged?").grid(column=1, row=2, sticky=(W, E))

# Loop to keep it running
root.mainloop()
