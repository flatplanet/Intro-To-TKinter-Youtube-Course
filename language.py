from tkinter import *
from random import randint

root = Tk()
root.title('Codemy.com - Spanish Language Flashcards')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("550x410")

words = [
    (("Hola"), ("Hello")),
    (("Adiós"), ("Goodbye")),
    (("Por favor"), ("Please")),
    (("Gracias"), ("Thank you")),
    (("Lo siento"), ("Sorry")),
    (("Salud"), ("Bless you")),
    (("Sí"), ("Yes")),
    (("No"), ("No")),
    (("¿Quién?"), ("Who")),
    (("¿Qué?"), ("What")),
    (("¿Por qué?"), ("Why")),
    (("¿Dónde?"), ("Where"))
]

# get a count of our word list
count = len(words)

def next():
    global hinter, hint_count
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint stuff
    hinter = ""
    hint_count = 0

    # Create random selection
    global random_word
    random_word = randint(0, count-1)
    # update label with Spanish Word
    spanish_word.config(text=words[random_word][0])

def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

# Keep Track Of the Hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1



# Labels
spanish_word = Label(root, text="", font=("Helvetica", 36))
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Create Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1,)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run next function when program starts
next()

root.mainloop()