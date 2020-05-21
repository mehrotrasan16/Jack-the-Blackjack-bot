import itertools

card_dict = {0:'A',1:'A', 11:'J', 12:'Q', 13:'K'}
card_outcomes = [i%14 for i in range(1,53)]

#sample_space = list(itertools.product(card_outcomes,repeat=2))
#print(sample_space)

suits = ['h','c','s','d']
cards = list(range(1,11))
cards.extend(['j','q','k'])

print(cards)

#Setting sequence flag to one so that 1,2,3,4 != 4,3,2,1
seq = 1 

#Number of cards to draw
draw = 2

#with replacement
replace = 1

deck = list(itertools.product(suits,cards))
sample_space = list(itertools.product(deck,repeat=draw))

#favorable_outcomes = [i for i in sample_space if i[0][0] == 'c' or i[1][0] == 'c'] #Both are clubs
favorable_outcomes = [i for i in sample_space if i[0][0] == i[1][0]] # both are the same suit

prob = len(favorable_outcomes)/len(sample_space)
print(prob)
