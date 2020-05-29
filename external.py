from tkinter import *
import os
from tkinter import filedialog

root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x400")


def run_program():
        my_file = filedialog.askopenfilename()
        os.system('"%s"' % my_file)

my_button = Button(root, text="open program", command=run_program).pack(pady=20)


root.mainloop()



