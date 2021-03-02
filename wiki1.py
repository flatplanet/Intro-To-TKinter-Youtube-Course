from tkinter import *
import wikipedia as wiki

root = Tk()
root.title('Codemy.com - Wikipedia')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("700x675")

# Clear
def clear():
	my_entry.delete(0, END)
	my_text.delete(0.0, END)

# Search
def search():
	data = wiki.page(my_entry.get())
	# Clear screen
	clear()
	# Output Wikipedia Results To Textbox
	my_text.insert(0.0, data.content)

my_label_frame = LabelFrame(root, text="Search Wikipedia")
my_label_frame.pack(pady=20)

# Create entry box
my_entry = Entry(my_label_frame, font=("Helvetica", 18), width=47)
my_entry.pack(pady=20, padx=20)

# create text box frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Vertical Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Horizontal Scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create Text Box
my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure Scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Button Frame
button_frame = Frame(root)
button_frame.pack(pady=10)

# Buttons
search_button = Button(button_frame, text="Lookup", font=("Helvetica", 32), fg="#3a3a3a", command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = Button(button_frame, text="Clear", font=("Helvetica", 32), fg="#3a3a3a", command=clear)
clear_button.grid(row=0, column=1)


root.mainloop()