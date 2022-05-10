from tkinter import *
from PyDictionary import PyDictionary
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Codemy.com - Dictionary')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("620x470")

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




my_labelframe = customtkinter.CTkFrame(root, corner_radius=10)
my_labelframe.pack(pady=20)

my_entry = customtkinter.CTkEntry(my_labelframe, width=400, height=40, border_width=1, placeholder_text="Enter A Word", text_color="silver")
my_entry.grid(row=0, column=0, padx=10, pady=10)

my_button = customtkinter.CTkButton(my_labelframe, text="Lookup", command=lookup)
my_button.grid(row=0, column=1, padx=10)

text_frame = customtkinter.CTkFrame(root, corner_radius=10)
text_frame.pack(pady=10)

my_text = Text(text_frame, height=20, width=67, wrap=WORD, bd=0, bg="#292929", fg="silver")
my_text.pack(pady=10, padx=10)


root.mainloop()