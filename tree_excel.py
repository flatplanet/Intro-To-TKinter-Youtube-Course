from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog

root = Tk()
root.title('Codemy.com - Excel To Treeview')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("700x500")

# Create frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create treeview
my_tree = ttk.Treeview(my_frame)

# File open function
def file_open():
	filename = filedialog.askopenfilename(
		initialdir="C:/gui/",
		title = "Open A File",
		filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*"))
		)

	if filename:
		try:
			filename = r"{}".format(filename)
			df = pd.read_excel(filename)
		except ValueError:
			my_label.config(text="File Couldn't Be Opened...try again!")
		except FileNotFoundError:
			my_label.config(text="File Couldn't Be Found...try again!")
	# Clear old treeview
	clear_tree()

	# Set up new treeview
	my_tree["column"] = list(df.columns)
	my_tree["show"] = "headings"
	# Loop thru column list for headers
	for column in my_tree["column"]:
		my_tree.heading(column, text=column)

	# Put data in treeview
	df_rows = df.to_numpy().tolist()
	for row in df_rows:
		my_tree.insert("", "end", values=row)

	# Pack the treeview finally
	my_tree.pack()




def clear_tree():
	my_tree.delete(*my_tree.get_children())

# Add a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add menu dropdown
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()