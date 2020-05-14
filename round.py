from tkinter import *

root = Tk()
root.title('Codemy.com - Rounded Buttons')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")


def thing():
	my_label.config(text="You clicked the button...")

login_btn = PhotoImage(file='images/login.png')

img_label = Label(image=login_btn, text="THIS IS A THING", compound=CENTER)
img_label.pack(pady=20)


my_button = Button(root, image=login_btn, command=thing, borderwidth=0)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)


mainloop()