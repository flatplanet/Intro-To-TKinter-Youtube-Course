from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Codemy.com")
root.geometry("400x400")
root.iconbitmap('c:/guis/codemy.ico')

def color():
	my_color = colorchooser.askcolor()[1]
	my_label = Label(root, text=my_color).pack(pady=10)
	my_label2 = Label(root, text="You Picked a Color!", font=("Helvetica", 32), bg=my_color).pack()

my_button = Button(root, text="Pick A Color", command=color).pack()

root.mainloop()