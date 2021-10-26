from tkinter import *
import webbrowser

root = Tk()
root.title('Codemy.com - Open Web Browser')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

def open_browser(e):
	# Open default browser
	#webbrowser.open_new("https://codemy.com")
	
	# Open Specific Browser
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://codemy.com")


# Create Button
my_button = Button(root, text="Open Web Browser!", 
	font=("Helvetica", 24), command=lambda: open_browser(1))
my_button.pack(pady=50)

# Create Label
my_label = Label(root, text="Open Browser", font=("Helvetica", 24),
	fg="blue")
my_label.pack(pady=20)

# Bind Label
my_label.bind("<Button-1>", open_browser)




root.mainloop()