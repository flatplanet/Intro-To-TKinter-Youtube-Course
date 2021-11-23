from tkinter import *
from mss import mss

root = Tk()
root.title('Codemy.com - Screen Shot')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x200")

def shot():
	with mss() as sct:
		# Designate the filename
		filename = sct.shot(mon=2, output="output.png")	

		# Confirm message
		my_label.config(text="Screen Shot Has Been Saved!")

my_button = Button(root, text="Take A Screenshot!", font=("Helvetica", 24), command=shot)
my_button.pack(pady=40)

my_label = Label(root, text="")
my_label.pack(pady=10)


root.mainloop()