from tkinter import *
from random import choice
from random import shuffle


root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x400+-1900+100")


my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)

def shuffler():
    # Clear Hint Label 
    hint_label.config(text='')

    # Clear Hint Count
    global hint_count
    hint_count = 0

    # Clear Answer Box
    entry_answer.delete(0, END)

    # Clear Answer Label
    answer_label.config(text='')

    # List of state words
    states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts', 'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota', 'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina', 'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas', 'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin', 'Delaware', 'Idaho', 'Arkansas', 'Louisiana']

    # Pick random state from list
    global word
    word = choice(states)
    

    # Break apart our chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)
    
    # Turn shuffeled List into a word
    global shuffled_word
    shuffled_word =  ''
    for letter in break_apart_word:
        shuffled_word += letter
    
    # print shuffled word to the screen
    my_label.config(text=shuffled_word)

#Create answer Function
def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct!!")
    else:
        answer_label.config(text="Incorrect!!")

# Create Hint Counter
global hint_count
hint_count = 0

# Create Hint Function
def hint(count):
    global hint_count
    hint_count = count

    # Get the length of the chosen word
    word_length = len(word)

    # Show Hint
    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count +=1 

entry_answer = Entry(root, font=("Helvetica", 24))
entry_answer.pack(pady=20)


button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=10)

my_button = Button(button_frame, text="Pick Another Word", command=shuffler)
my_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)


answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

hint_label = Label(root, text='', font=("Helvetica", 18))
hint_label.pack(pady=10)

shuffler()
root.mainloop()