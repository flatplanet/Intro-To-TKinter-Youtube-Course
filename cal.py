from tkinter import *
from tkcalendar import *
from date import datetime 

root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x400")

cal = Calendar(root, selectmode="day", year=2020, month=5, day=22)
cal.pack(pady=20)
#cal.pack(fill="both", expand=True)

def date():
	my_label.config(text=cal.get_date())

my_button = Button(root, text="get date", command=date)
my_button.pack(pady=10)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()

