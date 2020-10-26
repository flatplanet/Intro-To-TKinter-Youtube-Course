from tkinter import *
#import time

splash_root = Tk()
splash_root.title('SPLASH SCREEN!')
splash_root.geometry("300x200+-1500+250")
splash_root.overrideredirect(True)

def main_root():
	root = Tk()
	root.title('Codemy.com - Main App')
	root.iconbitmap('c:/gui/codemy.ico')
	root.geometry("500x550+-1500+250")

	main_label = Label(root, text="Main App!")
	main_label.pack(pady=20)



def call_mainroot():
	splash_root.destroy()
	main_root()

my_label = Label(splash_root, text="Splash Screen!")
my_label.pack(pady=20)



splash_root.after(5000,call_mainroot)

mainloop()