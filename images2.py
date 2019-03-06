from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')


my_img1 = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/aspen2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/me1.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/me2.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/me3.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)
#my_label2 = Label()

def forward(passed):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()

	my_label = Label(image=image_list[passed-1])
	button_forward = Button(root, text=">>", command=lambda: forward(passed+1))
	button_back = Button(root, text="<<", command=lambda: back(passed-1))

	if passed == 5:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

	

def back(passed):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[passed-1])
	button_forward = Button(root, text=">>", command=lambda: forward(passed+1))
	button_back = Button(root, text="<<", command=lambda: back(passed-1))

	if passed == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)


										 
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)






root.mainloop()