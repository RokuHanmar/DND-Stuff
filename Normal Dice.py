# Rolls dice. Can roll any standard DND dice (4, 6, 8, 10, 12, 20, 100). Can roll any number of dice, and allows a user to add a modifier for said dice

import random

def rollDie():

    #Get the type of die
    die = int(input("Enter the number of sides: "))
    while die != 4 and die != 6 and die != 8 and die != 10 and die != 12 and die != 20 and die != 100:
        print("Invalid number. Try again")
        die = int(input("Enter the number of sides: "))

        # add a modifier - set to 0 if there is no modifier
        modifier = int(input("What is the modifier? "))
    
    #Get the number of dice
    number = int(input("How many dice are you rolling? "))
    while number < 1:
        print("Invalid number. Try again")
        number = int(input("How many dice are you rolling? "))
    total = 0

    #Roll each die
    for i in range(number):
        roll = random.randint(1, die)
        modifiedRoll = roll + modifier
        print("Die", str(i + 1) + " (without modifiers):", str(roll) + "\n")
        print("Die", str(i + 1) + " (with modifiers):", str(modifiedRoll) + "\n")
        total += modifiedRoll
    print("Total: " + str(total))

rollDie()

