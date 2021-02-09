from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
root.title('Codemy.com - Using HTML')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x600")

my_label = HTMLLabel(root, html="\
	<code><h1>\
	<a href='https://codemy.com'>Learn To Code!</a>\
	</h1></code>\
	<ul>\
	<li>One</li>\
	<li>Two</li>\
	<li>Three</li>\
	</ul>\
	<img src='c:/gui/images/aspen.png'>")

my_label.pack(pady=20, 
	padx=20, 
	fill="both", 
	expand=True)


root.mainloop()

