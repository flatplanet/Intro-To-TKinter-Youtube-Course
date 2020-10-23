from tkinter import *

root = Tk()
root.title('Codemy.com - Tab Order')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x550")

# Create some entry boxes
red = Entry(root, bg="red", font=("Helvetica", 20))
white = Entry(root, bg="white", font=("Helvetica", 20))
blue = Entry(root, bg="blue", font=("Helvetica", 20))

# Pack them
red.pack(pady=20)
white.pack(pady=20)
blue.pack(pady=20)

# Pick focus
white.focus()

# Change Tab order
def tab_order():
	blue.focus()
	widgets = [blue, white, red]
	for w in widgets:
		w.lift()


my_button = Button(root, text="Change Tab Order", command=tab_order)
my_button.pack(pady=20)

tab_order()

root.mainloop()