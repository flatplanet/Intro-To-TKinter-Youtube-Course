import os, sys
import win32print
import win32api
import win32print
from tkinter import *

root = Tk()
root.title('Codemy.com - TextPad!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

#win32api.ShellExecute(0, "print", "sample.txt", None, ".", 0)


printer_name = win32print.GetDefaultPrinter()

my_label = Label(root, text=sys.version_info).pack()
if sys.version_info >= (3,):
	raw_data = bytes("This is a test", "utf-8")
else:
	raw_data = "This is a test"

hPrinter = win32print.OpenPrinter(printer_name)
try:
	hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
	try:
		#win32api.ShellExecute(0, "print", raw_data, None, ".", 0)
		win32print.StartPagePrinter (hPrinter)
		win32print.WritePrinter (hPrinter, raw_data)
		win32print.EndPagePrinter (hPrinter)
	finally:
		win32print.EndDocPrinter (hPrinter)
finally:
	win32print.ClosePrinter (hPrinter)


root.mainloop()