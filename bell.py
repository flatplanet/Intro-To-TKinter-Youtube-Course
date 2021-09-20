from tkinter import *

root = Tk()
root.title('Codemy.com - Ring The Bell!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")
thing = 500
print(f"{thing:04d}")

# Define image
bell = PhotoImage(file="images/bell.png")

# Add image to label
bell_label = Label(root, image=bell)
bell_label.pack(pady=20)

# create ring function
def ring():
	root.bell()

# Create our button
my_button = Button(root,
	text="Ring The Bell",
	command=ring,
	font=("Helvetica", 24), 
	fg="#4d4d4d")

my_button.pack(pady=20)



root.mainloop()