from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

# Drop Down Boxes

def clicking(event):
	myLabel = Label(root, text=droped.get()).pack()

def clicker(event):
	myLabel = Label(root, text=clicked.get()).pack()

def show():
	myLabel = Label(root, text=clicked.get()).pack()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday",
	"Saturday"
]	

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=clicker)

drop.pack()

droped = ttk.Combobox(root, value=["Search by...", "Last Name", "Email Address", "Customer ID"])
droped.current(0)
droped.bind("<<ComboboxSelected>>", clicking)
droped.pack()
	


#myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()

