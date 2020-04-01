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

count = 1

while count < 4:
	rando = randint(0, len(our_states)-1)
	if count == 1:
		answer = our_states[rando]
	
	# Add our first selection to a new list
	answer_list.append(our_states[rando])
	
	# Remove from old list
	our_states.remove(our_states[rando])

	#Shuffle original list
	random.shuffle(our_states)

	count += 1

print(answer_list)
print(answer)
