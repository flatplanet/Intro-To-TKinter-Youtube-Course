from tkinter import *

root = Tk()
root.title('Codemy.com - Bind Text!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

def labeler(e):
	my_label.config(text=my_text.get(1.0, END + "-1c") + e.char)


my_text = Text(root, width=50, height=20, font=("Helvetica", 12))
my_text.pack(pady=20)

my_label = Label(root, text="Type stuff above", font=("Helvetica", 14))
my_label.pack(pady=20)

my_text.bind("<Key>", labeler)




root.mainloop()