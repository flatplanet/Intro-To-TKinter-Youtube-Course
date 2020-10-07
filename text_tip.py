from tkinter import *
from tkinter.tix import *

root = Tk()
root.title('Codemy.com - Text Tip')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x350")

# Create Tooltip
tip = Balloon(root)
tip.config(bd=10, bg="blue")

# Sub categories
tip.label.config(bg="red", fg="white", bd=20)
tip.message.config(bg="red", fg="white")

# Button
my_button = Button(root, text="Click Me!")
my_button.pack(pady=50)

# Label
my_label = Label(root, text="Some Text", font=("Helvetica", 20))
my_label.pack(pady=20)

# Bind tooltip to Button
tip.bind_widget(my_button, balloonmsg="This is my awesome tooltip!")

# Bind to the label
tip.bind_widget(my_label, balloonmsg="This is my awesome tooltip!")


root.mainloop()