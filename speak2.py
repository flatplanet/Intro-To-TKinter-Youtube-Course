from tkinter import *
import pyttsx3

root = Tk()
root.title("Codemy.com")
root.geometry("800x500")
root.iconbitmap('c:/gui/codemy.ico')


#pip install pyttsx3
#pip install pywin32


def speak():
	thing = my_entry.get()
	my_entry.delete(0,END)
	engine = pyttsx3.init()
	engine.say(thing)
	engine.runAndWait()



my_entry = Entry(root, font=("Helvetica",28))
my_entry.pack(pady=20)


my_button = Button(root, text="Speak", command=speak)
my_button.pack(pady=20)


root.mainloop()