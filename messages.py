from tkinter import *

root = Tk()
root.title('Codemy.com - Message Widget!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x900")

def change():
	my_message.config(text="And now for something completely different!",
		aspect=200)

# First one
frame1 = LabelFrame(root, text="Right Justified")
frame1.pack(pady=20)

my_message = Message(frame1, text="This is some long text that I am typing so that we can look at it, isn't it cool!?",
	font=("helvetica", 18),
	aspect=150,
	justify=RIGHT)
my_message.pack(pady=10, padx=10)

# Second One
frame2 = LabelFrame(root, text="Left Justified")
frame2.pack(pady=20)

my_message2 = Message(frame2, text="This is some long text that I am typing so that we can look at it, isn't it cool!?",
	font=("helvetica", 18),
	aspect=100,
	justify=LEFT)
my_message2.pack(pady=10, padx=10)

# Third One
frame3 = LabelFrame(root, text="Center Justified")
frame3.pack(pady=20)

my_message3 = Message(frame3, text="This is some long text that I am typing so that we can look at it, isn't it cool!?",
	font=("helvetica", 18),
	aspect=200,
	justify=CENTER)
my_message3.pack(pady=10, padx=10)

# Button
my_button = Button(root, text="Change Text", command=change)
my_button.pack(pady=20)

root.mainloop()