from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('c:/gui/codemy.ico')

def open():
	global my_img1
	root.filename =  filedialog.askopenfilename(initialdir = "/gui/images",title = "Select file", filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
	my_img1 = ImageTk.PhotoImage(Image.open(root.filename))
	my_label = Label(image=my_img1).pack()
	my_label2 = Label(root, text=root.filename).pack()
btn = Button(root, text="Open File", command=open).pack()


root.mainloop()