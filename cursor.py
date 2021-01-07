from tkinter import *

root = Tk()
root.title("Cursors")
root.geometry("500x550")
root.iconbitmap('c:/guis/exe/codemy.ico')
root.config(cursor="fleur")

list = [
    "arrow",
    "circle",
    "clock",
    "cross",
    "dotbox",
    "exchange",
    "fleur",
    "heart",
    "man",
    "mouse",
    "pirate",
    "plus",
    "shuttle",
    "sizing",
    "spider",
    "spraycan",
    "star",
    "target",
    "tcross",
    "trek",
]

count = 0
row1=0
row2=0
row3=0
row4=0

for cursor in list:
	if count < 5:
		Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row1, column=0, pady=10, padx=10)
		row1 += 1
		count += 1

	elif count >= 5 and count < 10:
		Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row2, column=1, pady=10, padx=10)
		row2 += 1
		count += 1

	elif count >= 10 and count < 15:
		Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row3, column=2, pady=10, padx=10)
		row3 += 1
		count += 1

	else:
		Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row4, column=4, pady=5, padx=5)
		row4 += 1
		count += 1		

root.mainloop()