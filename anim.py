from tkinter import *

root = Tk()
root.title('Codemy.com - Simple Button Animation')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x300")

#define some variables
count = 0
size = 26
pos = 100

# Contract the button
def contract():
	global count, size, pos
	if count <= 10 and count > 0:
		size -= 2
		# Configure button font size
		my_button.config(font=("Helvetica", size))
		# Change button position
		my_button.pack_configure(pady=pos)
		# decrease the count by 1
		count -= 1
		pos -= 20
		# Set a timer
		root.after(100, contract)

# Expand the button
def expand():
	global count, size, pos
	if count < 10:
		size += 2 
		# Configure button font size
		my_button.config(font=("Helvetica", size))
		# Change button position
		my_button.pack_configure(pady=pos)
		# Increase the count by 1 
		count += 1
		pos += 20
		# Set the timer
		root.after(100, expand)

	elif count == 10:
		contract()


# Create a button
my_button = Button(root, 
	text="Click Me!", 
	command=expand,
	font=("Helvetica", 24),
	fg="red")
my_button.pack(pady=100)


root.mainloop()