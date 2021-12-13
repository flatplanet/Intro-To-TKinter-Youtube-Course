from tkinter import *
import platform

root = Tk()
root.title('Codemy.com - System Info!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x300")

info = f"System: {platform.system()}\n \
User Name: {platform.node()}\n \
Release: {platform.release()}\n \
Version: {platform.version()}\n \
Machine: {platform.machine()}\n \
Processor: {platform.processor()}\n \
Python Version: {platform.python_version()}\n \
"

my_label = Label(root, text=info, font=("Helvetica", 14))
my_label.pack(pady=20)


root.mainloop()