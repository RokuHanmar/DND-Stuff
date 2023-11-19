# Implementation for the Deck of Many Things
# IMPORTANT: use of this code requires a text file named Previous Uses stored in the same directory as the program. This is to ensure the same card is never drawn twice. My Previous Uses file has not been 
# provided, as it contains cards I have previously drawn and will therefore interfere with any cards drawn in a different campaign

import random

cards = ["Vizier\n", "Sun\n", "Moon\n", "Star\n", "Comet\n", "The Fates\n", "Throne\n", "Key\n", "Knight\n", "Gem\n", "Talons\n", "The Void\n", "Flames\n", "Skull\n", "Idiot\n", "Donjon\n", "Ruin\n", "Euryale\n", "Rogue\n", "Balance\n", "Fool\n", "Jester\n"]


def readFile():
    drawn = []
    previousUses = open("Previous Uses.txt", "r")
    for line in previousUses:
        drawn.append(line)
    previousUses.close()
    return drawn



def draw(numberOfCards):
    for i in range(0, numberOfCards):
        drawn = readFile()
        remainingCards = len(cards) - len(drawn)
        if remainingCards <= 0:
            print("There are no more cards in the Deck")
            
        else:    
            if remainingCards >= 0:
                cardDrawn = random.randint(0, len(cards)-1)
                card = cards[cardDrawn]
                
                while card in drawn:
                    cardDrawn = random.randint(0, len(cards)-1)
                    card = cards[cardDrawn]
                previousUses = open("Previous Uses.txt", "a")
                previousUses.write(card)
                previousUses.close()
                print(card)
                remainingCards -= 1
                i += 1
        
                if remainingCards <= 0:
                    print("There are no more cards in the Deck")


draw(int(input("How many cards are you drawing? ")))
