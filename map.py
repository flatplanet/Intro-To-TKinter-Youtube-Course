from tkinter import *
import tkintermapview

root = Tk()
root.title('Codemy.com - Tkinter MapView')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("900x700")

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



root.mainloop()