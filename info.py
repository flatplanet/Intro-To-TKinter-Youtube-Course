from tkinter import *


root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("800x800+-1900+100")



def info():
	root.update_idletasks()

	print (root.winfo_width())
	print (root.winfo_height())
	print (root.winfo_geometry())
	print (root.winfo_id())
	print (root.winfo_x()) #upper left x coordinate
	print (root.winfo_y()) #upper left y coordinate
	
	#root.resizable(0, 0)
	h = 300
	w = 200
	#root.geometry('%ix%i' % (h,w)) 
	#root.geometry('{height}x{width}'.format(height=h, width=w)) 
	root.geometry(f'{h}x{w}') 
	#'%0.0f' % float(my_slider.get())

Button(root, text="click", command=info).pack()


root.mainloop()