from tkinter import *
from random import randint
from tkinter import ttk


root = Tk()
root.title('Codemy.com - Rock, Paper, Scissors')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x600")
# Change bg color to white
root.config(bg="white")

# Define our images
rock = PhotoImage(file='images/rps/rock.png')
paper = PhotoImage(file='images/rps/paper.png')
scissors = PhotoImage(file='images/rps/scissors.png')

# Add Images to a list
image_list = [rock, paper, scissors]

# Pick random number between 0 and 2
pick_number = randint(0,2)

# Throw up an image when the program starts
image_label = Label(root, image=image_list[pick_number], bd=0)
image_label.pack(pady=20)

# Create Spin Function
def spin():
	# Pick random numnber
	pick_number = randint(0,2)
	# Show image
	image_label.config(image=image_list[pick_number])

	# 0 = Rock
	# 1 = Paper
	# 2 = Scissors

	# Convert Dropdown choice to a number
	if user_choice.get() == "Rock":
		user_choice_value = 0
	elif user_choice.get() == "Paper":
		user_choice_value = 1
	elif user_choice.get() == "Scissors":
		user_choice_value = 2


	# Determine if we won or lost
	if user_choice_value == 0: # Rock
		if pick_number == 0:
			win_lose_label.config(text="It's A Tie! Spin Again...")
		elif pick_number == 1: # Paper
			win_lose_label.config(text="Paper Cover Rock! You Lose...")
		elif pick_number == 2: # Scissors
			win_lose_label.config(text="Rock Smashes Scissors!  You Win!!!")


	# If USer Picks Paper
	if user_choice_value == 1: # Paper
		if pick_number == 1:
			win_lose_label.config(text="It's A Tie! Spin Again...")
		elif pick_number == 0: # Rock
			win_lose_label.config(text="Paper Cover Rock! You Win!!!")
		elif pick_number == 2: # Scissors
			win_lose_label.config(text="Scissors Cuts Paper! You Lose...")

	# If User Pics Scissors
	if user_choice_value == 2: # Scissors
		if pick_number == 2:
			win_lose_label.config(text="It's A Tie! Spin Again...")
		elif pick_number == 0: # Rock
			win_lose_label.config(text="Rock Smashes Scissors! You Lose...")
		elif pick_number == 1: # Paper
			win_lose_label.config(text="Scissors Cuts Paper! You Win!!!")








# Make our choice
user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

# Create Spin Button
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)

# Label for showing if you won or not
win_lose_label = Label(root, text="", font=("Helvetica", 18), bg="white")
win_lose_label.pack(pady=50)

root.mainloop()