from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Flashcards!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

my_menu = Menu(root)
root.config(menu=my_menu)

# click command
def our_command():
	my_label = Label(root, text="You Clicked a Dropdown Menu!").pack()
def check():
	if answer.get() == "Texas":
		answer_label = Label(file_new_frame, text="Correct! That State Was Texas!", bg="white").pack()
	else: 	
		answer_label = Label(file_new_frame, text="Incorrect! That State Was Texas!").pack()

	#show_texas.pack_forget()
	answer.delete(0, 'end')
	global nebraska_img
	nebraska_img = ImageTk.PhotoImage(Image.open("states/nebraska.png"))
	show_texas.config(image=nebraska_img)
	#show_texas = Label(file_new_frame, image=texas_img)


# File New Function
def states():
	hide_all_frames()
	file_new_frame.pack(fill="both", expand=1)
	global texas_img
	global show_texas

	texas_img = ImageTk.PhotoImage(Image.open("states/texas.png"))
	show_texas = Label(file_new_frame, image=texas_img, bg="white")
	show_texas.pack(pady=15)

	global answer
	answer = Entry(file_new_frame, font=("helvetica", 18), bd=2)
	answer.pack(pady=10)

	answer_button = Button(file_new_frame, text="Submit Answer", command=check)
	answer_button.pack(pady=5)
	

# Edit Cut
def edit_cut():
	hide_all_frames()
	edit_cut_frame.pack(fill="both", expand=1)
	my_label = Label(edit_cut_frame, text="You Clicked the Edit >> Cut Menu!").pack()	

# Hide all frames 
def hide_all_frames():
	file_new_frame.pack_forget()
	edit_cut_frame.pack_forget()

#Create a menu item

geography_menu = Menu(my_menu)
my_menu.add_cascade(label="States", menu=geography_menu)
geography_menu.add_command(label="States", command=states)
geography_menu.add_separator()
geography_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Math", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_command)

#Create an Options menu item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

# Create some frames
file_new_frame = Frame(root, width=500, height=500, bg="white")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")



root.mainloop()

