from tkinter import *
from PIL import Image



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


def paint(e):
    color_fg = 'red'
    color_bg = 'white'
    penwidth = 20
    old_x = e.x
    old_y = e.y
    #if old_x and old_y:
    my_canvas.create_line(old_x, old_y, e.x, e.y, width=penwidth, fill=color_fg, capstyle=ROUND,smooth=True)

    old_x = e.x
    old_y = e.y

def reset(event):    #reseting or cleaning the canvas 
    old_x = None
    old_y = None  

def save_as_png():
    # save postscipt image 
    my_canvas.postscript(file = 'test' + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open('test' + '.eps') 
    img.save('test' + '.png', 'png') 



my_canvas.bind('<B1-Motion>',paint)#drwaing the line 
#root.bind('<ButtonRelease-1>',reset)

my_button = Button(root, text="Save To PNG", command=save_as_png).pack(pady=20)

root.mainloop()

