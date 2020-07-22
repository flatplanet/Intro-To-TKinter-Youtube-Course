from tkinter import *
import time
from random import randint
import threading

root = Tk()

root.title("Learn To Code at Codemy.com")
root.geometry("500x400")

def five_seconds():
	time.sleep(5)
	my_label.config(text="5 Seconds Is Up!")

def rando():
	random_label.config(text=f'Random Number: {randint(1,100)}')

my_label = Label(root, text="Hello There!")
my_label.pack(pady=20)

my_button1 = Button(root, text="5 Seconds", command=threading.Thread(target=five_seconds).start())
my_button1.pack(pady=20)

my_button2 = Button(root, text="Pick Random Number", command=rando)
my_button2.pack(pady=20)

random_label = Label(root, text='')
random_label.pack(pady=20)

threading.Thread(target=five_seconds).start()


root.mainloop()