from tkinter import *
import psycopg2
# postgresql-cubic-98264

root = Tk()
root.title('Codemy.com - Postgres Cloud App')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x550")

def clear():
	f_name.delete(0, END)
	_name.delete(0, END)

def query():
	# Configure and connect to Postgres
	conn = psycopg2.connect(
		host = "ec2-18-211-41-246.compute-1.amazonaws.com", 
		database = "dalilo11l7p24t",
		user = "ikyumnardmfjok",
		password = "52d3b09a2480693c2649d8c8a6b10514ec9798d08126844f16a06342480e215b", 
		port = "5432",
		)

	# Create a cursor
	c = conn.cursor()

	# Create a Table
	c.execute('''CREATE TABLE IF NOT EXISTS customers
		(first_name TEXT,
		last_name TEXT);
		''')

	conn.commit()
	conn.close()

def submit():
	# Configure and connect to Postgres
	conn = psycopg2.connect(
		host = "ec2-18-211-41-246.compute-1.amazonaws.com", 
		database = "dalilo11l7p24t",
		user = "ikyumnardmfjok",
		password = "52d3b09a2480693c2649d8c8a6b10514ec9798d08126844f16a06342480e215b", 
		port = "5432",
		)

	# Create a cursor
	c = conn.cursor()

	# Insert data into table
	thing1 = f_name.get()
	thing2 = l_name.get()
	c.execute('''INSERT INTO customers (first_name, last_name)
		VALUES (%s, %s)''', (thing1, thing2)
		)
	
	conn.commit()	
	conn.close()
		
	update()
	clear()


def update():
	# Configure and connect to Postgres
	conn = psycopg2.connect(
		host = "ec2-18-211-41-246.compute-1.amazonaws.com", 
		database = "dalilo11l7p24t",
		user = "ikyumnardmfjok",
		password = "52d3b09a2480693c2649d8c8a6b10514ec9798d08126844f16a06342480e215b", 
		port = "5432",
		)

	# Create a cursor
	c = conn.cursor()

	# Grab stuff from online database
	c.execute("SELECT * FROM customers")
	records = c.fetchall()

	output = ''

	# Loop thru the results
	for record in records:
		output_label.config(text=f'{output}\n{record[0]} {record[1]}')
		output = output_label['text']

	conn.close()

# Create The GUI For The App
my_frame = LabelFrame(root, text="Postgres Example")
my_frame.pack(pady=20)

f_label = Label(my_frame, text="First Name:")
f_label.grid(row=0, column=0, pady=10, padx=10)

f_name = Entry(my_frame, font=("Helvetica, 18"))
f_name.grid(row=0, column=1, pady=10, padx=10)

l_label = Label(my_frame, text="Last Name:")
l_label.grid(row=1, column=0, pady=10, padx=10)

l_name = Entry(my_frame, font=("Helvetica, 18"))
l_name.grid(row=1, column=1, pady=10, padx=10)

submit_button = Button(my_frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, pady=10, padx=10)

update_button = Button(my_frame, text="Update", command=update)
update_button.grid(row=2, column=1, pady=10, padx=10)

output_label = Label(root, text="")
output_label.pack(pady=50)



query()

root.mainloop()