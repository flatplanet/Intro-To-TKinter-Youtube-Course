from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title("Math Flashcards")
root.geometry("400x400")
root.iconbitmap('c:/guis/codemy.ico')

# Define our fake command
def fake_command():
	pass

def add_answer(num_1, num_2, answer):
	correct = int(num_1) + int(num_2)
	my_answer = answer_entry.get()
	if int(my_answer) == correct:
		answer_label = Label(add_frame, text="Correct!" + " " + str(answer_entry.get()))
		answer_label.pack()
	else:
		answer_label = Label(add_frame, text="Incorrect!" + " " + str(answer_entry.get()))
		answer_label.pack()

def add():
	hide_menu_frames()
	current_status.set("Addition Flashcards")
	add_frame.pack(fill="both", expand=1)
	# Create random Numbers:
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	#Show Random Numbers, entry box, and answer button
	num_1_label = Label(add_frame, text=str(num_1) + " + " + str(num_2), font=("Helvetica", 32))
	num_1_label.pack(pady=10)


	global answer_entry
	answer_entry = Entry(add_frame)
	answer = IntVar()
	answer.set(answer_entry.get())
	answer_entry.pack(pady=20)

	answer_button = Button(add_frame, text="Answer", command=lambda: add_answer(num_1, num_2, answer))
	answer_button.pack()

def cut():
	hide_menu_frames()
	current_status.set("Cut Status")
	edit_frame.pack(height=400, widht=400, bg="blue")	

def hide_menu_frames():
	edit_frame.grid_forget()
	add_frame.grid_forget()

#Define a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Menu Items
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Mathcards", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=add)
math_menu.add_command(label="Multiply", command=add)
math_menu.add_command(label="Divide", command=add)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=root.quit)

# Create another submenu Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_command(label="Paste", command=fake_command)



# File Menu Frame
add_frame = Frame(root, width=400, height=400, bg="blue")
#file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

#file_frame_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
#file_frame_label.pack(padx=20, pady=20)


# Edit Menu Frame
edit_frame = Frame(root, width=400, height=400, bd=5, bg="blue", relief="sunken")
#file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

#edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
#edit_frame_label.pack(padx=20, pady=20)

current_status = StringVar()
current_status.set("Waiting")

my_status = Label(root, textvariable=current_status, bd=1, relief="sunken", width=56, anchor=E)
my_status.pack(side=BOTTOM, fill=X)


root.mainloop()