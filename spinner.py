from tkinter import *


root = Tk()
root.title('Codemy.com - Reset Spinner')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x350")

def reset():
	#var = IntVar(root)
	#var.set(0)
	var2 = StringVar(root)
	var2.set("John")
	my_spin.config(textvariable=var2)

# Set intvar
var = IntVar(root)
var.set(20)

# Set Stringvar
var2 = StringVar(root)
var2.set("John")


#from_=0, to=100,
my_spin = Spinbox(root, 
	values=("John", "Mary", "Bob", "Tina"), 
	font=("helvetica", 20),
	textvariable=var2)

my_spin.pack(pady=20)

my_button = Button(root, text="reset spinner", command=reset)
my_button.pack(pady=20)


root.mainloop()