from tkinter import *

root = Tk()
root.title('Codemy.com - Keys Method')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x550")

my_label = Label(root, text="My Label", font=("Helvetica", 18))
my_label.pack(pady=20)

my_entry = Entry(root)
my_entry.pack()

def something():
	pass
my_button = Button(root, text="Click Me!", command=something)
my_button.pack()

for key in my_label.keys():
	print(key)

print(my_label['font'])




root.mainloop()