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

def move(e):
	#e.x
	#e.y
	global img
	img = PhotoImage(file="c:/gui/images/me.png")
	my_image = my_canvas.create_image(e.x,e.y, image=img)
	my_label.config(text="Coordinates x: " + str(e.x) + " y: " + str(e.y))
	


#root.bind("<Left>", left)
#root.bind("<Right>", right)
#root.bind("<Up>", up)
#root.bind("<Down>", down)

my_label = Label(root, text="")
my_label.pack(pady=20)

my_canvas.bind('<B1-Motion>', move)



root.mainloop()

