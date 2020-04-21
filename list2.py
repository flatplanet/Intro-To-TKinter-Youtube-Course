from tkinter import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

# SINGLE, BROWSE, MULTIPLE, EXTENDED
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

# Insert index and a string
# index 0 is first item but END works too

my_listbox.insert(END, "Hello there!")
my_listbox.insert(END, "Item two!!")

listy = ["one", "two", "three"]

for thing in listy:
	my_listbox.insert(END, thing)

# Delete all items
#my_listbox.delete(0, END)
my_listbox.delete(4, END)

def delete():
	my_listbox.delete(ANCHOR)
	label2.config(text="")

def select():
	label2.config(text=my_listbox.get(ANCHOR))

button = Button(root, text="Delete", command=delete)
button.pack()

button2 = Button(root, text="Select", command=select)
button2.pack()
global label2
label2 = Label(root, text='')
label2.pack(pady=15)

root.mainloop()

