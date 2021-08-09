from tkinter import *

root = Tk()
root.geometry("1000x667")
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')

global our_images, count
count = -1

our_images = [
	PhotoImage(file = "images/bg/1.png"),
	PhotoImage(file = "images/bg/2.png"),
	PhotoImage(file = "images/bg/3.png"),
]

# Create a Canvas
my_canvas = Canvas(root, width=1000, height=667, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Set the canvas image
my_canvas.create_image(0,0, image=our_images[0], anchor='nw')

def next():
	global count
	if count == 2:
		my_canvas.create_image(0,0, image=our_images[0], anchor='nw')		
		count = 0
	else:
		my_canvas.create_image(0,0, image=our_images[count+1], anchor='nw')	
		count += 1

	root.after(1000, next)

next()
mainloop()