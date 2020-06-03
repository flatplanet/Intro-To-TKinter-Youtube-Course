from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title("Codemy.com")
root.geometry("800x500")
root.iconbitmap('c:/gui/codemy.ico')





def change(e):
	my_pic = PhotoImage(file="images/aspen2.png")
	my_label.config(image=my_pic)
	my_label.image = my_pic

def change_back(e):
	my_pic = PhotoImage(file="images/aspen.png")
	my_label.config(image=my_pic)
	my_label.image = my_pic

def do_something():
	label2 = Label(root, text="You clicked the button!")
	label2.pack()

my_pic = PhotoImage(file="images/aspen.png")
my_label = Button(root, image=my_pic, command=do_something)
my_label.pack(pady=20)

def exit(e):
	root.quit()

my_label.bind("<Enter>", change)
my_label.bind("<Leave>", change_back)
my_label.bind("<Return>", exit)

root.mainloop()