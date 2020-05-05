from tkinter import *


root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")


loops=6
i=1
entries = []
while i < loops:
	en = Entry(root, width = 15)
	en.grid(row=5, padx=10, column=i+1, sticky = W)
	entries.append(en)
	i+=1

def clicker():
	#print(entries[0].get())
	my_label = ''
	for entry in entries:
		my_label = Label(root, text=str(my_label) + str(entry.get()) + '\n')
		my_label.grid(row=7, column=1)
		#print(entry.get())


my_button=Button(root, text="print", command=clicker).grid(row=6,column=1)


'''
entries = []

for i in range(10):
    en = Entry(root)
    en.grid(row=i+1, column=0)
    entries.append(en)

def hallo():
    for entry in entries:
        print(entry.get())

button=Button(root,text="krijg",command=hallo).grid(row=12,column=0)

root.mainloop()
'''

root.mainloop()

