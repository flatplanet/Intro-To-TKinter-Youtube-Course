from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Codemy.com - Resize The App With Sizegrip')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x300")
# Make the app resizable
root.resizable(True, True) # Width, Height

my_frame2 = Frame(root, highlightbackground="gray", highlightthickness=1)
my_frame2.pack(pady=20)

my_label = Label(my_frame2, text="Hello World!", 
	font=("Helvetica", 32))
my_label.pack(pady=50, padx=20)

# Create Sizegrip
my_sizegrip2 = ttk.Sizegrip(my_frame2)
my_sizegrip2.pack(side="right", anchor=SE)


# Reconfigure our rows and columns for grid
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

# Create a frame
my_frame = Frame(root, highlightbackground="gray", highlightthickness=1)
my_frame.pack(side="bottom", fill=X)

# Create Sizegrip
my_sizegrip = ttk.Sizegrip(my_frame)
my_sizegrip.pack(side="right", anchor=SE)

# Grid
#my_sizegrip.grid(row=1, sticky=SE)





root.mainloop()