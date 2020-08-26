from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Codemy.com - Tic-Tac-Toe')
root.iconbitmap('c:/gui/codemy.ico')
#root.geometry("1200x710")

# X starts so true
clicked = True
count = 0




# disable all the buttons
def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

# Check to see if someone won
def checkifwon():
	global winner
	winner = False

	if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
		b1.config(bg="red")
		b2.config(bg="red")
		b3.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
		b4.config(bg="red")
		b5.config(bg="red")
		b6.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
		b7.config(bg="red")
		b8.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
		b1.config(bg="red")
		b4.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
		b2.config(bg="red")
		b5.config(bg="red")
		b8.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
		b3.config(bg="red")
		b6.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
		b1.config(bg="red")
		b5.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
		b3.config(bg="red")
		b5.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	#### CHECK FOR O's Win
	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
		b1.config(bg="red")
		b2.config(bg="red")
		b3.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
		b4.config(bg="red")
		b5.config(bg="red")
		b6.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
		b7.config(bg="red")
		b8.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
		b1.config(bg="red")
		b4.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
		b2.config(bg="red")
		b5.config(bg="red")
		b8.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
		b3.config(bg="red")
		b6.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
		b1.config(bg="red")
		b5.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
		b3.config(bg="red")
		b5.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	# Check if tie
	if count == 9 and winner == False:
		messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
		disable_all_buttons()
				
# Button clicked function
def b_click(b):
	global clicked, count

	if b["text"] == " " and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == " " and clicked == False:
		b["text"] = "O"
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )

# Start the game over!
def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global clicked, count
	clicked = True
	count = 0

	# Build our buttons
	b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
	b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
	b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

	b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
	b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
	b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

	b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
	b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
	b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

	# Grid our buttons to the screen
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

# Create menue
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)

reset()

root.mainloop()