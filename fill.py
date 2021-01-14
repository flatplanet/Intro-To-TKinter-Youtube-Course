from tkinter import *

root = Tk()
root.title('Codemy.com - Auto Select/Search')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

# Update the list box
def update(data):
	# Clear the listbox
	my_list.delete(0, END)

	# Add data to the listbox
	for item in data:
		my_list.insert(END, item)


# Create Function to check typed things
def check(e):
	# Grab whatever was typed in the entry box
	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings: 
			if typed.lower() in item.lower():
				data.append(item)

	# Pass updated listbox data to update function
	update(data)



# Add Listbox Clicked to Entry Box
def fillout(e):
	# Delete whatever is in the entry box already
	my_entry.delete(0, END)

	# Add clicked to entry box
	my_entry.insert(0, my_list.get(ACTIVE))


# Make a label
my_label = Label(root, text="Start Typing...",
	font=("Helvetica", 14),
	fg="grey")

my_label.pack(pady=20)

# Make our entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Make a Listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Bind the listbox to add clicked to entry box
my_list.bind("<<ListboxSelect>>", fillout)


# Create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushroom",
	"Cheese", "Onion", "Ham", "Taco"]

# Add our toppings to the list box
update(toppings)

# Create an event binding on our entry box
my_entry.bind('<KeyRelease>', check)	



root.mainloop()