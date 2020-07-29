from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x600")

# Read only r  
# Read and Write r+  (beginning of file)
# Write Only w   (over-written)
# Write and Read w+  (over written)
# Append Only a  (end of file)
# Append and Read a+  (end of file)


def open_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	text_file = open(text_file, 'r')
	stuff = text_file.read()

	my_text.insert(END, stuff)
	text_file.close()


def save_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	text_file = open(text_file, 'w')
	text_file.write(my_text.get(1.0, END))

def add_image():
	# Add image
	global my_image
	my_image = PhotoImage(file="images/profile.png")
	position = my_text.index(INSERT)
	my_text.image_create(position, image=my_image)

	my_label.config(text=position)

my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)


open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=5)

my_label = Label(root, text="")
my_label.pack()

root.mainloop()