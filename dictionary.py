from tkinter import *
from PyDictionary import PyDictionary


root = Tk()
root.title('Codemy.com - Dictionary')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("570x500")

def lookup():
	# Clear The text
	my_text.delete(1.0, END)

	# Lookup a word
	dictionary = PyDictionary()
	definition = dictionary.meaning(my_entry.get())

	# Add definition to text box
	#my_text.insert(END, defintion)

	# Find keys and values in definition
	for key,value in definition.items():
		# put the key header in textbox
		my_text.insert(END, key + '\n\n')

		for values in value:
			my_text.insert(END, f'- {values}\n\n')




my_labelframe = LabelFrame(root, text="Enter A Word")
my_labelframe.pack(pady=20)

my_entry = Entry(my_labelframe, font=("Helvetica", 28))
my_entry.grid(row=0, column=0, padx=10, pady=10)

my_button = Button(my_labelframe, text="Lookup", command=lookup)
my_button.grid(row=0, column=1, padx=10)

my_text = Text(root, height=20, width=65, wrap=WORD)
my_text.pack(pady=10)


root.mainloop()