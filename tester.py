from tkinter import *

main = Tk()

main.title("PRESCRIPTIONS")

main.geometry('1300x500')

f1 = LabelFrame(main, bg="red", height = 500, width = 1300)
f1.pack(fill="both", expand=1)

 

label = Label(f1, text = "HELP",fg = "red", bg = "yellow", padx = 50)

label.pack()

main.mainloop()