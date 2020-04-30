from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")


my_notebook = ttk.Notebook(root)
my_notebook.pack()

def hide():
	my_notebook.hide(1)

def show():
	my_notebook.add(my_frame2, text="Red Tab")

def select():
	my_notebook.select(1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Blue Tab")
my_notebook.add(my_frame2, text="Red Tab")

# Hide a tab
my_button = Button(my_frame1, text="Hide Tab 2", command=hide).pack(pady=10)

# Show a tab
my_button2 = Button(my_frame1, text="Show Tab 2", command=show).pack(pady=10)

# Navigate to a tab
my_button3 = Button(my_frame1, text="Navigate To Tab 2", command=select).pack(pady=10)



root.mainloop()

