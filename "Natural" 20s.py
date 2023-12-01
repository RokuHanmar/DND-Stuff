# Rigged die for DM use only. Will only roll natural 20s on any d20 rolled

import random

def rollDie():

    #Get the type of die
    die = int(input("Enter the number of sides: "))
    while die != 4 and die != 6 and die != 8 and die != 10 and die != 12 and die != 20 and die != 100:
        print("Invalid number. Try again")
        die = int(input("Enter the number of sides: "))

    areModifiers = input("Are there modifiers? ")
    while areModifiers.lower() != "yes" and areModifiers.lower() != "no":
        print("Invalid answer. Try again")
        areModifiers = input("Are there modifiers? ")
            
    if areModifiers.lower() == "yes":
        modifier = int(input("What is the modifier? "))
    else:
        modifier = 0
        
    #Get the number of dice
    number = int(input("How many dice are you rolling? "))
    while number < 1:
        print("Invalid number. Try again")
        number = int(input("How many dice are you rolling? "))
    total = 0

    #Roll each die
    for i in range(number):
        roll = random.randint(1, die)
        if die == 20:
            roll = 20
        modifiedRoll = roll + modifier
        print("Die", str(i + 1) + " (without modifiers):", str(roll) + "\n")
        print("Die", str(i + 1) + " (with modifiers):", str(modifiedRoll) + "\n")
        total += modifiedRoll
    print("Total: " + str(total))

rollDie()
