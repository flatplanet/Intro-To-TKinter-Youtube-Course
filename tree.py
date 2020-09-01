from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Codemy.com - TreeView')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

my_tree = ttk.Treeview(root)

# Define Our Columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favorite Pizza", anchor=W, width=120)

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
	["Bob", 5, "Onion"]
]

count=0
for record in data:
	my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]))
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

# Pack to the screen
my_tree.pack(pady=20)


root.mainloop()