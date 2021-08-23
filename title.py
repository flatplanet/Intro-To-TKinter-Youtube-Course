from tkinter import *

root = Tk()
root.title('Codemy.com - Change Titlebar Color')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

# remove title bar
root.overrideredirect(True)

def move_app(e):
	root.geometry(f'+{e.x_root}+{e.y_root}')

def quitter(e):
	root.quit()
	#root.destroy()

# Create Fake Title Bar
title_bar = Frame(root, bg="darkgreen", relief="raised", bd=0)
title_bar.pack(expand=1, fill=X)
# Bind the titlebar
title_bar.bind("<B1-Motion>", move_app)


# Create title text
title_label = Label(title_bar, text="  My Awesome App!!", bg="darkgreen", fg="white")
title_label.pack(side=LEFT, pady=4)

# Create close button on titlebar
close_label = Label(title_bar, text="  X  ", bg="darkgreen", fg="white", relief="sunken", bd=0)
close_label.pack(side=RIGHT, pady=4)
close_label.bind("<Button-1>", quitter)

my_button = Button(root, text="CLOSE!", font=("Helvetica, 32"), command=root.quit)
my_button.pack(pady=100)



root.mainloop()