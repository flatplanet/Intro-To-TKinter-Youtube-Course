from tkinter import *

root = Tk()
root.title('Codemy.com - Resize Button Text')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")


Grid.columnconfigure(root, index=0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
button_1 = Button(root, text="Button 1!")
button_1.grid(row=0, column=0, sticky="nsew")

def resize(e):
	# Grab the app width and divide by 10
	size = e.width / 10
	# Change our button text size
	button_1.config(font=("Helvetica", int(size)))

	# Mess with height
	height_size = e.height / 10
	if e.height <= 300:
		button_1.config(font=("Helvetica", int(height_size)))		

	'''
	if e.height <= 300 and e.height > 200:
		button_1.config(font=("Helvetica", 30))
	elif e.height < 200 and e.height > 100:
		button_1.config(font=("Helvetica", 20))		 		
	elif e.height < 100:
		button_1.config(font=("Helvetica", 10))		 		
	'''

# Bind the app 
root.bind('<Configure>', resize)

root.mainloop()