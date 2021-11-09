from tkinter import *

root = Tk()
root.title('Codemy.com - Multiple Text Scrolls')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x500")

# Yview Function
def multiple_yview(*args):
	my_text1.yview(*args)
	my_text2.yview(*args)
	#print(*args)

# Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Two Text Boxes
my_text1 = Text(my_frame, width=20, height=25, font=("Helvetica", 16), yscrollcommand=text_scroll.set, wrap="none")
my_text1.pack(side=RIGHT, padx=5)
my_text2 = Text(my_frame, width=20, height=25, font=("Helvetica", 16), yscrollcommand=text_scroll.set, wrap="none")
my_text2.pack(side=LEFT)

# Configure Scrollbar
text_scroll.config(command=multiple_yview)


root.mainloop()