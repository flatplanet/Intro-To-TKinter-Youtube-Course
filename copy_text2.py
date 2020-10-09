from tkinter import *

root = Tk()
root.title('Codemy.com - Copy Label Text')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x350")

my_frame = Frame(root)
my_frame.pack(pady=20)

my_label = Label(my_frame, text="This is Label 1", font=("Helvetica", 20))
my_label.grid(row=0, column=0, pady=20)


data_string = StringVar()
data_string.set("This is Label 2")
ent = Entry(my_frame, textvariable=data_string, bd=0,state="readonly", font=("Helvetica", 20))
ent.grid(row=1, column=0, pady=20)



my_entry = Entry(my_frame, font=("Helvetica", 20))
my_entry.grid(row=2, column=0, pady=20)
#my_entry.insert(0, "Stuff")







root.mainloop()