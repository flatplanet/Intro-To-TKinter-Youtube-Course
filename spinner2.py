from tkinter import *


root = Tk()
root.title('Codemy.com - Set Spinner')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x350")


var = IntVar(root)
var.set(0)

var2 = StringVar(root)
var2.set("John")

def reset():
	var = IntVar(root)
	var.set(0)
	#var2 = StringVar(root)
	#var2.set("John")
	my_spin.config(textvariable=var)
# from_=0, to=100,
#values=("John", "Tina", "Bob", "Mary")
my_spin = Spinbox(root, from_=0, to=100, font=("helvtica", 20), textvariable=var)
my_spin.pack(pady=20)

my_button = Button(root, text="Reset Spinbox", command=reset)
my_button.pack(pady=20)


root.mainloop()