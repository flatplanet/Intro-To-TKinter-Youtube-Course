from tkinter import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=w, heigh=h, bg="white")
my_canvas.pack(pady=20)



# Add Image To Canvas
img = PhotoImage(file="c:/gui/images/me.png")
my_image = my_canvas.create_image(260,125, anchor=NW, image=img)


def left(event):
	x = -10
	y = 0
	my_canvas.move(my_image, x, y)

def right(event):
	x = 10
	y = 0
	my_canvas.move(my_image, x, y)


def up(event):
	x = 0
	y = -10
	my_canvas.move(my_image, x, y)


def down(event):
	x = 0
	y = 10
	my_canvas.move(my_image, x, y)



root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)




root.mainloop()

