from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Codemy.com - Set Image as Background')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("800x500")

# Define image
bg = ImageTk.PhotoImage(file="images/mario.png")

# Create a canvas
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

# Add a label
my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50), fill="white")

# add some buttons
button1 = Button(root, text="Start")
button2 = Button(root, text="Reset Scores")
button3 = Button(root, text="Exit")

button1_window = my_canvas.create_window(10, 10, anchor="nw", window=button1)
button2_window = my_canvas.create_window(100, 10, anchor="nw", window=button2)
button3_window = my_canvas.create_window(230, 10, anchor="nw", window=button3)

def resizer(e):
	global bg1, resized_bg, new_bg
	# Open our image
	bg1 = Image.open("images/mario.png")
	# Resize the image
	resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
	# Define our image again
	new_bg = ImageTk.PhotoImage(resized_bg)
	# Add it back to the canvas
	my_canvas.create_image(0,0, image=new_bg, anchor="nw")
	# Readd the text
	my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50), fill="white")

'''
# Create a label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add something to the top of our image
my_text = Label(root, text="Welcome!", font=("Helvetica", 50), fg="white", bg="#2a1863")
my_text.pack(pady=50)

# create a frame
my_frame = Frame(root, bg='#6b88fe')
my_frame.pack(pady=20)

# Add some buttons
my_button1 = Button(my_frame, text="Exit")
my_button1.grid(row=0, column=0, padx=20)

my_button2 = Button(my_frame, text="Start")
my_button2.grid(row=0, column=1, padx=20)

my_button3 = Button(my_frame, text="Reset")
my_button3.grid(row=0, column=2, padx=20)
'''
root.bind('<Configure>', resizer)

root.mainloop()