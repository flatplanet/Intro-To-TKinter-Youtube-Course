from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")


class Elder:

	def __init__(self, master):
		myFrame = Frame(master)
		myFrame.bind("<Key>", self.key)
		myFrame.pack()

		self.myButton = Button(master, text="Click Me!")
		self.myButton.bind("<Button-1>", self.clicker)
		self.myButton.pack(pady=20)

	def clicker(self, event):
		print("Look at you...you clicked a button! ", event.char)

	def key(self, event):
		print("You pressed this key: ", char)
	

e = Elder(root)

root.mainloop()