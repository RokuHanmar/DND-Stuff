# Import libraries
import random

# Define variables
level = 1
global charismaModifier
charismaModifier = 5
charismaBonus = 3
beamCounter = 1
agonisingBlast = False

# Creates beam function - prints out the beam number (based on Beam Counter) and damage (based on D10 and Charisma
# modifier if Agonising Blast is used)
def RollD20():
    D20 = random.randint(1, 20)
    return D20

def beam():
    if agonisingBlast == True:
        damage = random.randint(1, 10) + charismaBonus
    else:
        damage = random.randint(1, 10)
    return damage

# Changes the amount of beams generated based on player level
def beamNumber():
    if 5 > level:
        numberOfBeams = 1
    elif level >= 5 and level < 11:
        numberOfBeams = 2
    elif level >= 11 and level < 17:   
        numberOfBeams = 3
    elif level >= 17:
        numberOfBeams = 4
    
    return numberOfBeams

# Creates Eldritch Blast function, which generates saving throw based on a D20 and the Charisma Modifier, then generates
# beams using the BeamNumber and beam functions
def eldritchBlast():
    D20Roll = RollD20()
    attackRoll = D20Roll + charismaModifier
    print("To save:", str(attackRoll))# Replace Charisma Modifier with Hit Chance if
    # they're different for any reason
    
    # Redefine scope of Beam Counter to allow it to keep its value and prevent errors from lack of definition
    global beamCounter
    
    if D20Roll != 1:
        if D20Roll == 20:
            print("Critical hit! Attacks deal double damage!")
            while (beamNumber()) + 1 > beamCounter:
                damage = beam()
                damage = damage * 2
                print("Beam " + str(beamCounter) + ": " + str(damage))
                beamCounter += 1
        else:
            while (beamNumber()) + 1 > beamCounter:
                damage = beam()
                print("Beam " + str(beamCounter) + ": " + str(damage))
                beamCounter += 1
    else:
        print("Critical miss!")

# Call function
eldritchBlast()