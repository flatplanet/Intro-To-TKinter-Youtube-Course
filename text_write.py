from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x650")

# Read only r  
# Read and Write r+  (beginning of file)
# Write Only w   (over-written)
# Write and Read w+  (over written)
# Append Only a  (end of file)
# Append and Read a+  (end of file)


def open_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	name = text_file
	name = name.replace("C:/gui/", "")
	name = name.replace(".txt", "")
	
	text_file = open(text_file, 'r')
	stuff = text_file.read()

	my_text.insert(END, stuff)
	text_file.close()

	root.title(f'{name} - Textpad')


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

def select():
	selected = my_text.selection_get()
	my_label.config(text=selected)

def bolder():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	my_text.tag_configure("bold", font=bold_font)

	current_tags = my_text.tag_names("sel.first")

	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last" )
	else:
		my_text.tag_add("bold", "sel.first", "sel.last" )


def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	my_text.tag_configure("italic", font=italics_font)
	current_tags = my_text.tag_names("sel.first")

	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last" )
	else:
		my_text.tag_add("italic", "sel.first", "sel.last" )


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)


open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=5)

select_button = Button(root, text="Select Text", command=select)
select_button.pack(pady=5)

bold_button = Button(root, text="Bold", command=bolder)
bold_button.pack(pady=5)

italics_button = Button(root, text="Italics", command=italics_it)
italics_button.pack(pady=5)

my_label = Label(root, text="")
my_label.pack()

undo_button = Button(root, text="Undo", command=my_text.edit_undo)
undo_button.pack(pady=5)

redo_button = Button(root, text="Redo", command=my_text.edit_redo)
redo_button.pack(pady=5)


root.mainloop()