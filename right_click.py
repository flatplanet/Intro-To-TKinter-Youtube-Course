from tkinter import *

root = Tk()
root.title('Codemy.com - Right Click Menu')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x550")

my_label = Label(root, text="", font=("Helvetica", 20))
my_label.pack(pady=20)

def hello():
	my_label.config(text="Hello World!")

def goodbye():
	my_label.config(text="Goodbye World!")

def my_popup(e):
	my_menu.tk_popup(e.x_root, e.y_root)

# Create a Menu
my_menu = Menu(root, tearoff=False)
my_menu.add_command(label="Say Hello", command=hello)
my_menu.add_command(label="Say Goodbye", command=goodbye)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)

root.bind("<Button-3>", my_popup)


root.mainloop()