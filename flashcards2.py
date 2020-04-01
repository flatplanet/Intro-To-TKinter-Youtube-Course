from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random 

root = Tk()
root.title('Flashcards!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x600")

# Create Radomizing state function
def random_state():
	#Create a list of state names
	global our_states
	our_states = ['california', 'florida', 'illinois', 'kentucky', 'nebraska', 'nevada', 'newyork', 'oregon', 'texas', "vermont"]
	global our_state_capitals
	our_state_capitals = {
	'california':"sacramento", 
	'florida':"tallahassee", 
	'illinois':"springfield", 
	'kentucky':"frankfort", 
	'nebraska':"lincoln", 
	'nevada':"carson city", 
	'newyork':"albany", 
	'oregon':"salem", 
	'texas':"austin", 
	'vermont':"montpelier"
	}
	#Generate a random number
	global rando
	rando = randint(0, len(our_states)-1)
	state = "states/" + our_states[rando] + ".png"
	
	#Create our State Images
	global state_image
	state_image = ImageTk.PhotoImage(Image.open(state))
	show_state.config(image=state_image, bg="white")
	
# Create answer function
def state_answer():
	answer = answer_input.get()
	answer = answer.replace(" ", "")

	# Determine if our answer is right or wrong!
	if answer.lower() == our_states[rando]:
		response = "Correct! " + our_states[rando].title()
	else:
		response = "Incorrect! " + our_states[rando].title() 

	answer_label.config(text=response)

	#Clear the entry box
	answer_input.delete(0, 'end')

	random_state()

# Create State Flashcard Function
def states():
	# Hide previous frames
	hide_all_frames()
	state_frame.pack(fill="both", expand=1)
	
	global show_state
	show_state = Label(state_frame)
	show_state.pack(pady=15)
	random_state()

	# Create anser input box
	global answer_input
	answer_input = Entry(state_frame, font=("Helvetica", 18), bd=2)
	answer_input.pack(pady=15)


	# Create Button To Randomize State Images
	rando_button = Button(state_frame, text="Pass", command=states)
	rando_button.pack(pady=10)

	# Create a Button To Answer the Question
	answer_button = Button(state_frame, text="Answer", command=state_answer)
	answer_button.pack(pady=5)	

	# Create a Label To tell us if we got the answer right or not
	global answer_label
	answer_label = Label(state_frame, text="", font=("Helvetica", 18), bg="white")
	answer_label.pack(pady=15)


# Create State Capital Flashcard Function
def state_capitals():
	# Hide previous frames
	hide_all_frames()
	state_capitals_frame.pack(fill="both", expand=1)
	#my_label = Label(state_capitals_frame, text="Capitals").pack()

	global show_state
	show_state = Label(state_capitals_frame)
	show_state.pack(pady=15)
	#random_state()

	global our_states
	our_states = ['california', 'florida', 'illinois', 'kentucky', 'nebraska', 'nevada', 'newyork', 'oregon', 'texas', "vermont"]
	global our_state_capitals
	our_state_capitals = {
	'california':"sacramento", 
	'florida':"tallahassee", 
	'illinois':"springfield", 
	'kentucky':"frankfort", 
	'nebraska':"lincoln", 
	'nevada':"carson city", 
	'newyork':"albany", 
	'oregon':"salem", 
	'texas':"austin", 
	'vermont':"montpelier"
	}

	answer_list = []
	count = 1
	while count < 4:
		rando = randint(0, len(our_states)-1)
		if count == 1:
			answer = our_states[rando]
			#Create our State Images
			global state_image
			state = "states/" + our_states[rando] + ".png"
			state_image = ImageTk.PhotoImage(Image.open(state))
			show_state.config(image=state_image, bg="white")
		
		# Add our first selection to a new list
		answer_list.append(our_states[rando])
		
		# Remove from old list
		our_states.remove(our_states[rando])

		#Shuffle original list
		random.shuffle(our_states)

		count += 1

	# Suffle our answer list so the answer isn't always the first one listed
	random.shuffle(answer_list)

	
	# Create answer radio buttons
	global capital_radio
	capital_radio = IntVar()
	#capital_radio.set("springfield")



	capital_radio_button1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(), variable=capital_radio, value=1).pack()
	capital_radio_button2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(), variable=capital_radio, value=2).pack()
	capital_radio_button3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(), variable=capital_radio, value=3).pack()
	


	# Create Button To Randomize State Images
	rando_button = Button(state_capitals_frame, text="Pass", command=state_capitals)
	rando_button.pack(pady=10)

	# Create a Button To Answer the Question
	answer_button = Button(state_capitals_frame, text="Answer", command=state_answer)
	answer_button.pack(pady=5)	

	# Create a Label To tell us if we got the answer right or not
	global answer_label_capitals
	answer_label_capitals = Label(state_capitals_frame, text="", font=("Helvetica", 18))
	answer_label_capitals.pack(pady=15)

# Hide all previous frames
def hide_all_frames():
	# Loop thru and destroy all children in previous frames
	for widget in state_frame.winfo_children():
		widget.destroy()
	
	for widget in state_capitals_frame.winfo_children():
		widget.destroy()



	state_frame.pack_forget()
	state_capitals_frame.pack_forget()


# Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Geography menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)



# Create our Frames
state_frame = Frame(root, width=500, height=500, bg="white")
state_capitals_frame = Frame(root, width=500, height=500)








root.mainloop()

