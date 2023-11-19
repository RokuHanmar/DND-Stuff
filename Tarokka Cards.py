import random

usedLow = []
usedHigh = []

lowDeck = [["Glyphs", "Swords", "Stars", "Coins"], ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Master"]]

highDeck = ["Ghost", "Innocent", "Marrionette", "Darklord", "Mists", "Executioner", "Broken One", "Tempter", "Beast", "Donjon", "Raver", "Seer", "Artifact", "Horseman"]

print("Low Cards:")
for i in range(0, 3):
    suit = random.randint(0, 3)
    number = random.randint(0, 9)
        
    cardSuit = lowDeck[0][suit]
    cardNumber = lowDeck[1][number]
    card = [cardSuit], [cardNumber]
    while card in usedLow:
        cardSuit = lowDeck[0][suit]
        cardNumber = lowDeck[1][number]
    usedLow.append(card)
    
    print(cardNumber + " of " + cardSuit)

print("\nHigh Cards:")
for i in range(0, 2):
    card = random.randint(0, 13)
    highCard = highDeck[card]
    while highCard in usedHigh:
        card = random.randint(0, 13)
        highCard = highDeck[card]
    usedHigh.append(highCard)
    
    print(highCard)