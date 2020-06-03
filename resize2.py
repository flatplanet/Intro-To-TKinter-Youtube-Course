from tkinter import *
from PIL import ImageTk, Image
# pip install Pillow

root = Tk()
root.title("Codemy.com")
root.geometry("800x500")
root.iconbitmap('c:/gui/codemy.ico')

#500x375; 300 225

my_pic = Image.open('images/aspen.png')
resized = my_pic.resize((300, 225), Image.ANTIALIAS)
thing = ImageTk.PhotoImage(resized)
my_label = Label(root, image=thing)
my_label.pack(pady=20)



root.mainloop()