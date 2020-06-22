from tkinter import *


root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')

width = root.winfo_screenwidth()
height = (root.winfo_screenheight() - 70)

root.geometry(f"{width}x{height}+0+0")

#root.geometry("600x400+-1900+100")



root.mainloop()