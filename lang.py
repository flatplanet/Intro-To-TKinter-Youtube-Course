from tkinter import *
from langdetect import detect
from langcodes import *

root = Tk()
root.title('Codemy.com - Language Detection!')

root.geometry("500x350")

def check_lang():
	if my_text.compare("end-1c", "==", "1.0"):
		my_label.config(text="Hey! You forgot to enter anything...")
	else:
		code = detect(my_text.get(1.0, END))
		my_result = Language.make(language=code).display_name()
		my_label.config(text=f"Your Language Is: {my_result}")


my_text = Text(root, height=10, width=50)
my_text.pack(pady=20)

my_button = Button(root, text="Check Language", command=check_lang)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=10)


root.mainloop()