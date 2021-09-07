from tkinter import *
import random 



root = Tk()
root.title('Codemy.com - Software Registration Key Generator')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

name = "-"
print(ord(name))

def verify(key):
	global score
	score = 0
	# Grab the first digit in the key
	check_digit = key[2]
	check_digit_count = 0
	# Separate by hyphen
	chunks = key.split('-')

	#loop thru and check
	for chunk in chunks:
		if len(chunk) != 4:
			return False
			#verify_label.config(text="Not enough chunks")
		for char in chunk:
			if char == check_digit:
				check_digit_count += 1
			# Grab numerical representation of ASCII Character
			score += ord(char)
			#1772
			#verify_label.config(text=score)
	if score > 1700 and score < 1800 and check_digit_count == 3:
		return True
	#if check_digit_count == 3:
	#	return True

	else:
		return False




def generate():
	# Clear any previous key
	key_label.delete(0, END)
	verify_label.config(text="")

	# Set out defaults
	key = ''
	blob = ''
	check_digit_count = 0
	alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'


	#while True:
	while len(key) < 25:
		char = random.choice(alphabet)
		key += char
		blob += char
		if len(blob) == 4:
			# Add in a dash to our key
			key += '-'
			# Reset Chunk to blank
			blob = ""

	# set key to all but last digit
	key = key[:-1]
	

	# Next Verify The Key
	#key_label.insert(0, key)
	if verify(key):
		key_label.insert(0, key)
		verify_label.config(text="Valid!")
		score_label.config(text=f'Score: {score}')
	else:
		key_label.insert(0, key)
		verify_label.config(text="Invalid!")
		generate()

#verify_label.config(text="Valid!")

generate_button = Button(root, text="Generate Key", command=generate, font=("Helvetica", 32))
generate_button.pack(pady=50)

key_label = Entry(root, font=("Helvetica", 24), bd=0, bg="systembuttonface", width=25)
key_label.pack(pady=10, padx=50)

verify_label = Label(root, text='', font=("Helvetica", 32))
verify_label.pack(pady=10)

score_label = Label(root, text='', font=("Helvetica", 32))
score_label.pack(pady=10)


root.mainloop()