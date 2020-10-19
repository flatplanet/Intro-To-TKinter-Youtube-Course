from tkinter import *

root = Tk()
root.title('Codemy.com - Alpha Method')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x550")

#root.attributes('-alpha', 0.5)
root.wm_attributes('-transparentcolor', root['bg'])

my_frame = Frame(root, width=200, height=200)
my_frame.pack(pady=20, ipady=20, ipadx=20)

my_label = Label(my_frame, text="Hello World!", fg="white", font=("Helvetica", 16))
my_label.pack(pady=20)


root.mainloop()