from tkinter import *

root = Tk()
root.title("Bitmaps")
root.geometry("300x900")
root.iconbitmap('c:/guis/exe/codemy.ico')

'''
error
gray75
gray50
gray12
hourglass
info
questhead
question
warning
'''
list = ["error",
"gray75",
"gray50",
"gray12",
"hourglass",
"info",
"questhead",
"question",
"warning"]

for map in list:
	Button(root, bitmap=map, width=50, height=50, fg="darkblue").pack(pady=20)



root.mainloop()