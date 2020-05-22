from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import colorchooser
import tkinter.ttk as ttk
#from tkinter.ttk import *


root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("800x800")

w = 600
h = 400
x = w/2
y = h/2

white = (255, 255, 255)
image1 = PIL.Image.new('RGB', (w, h), white)
draw = ImageDraw.Draw(image1)

my_canvas = Canvas(root, width=w, heigh=h, bg="white")
my_canvas.pack(pady=20)

brush_color = 'red'

def paint(e):
    
    color_bg = 'white'
    #penwidth = 20
    penwidth = '%0.0f' % float(my_slider.get())
    #old_x = e.x
    #old_y = e.y
    x1 = e.x -1
    y1 = e.y -1
    x2 = e.x + 1
    y2 = e.y +1
    #if old_x and old_y:
    #my_canvas.create_line(old_x, old_y, e.x, e.y, width=penwidth, fill=color_fg, capstyle=ROUND,smooth=True)
    # CAPSTYLE, BUTT, ROUND, PROJECTING
    my_canvas.create_line(x1, y1, x2, y2, width=penwidth, fill=brush_color, capstyle=PROJECTING,smooth=True)
    old_x = e.x
    old_y = e.y

def reset(event):    #reseting or cleaning the canvas 
    old_x = None
    old_y = None  

def save_as_png():
    # save postscipt image 
    #my_canvas.postscript(file = 'test' + '.eps') 
    # use PIL to convert to PNG 
    #img = Image.open('test' + '.eps') 
    #img.save('test' + '.png', 'png') 
    w = 600
    h = 400
    
    filename = "image.png"
    image1.save(filename)


my_canvas.bind('<B1-Motion>',paint)#drwaing the line 
#root.bind('<ButtonRelease-1>',reset)


def clear():
    my_canvas.delete(ALL)

def change_brush_color():
    global brush_color
    brush_color = "black"
    brush_color=colorchooser.askcolor(color=brush_color)[1]

def change_pen(thing):
    #'%0.2f' % float(my_slider.get())
    slider_label.config(text='%0.0f' % float(my_slider.get()))
    

my_slider = ttk.Scale(root,from_= 1, to = 100,command=change_pen,orient=VERTICAL, value=10)
my_slider.pack(pady=10)
slider_label = Label(root, text='%0.0f' % float(my_slider.get()))
slider_label.pack()


my_button = Button(root, text="Save To PNG", command=save_as_png).pack(pady=20)
clear_button = Button(root, text="Clear Screen", command=clear).pack()
clear_button = Button(root, text="Brush Color", command=change_brush_color).pack()

root.mainloop()

