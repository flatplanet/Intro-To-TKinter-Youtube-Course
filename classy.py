from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")


class Elder:

	def __init__(self, master):
		myFrame = Frame(master)
		myFrame.pack()

		self.myButton = Button(master, text="Click Me!", command=clicker)
		self.myButton.pack(pady=20)

	def clicker(self):
		print("Look at you...you clicked a button!")

e = Elder(root)


root.mainloop()