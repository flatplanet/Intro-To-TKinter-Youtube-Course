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

'''
#Generate a random number
global rando
rando = randint(0, len(our_states)-1)

#print(our_states[rando])
#print(our_state_capitals[our_states[rando]])

answer = our_states[rando]

# add our first random selection to our answer_list list
answer_list.append(our_states[rando])

#remove answer from list
our_states.remove(our_states[rando])


# Shuffle our original list
random.shuffle(our_states)

# Randomly select our next state
rando = randint(0, len(our_states)-1)
answer_list.append(our_states[rando])

#remove 2nd answer from list
our_states.remove(our_states[rando])

# Shuffle our original list
random.shuffle(our_states)

# Randomly select our third state
rando = randint(0, len(our_states)-1)
answer_list.append(our_states[rando])

print(answer_list)
print(answer)
'''
count = 1

while count < 4:
	rando = randint(0, len(our_states)-1)
	# If first selection, make it our answer
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
random.shuffle(answer_list)
print(answer_list)

print(our_state_capitals[answer])


