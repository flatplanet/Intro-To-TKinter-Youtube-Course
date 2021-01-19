from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime

root = Tk()
root.title('Codemy.com - Bitcoin Price Grabber')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("550x210")
root.config(bg="black")

global previous
previous = False

# Get Current Time
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")


# Create a Frame
my_frame = Frame(root, bg="black")
my_frame.pack(pady=20)

# Define logo image
logo = PhotoImage(file='images/bitcoin.png')
logo_label = Label(my_frame, image=logo, bd=0)
logo_label.grid(row=0, column=0, rowspan=2)

# Add bitcoin price label
bit_label = Label(my_frame, text='TEST', 
	font=("Helvetica", 45),
	bg="black",
	fg="green",
	bd=0)
bit_label.grid(row=0, column=1, padx=20, sticky="s")

# Latest Price Up/Down
latest_price = Label(my_frame, text="move test",
	font=("Helvetica", 8),
	bg="black",
	fg="grey")
latest_price.grid(row=1, column=1, sticky="n" )

#Grab the bitcoin price
def Update():
	global previous

	# Grab Bitcoin Price
	page = urllib.request.urlopen("https://www.coindesk.com/price/bitcoin").read()
	html = BeautifulSoup(page, "html.parser")
	price_large = html.find(class_="price-large")
	
	# convert to string so we can slice
	price_large1 = str(price_large)
	# Grab a slice that contains the price
	price_large2 = price_large1[54:63]

	# Update our bitcoin label
	bit_label.config(text=f'${price_large2}')
	# Set timer to 30 seconds
	# 1 second = 1000
	root.after(30000, Update)

	# Get Current Time
	now = datetime.now()
	current_time = now.strftime("%I:%M:%S %p")

	# Update the status bar
	status_bar.config(text=f'Last Updated: {current_time}   ')

	# Determine Price Change
	# grab current Price
	current = price_large2

	# remove the comma
	current = current.replace(',', '')

	if previous:
		if float(previous) > float(current):
			latest_price.config(
				text=f'Price Down {round(float(previous)-float(current), 2)}', fg="red")

		elif float(previous) == float(current):
			latest_price.config(text="Price Unchanged", fg="grey")	

		else:
			latest_price.config(
				text=f'Price Up {round(float(current)-float(previous), 2)}', fg="green")			


	else:
		previous = current
		latest_price.config(text="Price Unchanged", fg="grey")

# Create status bar
status_bar = Label(root, text=f'Last Updated {current_time}   ',
	bd=0,
	anchor=E,
	bg="black",
	fg="grey")

status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# On program start, run update function
Update()
root.mainloop()