from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

def selected(event):
	#myLabel = Label(root, text=clicked.get()).pack()
	if clicked.get() == 'Friday':
		myLabel = Label(root, text="Yay! It's Friday").pack()
	else:
		myLabel = Label(root, text=clicked.get()).pack()


def comboclick(event):
	#myLabel = Label(root, text=myCombo.get()).pack()
	if myCombo.get() == 'Friday':
		myLabel = Label(root, text="Yay! It's Friday").pack()
	else:
		myLabel = Label(root, text=myCombo.get()).pack()


options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()


#myButton = Button(root, text="select from list", command=selected)
#myButton.pack()

root.mainloop()