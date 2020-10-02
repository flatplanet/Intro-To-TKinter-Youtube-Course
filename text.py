from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x450")

# Create Clear Function
def clear():
	my_text.delete(1.5, END)

# Grab the text from the text box
def get_text():
	my_label.config(text=my_text.get(1.0, 3.0))

my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="Get Text", command=get_text)
get_text_button.grid(row=0, column=1, padx=20)

my_label = Label(root, text='')
my_label.pack(pady=20)



root.mainloop()