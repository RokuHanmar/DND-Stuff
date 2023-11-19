# Program used to roll stats for a character. Rolls 4d6 and drops the lowest, returning the sum of the 3 remaining dice. It does this 6 times to create an array of scores

import random

def getRolls():
    D6 = random.randint(1, 6)
    return D6
  
def getLowest(die1, die2):
    if die1 > die2:
        lowest = die2
    if die1 < die2:
        lowest = die1
    if die1 == die2:
        lowest = die2
    return lowest

def getLowestOfFour(die1, die2, die3, die4):
    total = 0
    pair1 = getLowest(die1, die2)
    pair2 = getLowest(die3, die4)
    lowest = getLowest(pair1, pair2)
    total = die1 + die2 + die3 + die4 - lowest
    print("Total: " + str(total) + "\n")
    
def getAbilities():    
    die1 = getRolls()
    print("die 1: " + str(die1))
    
    die2 = getRolls()
    print("die 2: " + str(die2))
    
    die3 = getRolls()
    print("die 3: " + str(die3))
    
    die4 = getRolls()
    print("die 4: " + str(die4))
    
    getLowestOfFour(die1, die2, die3, die4)

for i in range(6):
    getAbilities()
