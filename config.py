from tkinter import *


root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")


def something():
	my_label.config(text="This is new text!!", font=("Helvetica", 8))
	root.config(bg="blue")
	my_button.config(text="You've been configged!", state=DISABLED, pady=30)



my_label = Label(root, text="This is my text", font=("Helvetica", 18))
my_label.pack(pady=10)


my_button = Button(root, text="Click Me", command=something)
my_button.pack(pady=10)






root.mainloop()

