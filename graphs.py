from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt



root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x200")


def grapher():
	incomes = np.random.normal(27000,15000,10000) #create a random normal distribution, around a point of 27,000 with a stdev of 15,000 and with 10,000 data points
	np.mean(incomes)
	plt.hist(incomes,50) # 50 buckets

	canvas = plt.show()
	canvas.show()
	canvas.get_tk_widget().pack()

	#plt.show()

graph_button = Button(root, text="Graph It!", command=grapher)
graph_button.pack()

incomes = np.random.normal(27000,15000,20) #create a random normal distribution, around a point of 27,000 with a stdev of 15,000 and with 10,000 data points
plt.specgram(incomes)
plt.show()

#plt.box() # 50 buckets

#plt.show()

root.mainloop()