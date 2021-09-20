from tkinter import *
from tkinter import font

root = Tk()
root.title('Codemy.com - Font Dialog Box')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

# Create font chooser function
def font_chooser(e):
	our_font.config(
		family=my_listbox.get(my_listbox.curselection()))

# Designate Our Font
our_font = font.Font(family="Helvetica", size="32")

# Add Frame
my_frame = Frame(root, width=480, height=275)
my_frame.pack(pady=10)
# Freeze Frame in place
my_frame.grid_propagate(False)
my_frame.columnconfigure(0, weight=10)

# Add Text Box
my_text = Text(my_frame, font=our_font)
my_text.grid(row=0, column=0)
my_text.grid_rowconfigure(0, weight=1)
my_text.grid_columnconfigure(0, weight=1)

# Add Listbox
my_listbox = Listbox(root, selectmode=SINGLE, width=80)
my_listbox.pack()

# Add Font Families To Listbox
for f in font.families():
	my_listbox.insert('end', f)

# Bind The Listbox
my_listbox.bind('<ButtonRelease-1>', font_chooser)

root.mainloop()