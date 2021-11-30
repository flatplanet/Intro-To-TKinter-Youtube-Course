from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')




button_quit = Button(root, text="Exit", command=root.quit)

img = ImageTk.PhotoImage(Image.open("aspen.png"))  
label = Label(image=img)
label.pack()


button_quit.pack()
t = Text(root, height=5, width=30)
t.insert(END, "What the Funk!\nChuck!")
#t.pack()


root.mainloop()