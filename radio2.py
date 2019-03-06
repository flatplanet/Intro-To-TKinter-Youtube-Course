from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')


r = IntVar()

def press(thing):
	myLabel = Label(root, text=thing)
	myLabel.pack()	

Radiobutton(root, text="One", variable=r, value=1, command=lambda: press(r.get())).pack(anchor=W)
Radiobutton(root, text="Two", variable=r, value=2, command=lambda: press(r.get())).pack(anchor=W)

MODES = [
        ("Pepperoni", "Pepperoni"),
        ("Cheese", "Cheese"),
        ("Mushroom", "Mushroom"),
        ("Onion", "Onion"),
    ]

pizza = StringVar()
pizza.set("Pepperoni") # initialize

for text, mode in MODES:
    b = Radiobutton(root, text=text,
                    variable=pizza, value=mode)
    b.pack(anchor=W)



myLabel = Label(root)
myLabel.pack()

myButton = Button(root, text="Click Me!!", command=lambda: press(pizza.get()))
myButton.pack()

mainloop()