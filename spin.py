from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")

def grab():
	my_label.config(text=my_spin.get())

names = ("John", "Tim", "Mary", "Tina")
#my_spin = Spinbox(root, from_=0, to=10, increment=2, font=("Helvetica", 20))
my_spin = Spinbox(root, values=names,  font=("Helvetica", 20))
my_spin.pack(pady=20)

my_button = Button(root, text="Submit", command=grab)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()