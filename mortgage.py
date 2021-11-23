from tkinter import *

root = Tk()
root.title('Codemy.com - Mortgage Calculator')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")

def payment():
	if amount_entry.get() and interest_entry.get() and term_entry.get():
		# Convert Entry Boxes to numbers
		years = int(term_entry.get())
		months = years * 12
		rate = float(interest_entry.get())
		loan = int(amount_entry.get())
		# Calculate The Loan
		# Monthly Interest Rate
		monthly_rate = rate / 100 / 12 
		# Get Our Payment
		payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
		# Format Payment
		payment = f"{payment:,.2f}"

		# Output Payment to the screen
		payment_label.config(text=f"Monthly Payment: ${payment}")

	else:
		payment_label.config(text="Hey! You Forgot To Enter Something...")




my_label_frame = LabelFrame(root, text="Mortgage Calculator")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Define Labels and Entry Boxes
amount_label = Label(my_frame, text="Loan Amount")
amount_entry = Entry(my_frame, font=("Helvetica", 18))

interest_label = Label(my_frame, text="Interest Rate")
interest_entry = Entry(my_frame, font=("Helvetica", 18))

term_label = Label(my_frame, text="Term (years)")
term_entry = Entry(my_frame, font=("Helvetica", 18))

# Put Labels and Entry Boxes on the Screen
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=20)

term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

# Button
my_button = Button(my_label_frame, text="Calculate Payment", command=payment)
my_button.pack(pady=20)

# Output Label
payment_label = Label(root, text="", font=("Helvetica", 18))
payment_label.pack(pady=20)

root.mainloop()