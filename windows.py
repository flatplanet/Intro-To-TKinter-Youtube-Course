from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')

global counter
counter = 1

def open():
	global counter

	# Create counter logic
	if counter < 4:
		top = Toplevel()
		top.geometry("300x200")
		top.title('New Window')
		top.iconbitmap('c:/gui/codemy.ico')

		my_label = Label(top, text="New Window!", font=("Helvetica, 24"))
		my_label.pack(pady=50, padx=50)

		counter +=1
	else:
		messagebox.showinfo("Error", "Hey! You've already opened a new window!")


my_button = Button(root, text="Open Window", command=open)
my_button.pack(pady=50, padx=50)

mainloop()