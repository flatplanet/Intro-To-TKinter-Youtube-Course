from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)

# click command
def our_command():
	my_label = Label(root, text="You Clicked a Dropdown Menu!").pack()

# File New Function
def file_new():
	hide_all_frames()
	file_new_frame.pack(fill="both", expand=1)
	my_label = Label(file_new_frame, text="You Clicked the File >> New Menu!").pack()

# Edit Cut
def edit_cut():
	hide_all_frames()
	edit_cut_frame.pack(fill="both", expand=1)
	my_label = Label(edit_cut_frame, text="You Clicked the Edit >> Cut Menu!").pack()
	dummy_button = Button(edit_cut_frame, text="fake!").pack(pady=10)

	child_label = Label(edit_cut_frame, text=edit_cut_frame.winfo_children()[1])
	child_label.pack(pady=10)

	#print(edit_cut_frame.winfo_children())
	#[<tkinter.Label object .!frame2.!label>, <tkinter.Button object .!frame2.!button>, <tkinter.Label object .!frame2.!label2>]
# Hide all frames 
def hide_all_frames():
	# Loop thru all the children in each frame and delete them
	for widget in file_new_frame.winfo_children():
		widget.destroy()

	for widget in edit_cut_frame.winfo_children():
		widget.destroy()

	file_new_frame.pack_forget()
	edit_cut_frame.pack_forget()

#Create a menu item

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_command)

#Create an Options menu item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

# Create some frames
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")



root.mainloop()

