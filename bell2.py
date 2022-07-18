import pprint
from tkinter import *
from tkinter import ttk



root = Tk()




w = ttk.Spinbox(root, show="*")
w.pack()
pprint.pprint(w.config())

#exec(open("age.py").read())


root.mainloop()