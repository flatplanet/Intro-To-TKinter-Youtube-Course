from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageGrab
import PIL
from tkinter import colorchooser
import tkinter.ttk as ttk
#from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox

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



my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

brush_color = 'red'

def paint(e):
    
    #color_bg = 'white'
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
    # CAPSTYLE:, BUTT, ROUND, PROJECTING
    # Butt / slash
    # Round: circle round 
    # PROJECTING: Diamond
    #my_canvas.create_line(0,100, 300, 100, fill="color")
    #my_canvas.create_line(150,0, 150, 200, fill="color")
    my_canvas.create_line(x1, y1, x2, y2, width=penwidth, fill=brush_color, capstyle=brush_type.get(),smooth=True)
    old_x = e.x
    old_y = e.y

def reset(event):    #reseting or cleaning the canvas 
    old_x = None
    old_y = None  



def save_as_png():
    #thing = save_name.get()
    result = filedialog.asksaveasfilename(initialdir = "c:/gui/images/", filetypes = (("png files","*.png"),("all files","*.*")))
    result_label = Label(root, text=result)
    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'
    if result:
        x=root.winfo_rootx()+my_canvas.winfo_x()
        y=root.winfo_rooty()+my_canvas.winfo_y()
        x1=x+my_canvas.winfo_width()
        y1=y+my_canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)
        messagebox.showinfo("Image Saved", "Your Image Has Been Saved!")

    
    

'''
def save_as_png():
    # save postscipt image 
    my_canvas.postscript(file = 'fart' + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open('fart' + '.eps') 
    img.save('fart2' + '.png', 'png') 

'''
'''
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
'''

my_canvas.bind('<B1-Motion>',paint)#drwaing the line 
#root.bind('<ButtonRelease-1>',reset)


def clear():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")

def change_brush_color():
    global brush_color
    brush_color = "black"
    brush_color=colorchooser.askcolor(color=brush_color)[1]

def change_bg_color():
    global bg_color
    bg_color = "white"
    bg_color = colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg=bg_color)

def change_pen(thing):
    #'%0.2f' % float(my_slider.get())
    slider_label.config(text='%0.0f' % float(my_slider.get()))
    

# Brush Option Frame

brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)


# Brush Size
brush_frame = LabelFrame(brush_options_frame, text="Brush Size")
brush_frame.grid(row=0, column=0)
# Brush Slider
my_slider = ttk.Scale(brush_frame,from_= 1, to = 100,command=change_pen,orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)
slider_label = Label(brush_frame, text='%0.0f' % float(my_slider.get()))
slider_label.pack()

#Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type", height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round").pack(anchor=W)
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt").pack(anchor=W)
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting").pack(anchor=W)

# Colors
change_colors_frame = LabelFrame(brush_options_frame, text="Change Colors")
change_colors_frame.grid(row=0, column=2)

brush_color_button = Button(change_colors_frame, text="Brush Color", command=change_brush_color).pack(padx=10, pady=10)
bg_color_button = Button(change_colors_frame, text="Canvas Color", command=change_bg_color).pack(padx=10, pady=10)


# Program Options Frame
options_frame = LabelFrame(brush_options_frame, text="Program Options")
options_frame.grid(row=0, column=3, padx=50)

clear_button = Button(options_frame, text="Clear Screen", command=clear).pack(padx=10, pady=10)

my_button = Button(options_frame, text="Save To PNG", command=save_as_png).pack(padx=10, pady=10)


root.mainloop()

