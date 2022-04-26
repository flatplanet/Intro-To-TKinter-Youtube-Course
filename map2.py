from tkinter import *
import tkintermapview
from tkinter import ttk

root = Tk()
root.title('Codemy.com - Tkinter MapView')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("900x800")


def lookup():
	map_widget.set_address(my_entry.get())
	my_slider.config(value=9)

def slide(e):
	map_widget.set_zoom(my_slider.get())

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
# Set Coordinates
#map_widget.set_position(36.1699, -115.1396) # Vegas Baby!

# Set Address
map_widget.set_address("10 West Elm St., Chicago, IL, United States")

# Set A Zoom Level
map_widget.set_zoom(20)


map_widget.pack()


my_frame = LabelFrame(root)
my_frame.pack(pady=10)

my_entry = Entry(my_frame, font=("Helvetica", 28))
my_entry.grid(row=0, column=0, pady=20, padx=10)

my_button = Button(my_frame, text="Lookup", font=("Helvetica", 18), command=lookup)
my_button.grid(row=0, column=1, padx=10)

my_slider = ttk.Scale(my_frame, from_=4, to=20, orient=HORIZONTAL, command=slide, value=20, length=220)
my_slider.grid(row=0, column=2, padx=10)



root.mainloop()