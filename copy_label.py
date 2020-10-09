from tkinter import *

root = Tk()
root.title('Codemy.com - Copy Label Text')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x350")

#Create Label
my_label = Label(root, text="Label 1", font=("Helvetica", 20))
my_label.pack(pady=20)

# create stringvar
#my_text = StringVar()
#my_text.set("This is Label 2")

# Create Entry Box
my_entry = Entry(root, 
	font=("Helvetica", 20),
	bd=0, 
	width=15)

# textvariable=my_text
# Insert into entry box
my_entry.insert(0, "This is cool label 2")
my_entry.config(state="readonly")

my_entry.pack(pady=20)


root.mainloop()