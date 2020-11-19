from tkinter import *

root = Tk()
root.title('Codemy.com - Expand Buttons To Fit App')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

# Config our column rows and cols
#Grid.rowconfigure(root, index=0, weight=1)
Grid.columnconfigure(root, index=0, weight=1)

# Config row 2
#Grid.rowconfigure(root, 1, weight=1)



# Create two buttons
button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")
button_3 = Button(root, text="Button 3")
button_4 = Button(root, text="Button 4")

# Grid them to the screen
button_1.grid(row=0, column=0, sticky="nsew")
button_2.grid(row=1, column=0, sticky="nsew")
button_3.grid(row=2, column=0, sticky="nsew")
button_4.grid(row=3, column=0, sticky="nsew")

# Create list of buttons
button_list = [button_1, button_2, button_3, button_4]

# Define row number
row_number = 0
weight_number = 1
#loop thru the list and config each row automatically
for button in button_list:
	Grid.rowconfigure(root, row_number, weight=weight_number)
	# Increment the counter
	row_number += 1
	weight_number += 1 


root.mainloop()