from tkinter import *

root = Tk()
root.title('Codemy.com - Center A Thing With Place')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

button_1 = Button(root, text="Button 1", font=("Helvetica", 32))
button_2 = Button(root, text="Button 2", font=("Helvetica", 32))

button_1.grid(column=0, row=0)
button_2.grid(column=1, row=0)

my_button = Button(root, text="Click Me", font=("Helvetica, 32"))
my_button.place(relx=0.5, rely=0.5, anchor=CENTER)
#my_button.place(x=100, y=50)




root.mainloop()