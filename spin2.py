from tkinter import *

root = Tk()
root.title('Codemy.com MP3 Player')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")

def clear():
	my_spin.selection_clear()
	my_spin.insert(END, "Bob")
	my_label.config(text=my_spin.selection_element())

#my_spin = Spinbox(root, values=("Tim", "John"), font=('Helvetica', 20))
my_spin = Spinbox(root, from_=0, to=10, font=('Helvetica', 20))
my_spin.pack(pady=20)

my_button = Button(root, text='Submit', command=clear)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)



root.mainloop()