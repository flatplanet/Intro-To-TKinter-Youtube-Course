from random import randint
import random 

answer_list = []

global our_states
our_states = ['california', 'florida', 'illinois', 'kentucky', 'nebraska', 'nevada', 'newyork', 'oregon', 'texas', "vermont"]

global our_state_capitals
our_state_capitals = {
'california':"sacramento", 
'florida':"tallahassee", 
'illinois':"springfield", 
'kentucky':"frankfort", 
'nebraska':"lincoln", 
'nevada':"carson city", 
'newyork':"albany", 
'oregon':"salem", 
'texas':"austin", 
'vermont':"montpelier"
}

#Generate a random number
global rando
rando = randint(0, len(our_states)-1)
print (our_states[rando])

# Make this the answer
answer = our_states[rando]

#Add to new list
answer_list.append(our_states[rando])
print(answer_list)

# Remove from old list
our_states.remove(our_states[rando])
print (our_states)

#Shuffle original list
random.shuffle(our_states)

# Second  random number
rando2 = randint(0, len(our_states)-1)
print (our_states[rando2])

#Add Second Name to new list
answer_list.append(our_states[rando2])
print(answer_list)

#Shuffle original list again
random.shuffle(our_states)

# Third random number
rando3 = randint(0, len(our_states)-1)
print (our_states[rando3])

#Add Third Name to new list
answer_list.append(our_states[rando3])
print(answer_list)

# Shuffle our answer list
random.shuffle(answer_list)
print(answer_list)