from tkinter import *

splash_root = Tk()
splash_root.title("Splash Screen!!")
splash_root.geometry("300x200+-1500+250")
# Hide the title bar
splash_root.overrideredirect(True)

splash_label = Label(splash_root, text="Splash Screen!", font=("Helvetica", 18))
splash_label.pack(pady=20)


def main_window():
	# Kill the splash screen
	splash_root.destroy()
	# Throw up our main root window
	root = Tk()
	root.title('Codemy.com - Splash Screens')
	root.iconbitmap('c:/gui/codemy.ico')
	root.geometry("500x550+-1500+250")

	main_label = Label(root, text="Main Screen", font=("Helvetica", 18))
	main_label.pack(pady=20)	


# Splash Screen Timer
splash_root.after(5000, main_window)


mainloop()