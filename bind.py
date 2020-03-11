from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

def clicker(event):
	myLabel = Label(root, text="You clicked this button: " + event.keysym)
	myLabel.pack()

myButton = Button(root, text="Click Me")
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)


root.mainloop()