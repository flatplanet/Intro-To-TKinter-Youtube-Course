from tkinter import *

root = Tk()
root.title('Codemy.com - Justify Labels')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x550")


my_label1 = Label(root, 
	text="Stuff\nStuff Stuff\nStuff Stuff Stuff",
	font=("Helvetica", 18),
	bd=1, relief="sunken")
my_label1.attributes('-alpha', 0.9)
my_label1.pack(pady=20, ipady=10, ipadx=10)


my_label2 = Label(root, 
	text="Stuff\nStuff Stuff\nStuff Stuff Stuff",
	font=("Helvetica", 18),
	bd=1, relief="sunken",
	justify="left")
my_label2.pack(pady=20, ipady=10, ipadx=10)


my_label3 = Label(root, 
	text="Stuff\nStuff Stuff\nStuff Stuff Stuff",
	font=("Helvetica", 18),
	bd=1, relief="sunken",
	justify="right")
my_label3.pack(pady=20, ipady=10, ipadx=10)


root.mainloop()