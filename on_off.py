from tkinter import *

root = Tk()
root.title('Codemy.com - Flip The Switch!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

global is_on
is_on = True
# Define image
on = PhotoImage(file="images/on.png")
off = PhotoImage(file="images/off.png")

def switch():
	global is_on
	if is_on:
		on_button.config(image=off)
		is_on = False
		my_label.config(text="The Switch Is Off", fg="grey")
	else:
		on_button.config(image=on)
		is_on = True
		my_label.config(text="The Switch Is On", fg="green")


my_label = Label(root, text="The Switch Is On", font=("Helvetica", 32), fg="green")
my_label.pack(pady=20)

# Add image to label
on_button = Button(root, image=on, bd=0, command=switch)
on_button.pack(pady=50)




root.mainloop()