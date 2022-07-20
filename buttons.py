from tkinter import *


class Button(TK):
	super().__init__()
	self.geometry("800x400")
	
	def myClick():
		self.myLabel = Label(self, text="Look! I clicked a Button!!")
		self.myLabel.pack()

	def create_button():
		self.btn = Button(self, text="Click Me!", command=myClick)
	def run():
		self.mainloop()	
		
b = Button()
b.create_button()
b.run()
