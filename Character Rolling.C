// Program used to roll stats for a character. Rolls 4d6 and drops the lowest, returning the sum of the 3 remaining dice. It does this 6 times to create an array of scores

#include <stdio.h>
#include <stdlib.h>

time_t t6;
srand ((unsigned) time (&t6));

int getRolls(){
    int d6 = rand() % 7;
    return d6;
}

int getLowest(die1, die2) {
    int lowest = 0;
    
    if (die1 > die2) {
        lowest = die1;
    } else if (die2 > die1) {
        lowest = die2;
    } else {
    lowest = die2;
    }
    
return lowest;
}

int getLowestOfFour(die1, die2, die3, die4) {
    int total = 0;
    int pair1 = getLowest(die1, die2);
    int pair2 = getLowest(die3, die4);
    int lowest = getLowest(pair1, pair2);
    total = die1 + die2 + die3 + die4 - lowest;
    printf("%s %d \n", "Total:", total);
}

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
