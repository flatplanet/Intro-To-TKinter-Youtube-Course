from tkinter import *

root = Tk()
root.title("Calculator")

#font size
large_font = ('Verdana',17)
small_font = ('Verdana',12)

#functions for buttons
def num_click(number):
    current= ent.get()
    ent.delete(0,END)
    ent.insert(0, str(current) + str(number))

def add_click():
    global num1   #num1 is set to global so it can be used outside function
    num1= ent.get() #num1 gets the number in the entry field before the add button is clicked
    global fun #fun can be used globally
    fun="add" #function of add
    ent.delete(0, END)

def sub_click():
    global num1
    num1 = ent.get()
    global fun
    fun="sub"
    ent.delete(0, END)

def mul_click():
    global num1
    num1 = ent.get()
    global fun
    fun="mul"
    ent.delete(0, END)

def div_click():
    global num1
    num1 = ent.get()
    global fun
    fun="div"
    ent.delete(0, END)

def equal_click():
    num2= ent.get() #gets the number in the entry tab present before clicking equal
    ent.delete(0, END) #delete whats on the screen when equal pressed
    if fun=="add":
        ent.insert(0,eval(num1) + eval(num2))
    elif fun == "sub":
        ent.insert(0, eval(num1) - eval(num2))
    elif fun == "mul":
        ent.insert(0, eval(num1) * eval(num2))
    elif fun == "div":
        ent.insert(0, eval(num1) / eval(num2))

def clear_click():
    ent.delete(0, END) #deletes everything in the entry field



# entry field row 0
ent = Entry(root, width=20,borderwidth=5,font=large_font)
ent.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# buttons
#row 1
but_7 = Button(root, text="7", padx=30, pady=30,font=small_font, command=lambda: num_click(7))
but_8 = Button(root, text="8", padx=30, pady=30,font=small_font, command=lambda: num_click(8))
but_9 = Button(root, text="9", padx=30, pady=30,font=small_font, command=lambda: num_click(9))
but_clear = Button(root, text="C", padx=31, pady=30,font=small_font, command=clear_click)

#row 2
but_4 = Button(root, text="4", padx=30, pady=30,font=small_font, command=lambda: num_click(4))
but_5 = Button(root, text="5", padx=30, pady=30,font=small_font, command=lambda: num_click(5))
but_6 = Button(root, text="6", padx=30, pady=30,font=small_font, command=lambda: num_click(6))
but_add = Button(root, text="+", padx=30, pady=30,font=small_font,command= add_click)

#row 3
but_1 = Button(root, text="1", padx=30, pady=30,font=small_font, command=lambda: num_click(1))
but_2 = Button(root, text="2", padx=30, pady=30,font=small_font, command=lambda: num_click(2))
but_3 = Button(root, text="3", padx=30, pady=30,font=small_font, command=lambda: num_click(3))
but_sub = Button(root, text="-", padx=33, pady=30,font=small_font, command=sub_click)

#row 4
but_period = Button(root, text=".", padx=31, pady=30,font=small_font, command=lambda: num_click("."))
but_0 = Button(root, text="0", padx=30, pady=30,font=small_font, command=lambda: num_click(0))
but_mul = Button(root, text="x", padx=32, pady=30,font=small_font, command=mul_click)
but_div= Button(root, text="÷", padx=28, pady=30, font=small_font,command=div_click)

#row 5
but_equal = Button(root, text="=", padx=150, pady=12,font=large_font, command=equal_click)

# button placement
#row 1
but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)
but_clear.grid(row=1, column=3)

#row 2
but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)
but_add.grid(row=2, column=3)

#row 3
but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)
but_sub.grid(row=3, column=3)

#row 4
but_period.grid(row=4, column=0)
but_0.grid(row=4, column=1)
but_mul.grid(row=4, column=3)
but_div.grid(row=4, column=2)

#row 5
but_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()
