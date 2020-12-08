from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Codemy.com - Custom Fonts')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

# Define Our Font
bigFont = Font(
	family="Times",
	size=40,
	weight="bold",
	slant="roman",
	underline=0,
	overstrike=0)

# Define Out Font
mediumFont = Font(
	family="Helvetica",
	size=24,
	weight="normal",
	slant="italic",
	underline=1,
	overstrike=0)

# Define A Button
my_button1 = Button(root, text="Big Text", font=bigFont)
my_button1.pack(pady=20)


# Label
my_label = Label(root, text="more big text", font=mediumFont)
my_label.pack(pady=20)

root.mainloop()