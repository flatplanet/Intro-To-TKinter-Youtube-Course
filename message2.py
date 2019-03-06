from tkinter import *
#from tkmessagebox import *
from tkinter import messagebox

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

top = Tk()

def hello():
	response = messagebox.askokcancel("Say Hello", "Hello World")
	
	if response == 1:
		Label(top, text="ask!!").pack()
	else:
		myResponse = "Cancel"
		Label(top, text=myResponse).pack()
	

B1 = Button(top, text = "Say Hello", command = hello).pack()
Label(top, text="Hello").pack()
top.mainloop()