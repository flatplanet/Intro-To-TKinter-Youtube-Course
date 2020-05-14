from tkinter import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

def number():
	try:
		value = int(my_box.get())
		answer.config(text="You Entered A Number")
	except ValueError:
		answer.config(text="That's Not A Number!")
	
	
	my_box.delete(0, END)

my_label = Label(root, text="Enter a Number")
my_label.pack(pady=20)

my_box = Entry(root)
my_box.pack(pady=20)

my_button = Button(root, text="Enter Number", command=number)
my_button.pack(pady=5)

answer = Label(root, text='')
answer.pack(pady=20)

root.mainloop()

