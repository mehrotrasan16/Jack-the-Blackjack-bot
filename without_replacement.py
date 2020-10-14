# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:23:17 2020

@author: SanketM
"""
#Author:Sanket Mehrotra
#Card probability calculation without replacement

import itertools

card_dict = {0:'A',1:'A', 11:'J', 12:'Q', 13:'K'}
card_outcomes = [i%14 for i in range(1,53)]

#sample_space = list(itertools.product(card_outcomes,repeat=2))
#print(sample_space)

suits = ['h','c','s','d']
cards = list(range(1,11))
cards.extend(['j','q','k'])

#print(cards)

#Setting sequence flag to one so that 1,2,3,4 != 4,3,2,1
seq = 1 

#Number of cards to draw
draw = 2

#with replacement
replace = 1

sample_space= list(itertools.product(suits,cards))
print(sample_space)
#sample_space = list(itertools.product(deck,repeat=draw))

#see what we've done
#print(sample_space[0],sample_space[1])

#favorable_outcomes = [i for i in sample_space if i[0][0] == i[1][0]] # both are the same suit

#prob = len(favorable_outcomes)/len(sample_space)
#print(prob)

conditions = [('c',1),('c',2)]
probs = []
favorable_outcomes = []

for j in range(draw):
    favorable_outcomes = [i for i in sample_space if i[0] == conditions[j][0] and i[1] == conditions[j][1]]
    print(favorable_outcomes)
    probs += [len(favorable_outcomes)/len(sample_space)]
    print(probs)
    #sample_space.remove(favorable_outcomes[0])
    for k in favorable_outcomes:
        sample_space.remove(k)
    print(sample_space)
    
