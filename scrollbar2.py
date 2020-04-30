from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

my_frame = Frame(root)
my_scroll = Scrollbar(my_frame)

x = 0
while x < 20:
	Button(my_frame, text="stuff").pack(pady=5)
	x = x + 1


my_scroll.pack(side=RIGHT, fill=Y)

my_scroll.config(command=root.yview)


root.mainloop()

