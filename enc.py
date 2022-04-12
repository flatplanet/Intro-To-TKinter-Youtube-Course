from tkinter import *
import pybase64
from tkinter import messagebox

root = Tk()
root.title('Codemy.com - Encrypt/Decrpt Base64')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")

def clear():
	#Clear boxes
	my_text.delete(1.0, END)
	my_entry.delete(0, END)

def encrypt():
	# Get text from text box
	secret = my_text.get(1.0, END)
	# Clear the text box
	my_text.delete(1.0, END)

	# Logic for password
	if my_entry.get() == "elder":
		# Convert to byte
		secret = secret.encode("ascii")
		# Convert to base64
		secret = pybase64.b64encode(secret)
		# Convert it back to ascii
		secret = secret.decode("ascii")
		# Print to text box
		my_text.insert(END, secret)

	else:
		# Flash a message if wrong password
		messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!")

def decrypt():
	# Get text from text box
	secret = my_text.get(1.0, END)
	# Clear the screen
	my_text.delete(1.0, END)
	
	# Logic for password
	if my_entry.get() == "elder":
		# Convert to byte
		secret = secret.encode("ascii")
		# Convert to base64
		secret = pybase64.b64decode(secret)
		# Convert it back to ascii
		secret = secret.decode("ascii")
		# Print to text box
		my_text.insert(END, secret)

	else:
		# Flash a message if wrong password
		messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!")


my_frame = Frame(root)
my_frame.pack(pady=20)

enc_button = Button(my_frame, text="Encrypt", font=("Helvetica", 18), command=encrypt)
enc_button.grid(row=0, column=0)

dec_button = Button(my_frame, text="Decrypt", font=("Helvetica", 18), command=decrypt)
dec_button.grid(row=0, column=1, padx=20)

clear_button = Button(my_frame, text="Clear", font=("Helvetica", 18), command=clear)
clear_button.grid(row=0, column=2)

enc_label = Label(root, text="Encrypt/Decrypt Text...", font=("Helvetica", 14))
enc_label.pack()

my_text = Text(root, width=57, height=10)
my_text.pack(pady=10)


password_label = Label(root, text="Enter Your Password...", font=("Helvetica", 14))
password_label.pack()

my_entry = Entry(root, font=("Helvetica", 18), width=35, show="*")
my_entry.pack(pady=10)


root.mainloop()