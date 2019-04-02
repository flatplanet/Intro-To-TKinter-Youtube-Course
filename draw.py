from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

w = Scale(root, from_=0, to=100)
w.pack()



def see(val):
	root.geometry(str(w.get()) + "x" + str(w.get()))
	mylbl = Label(root, text=val).pack()	

w = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=see)
w.pack()

mybtn = Button(root, text="click", command=see).pack()
mainloop()
