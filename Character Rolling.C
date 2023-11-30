// Program used to roll stats for a character. Rolls 4d6 and drops the lowest, returning the sum of the 3 remaining dice. It does this 6 times to create an array of scores

#include <stdio.h>
#include <stdlib.h>


int main() {
    time_t t6;
    srand ((unsigned) time (&t6));

    int roll() {
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
        return total;
    }

    int getAbilities(){
        int die1 = getRolls();
        printf("%s%d\n", "die 1:", die1);
        
        int die2 = getRolls();
        printf("%s%d\n", "die 2:", die2);
        

        int die3 = getRolls();
        printf("%s%d\n", "die 3:", die3);
            
        
        int die4 = getRolls();
        printf("%s%d\n", "die 4:", die4);
        
        int totalScore = getLowestOfFour(die1, die2, die3, die4);

        return totalScore;
    }

    for (int i = 0; i < 6; i++){
        getAbilities();
    }

    return 0;
}
