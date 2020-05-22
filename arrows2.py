from tkinter import *
import tkinter.ttk as ttk

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

#my_circle = my_canvas.create_oval(x, y, x+20, y+20 )

img = PhotoImage(file="images/me.png")
me = my_canvas.create_image(275,100, anchor=NW, image=img)

def left(event):
	x = -10
	y = 0
	my_canvas.move(me, x, y)

def right(event):
	x = 10
	y = 0
	my_canvas.move(me, x, y)


def up(event):
	x = 0
	y = -10
	my_canvas.move(me, x, y)


def down(event):
	x = 0
	y = 10
	my_canvas.move(me, x, y)

def pressing(event):
	x = 0
	y = 0
	if event.char == "a": x = -10
	if event.char == "d": x = 10
	if event.char == "r": y = -10
	if event.char == "x": y = 10
	my_canvas.move(my_circle, x, y)
	


root.bind("<Key>", pressing)


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)




root.mainloop()

