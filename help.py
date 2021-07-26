from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

root = Tk()
root.title('Codemy.com - Tkinter Help!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

# List of widgets
# Button, Canvas, Checkbutton, Entry, Frame, 
# Label, LabelFrame, Listbox, Menu, Menubutton, Message, 
# Radiobutton, Scale

my_help = str(help(colorchooser))
print(my_help)

#TTK
# Button, Checkbutton, Entry, Frame, Label, 
# LabelFrame, Menubutton, PanedWindow, 
#Radiobutton, Scale, Scrollbar, and Spinbox. 

# New TTK
#Combobox, Notebook, Progressbar, Separator, 
#Sizegrip and Treeview


root.mainloop()