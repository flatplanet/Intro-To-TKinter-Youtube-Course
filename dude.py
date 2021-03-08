from tkinter import *

root = Tk()
root.title('Codemy.com - Ring The Bell!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

frame1.pack(pady=10)
label1 = Label(frame1, text="Text 1")
label1.grid(row=0, column=0)
entry1 = Entry(frame1)
entry1.grid(row=0, column=1)

frame2.pack(pady=10)
label2 = Label(frame2, text="This is some text that goes in frame 2")
label2.grid(row=0, column=0)
entry2 = Entry(frame2)
entry2.grid(row=0, column=1)

frame3.pack(pady=10)
label3 = Label(frame3, text="Text 3")
label3.grid(row=0, column=0)
entry3 = Entry(frame3)
entry3.grid(row=0, column=1)

root.mainloop()