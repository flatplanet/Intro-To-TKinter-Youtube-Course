from tkinter import *

root = Tk()
root.title('Codemy.com - Auto Search')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x300")

my_label = Label(root, text="Start Typing...", font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)

def check(event): 
	
	value = e.get() 

	
	# get data from l 
	if value == '': 
		data = toppings 
	else: 
		data = [] 
		for item in toppings: 
			if value.lower() in item.lower(): 
				data.append(item)				 

	# update data in listbox 
	update(data) 


def update(data): 
	
	# clear previous data 
	lb.delete(0, 'end') 

	# put new data 
	for item in data: 
		lb.insert('end', item) 


# Driver code 
toppings = ("Pepperoni", "Peppers", "Mushrooms",
	"Cheese", "Onions", "Ham", "Taco") 

 

#creating text box 
e = Entry(root, font=("Helvetica", 20)) 
e.pack(pady=0) 
e.bind('<KeyRelease>', check) 

#creating list box 
lb = Listbox(root, width=50) 
lb.pack(pady=40) 
update(toppings) 

def fillout(event):
	e.delete(0, END)
	e.insert(0, lb.get(ACTIVE))

lb.bind("<<ListboxSelect>>", fillout)

root.mainloop()