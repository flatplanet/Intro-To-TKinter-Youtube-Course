from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Notebook Tabs")
root.geometry("500x500")
root.iconbitmap('c:/guis/codemy.ico')



def hide():
 	my_notebook.hide(1)

def show():
	my_notebook.add(my_frame2, text="Red Tab")
def switch():
	my_notebook.select(1)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Blue Tab")
my_notebook.add(my_frame2, text="Red Tab")

style = ttk.Style()
style.configure("my_notebook.Tab", foreground="black", background="white")

my_button = Button(my_frame1, text="hide tab 2", command=hide).pack(pady=15)

my_button2 = Button(my_frame1, text="show tab 2", command=show).pack(pady=15)

my_button3 = Button(my_frame1, text="switch to tab 2", command=switch).pack(pady=15)

root.mainloop()