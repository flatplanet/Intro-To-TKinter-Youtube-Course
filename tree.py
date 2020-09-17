from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Codemy.com - TreeView')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x800")

# Add some style
style = ttk.Style()
#Pick a theme
style.theme_use("default")
# Configure our treeview colors

style.configure("Treeview", 
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3"
	)
# Change selected color
style.map('Treeview', 
	background=[('selected', 'blue')])

# Create Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# Pack to the screen
my_tree.pack()

#Configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favorite Pizza", anchor=W, width=140)

# Create Headings 
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Add Data
data = [
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["Ruth", 9, "Vegan"]
]

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count=0

for record in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))

	count += 1


'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("John", 1, "Peperroni"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", "2", "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Tina", "3", "Ham"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Bob", "4", "Supreme"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Erin", "5", "Cheese"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Wes", "6", "Onion"))
'''
# add child
#my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
#my_tree.move('6', '0', '0')



add_frame = Frame(root)
add_frame.pack(pady=20)

#Labels
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

#Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

# Add Record
def add_record():
	my_tree.tag_configure('oddrow', background="white")
	my_tree.tag_configure('evenrow', background="lightblue")

	global count
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('oddrow',))

	count += 1

	# Clear the boxes
	name_box.delete(0, END)
	id_box.delete(0, END)
	topping_box.delete(0, END)

# Remove all records
def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

# Remove one selected
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

# Remove many selected
def remove_many():
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)

# Select Record
def select_record():
	# Clear entry boxes
	name_box.delete(0, END)
	id_box.delete(0, END)
	topping_box.delete(0, END)

	# Grab record number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	#temp_label.config(text=values[0])

	# output to entry boxes
	name_box.insert(0, values[0])
	id_box.insert(0, values[1])
	topping_box.insert(0, values[2])


# Save updated record
def update_record():
	# Grab record number
	selected = my_tree.focus()
	# Save new data
	my_tree.item(selected, text="", values=(name_box.get(), id_box.get(), topping_box.get()))

	# Clear entry boxes
	name_box.delete(0, END)
	id_box.delete(0, END)
	topping_box.delete(0, END)

# Create Binding Click function
def clicker(e):
	select_record()

# Move Row up
def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Row Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)



#Buttons
move_up = Button(root, text="Move Up", command=up)
move_up.pack(pady=20)

move_down = Button(root, text="Move Down", command=down)
move_down.pack(pady=10)

select_button = Button(root, text="Select Record", command=select_record)
select_button.pack(pady=10)

update_button = Button(root, text="Save Record", command=update_record)
update_button.pack(pady=10)
add_record = Button(root, text="Add Record", command=add_record)
add_record.pack(pady=10)

# Remove all
remove_all = Button(root, text="Remove All Records", command=remove_all)
remove_all.pack(pady=10)

# Remove One
remove_one = Button(root, text="Remove One Selected", command=remove_one)
remove_one.pack(pady=10)

# Remove Many Selected
remove_many = Button(root, text="Remove Many Selected", command=remove_many)
remove_many.pack(pady=10)

temp_label = Label(root, text="")
temp_label.pack(pady=20)

# Bindings
#my_tree.bind("<Double-1>", clicker)
my_tree.bind("<ButtonRelease-1>", clicker)


root.mainloop()