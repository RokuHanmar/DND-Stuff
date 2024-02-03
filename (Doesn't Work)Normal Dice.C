#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    time_t t20;
    srand ((unsigned) time (&t20));
/*
    // ERROR - doesn't take an input
    // Get number of sides
    printf("%d\n", "Enter the number of sides: ");
    int sides;
    scanf("%d", &sides);
*/

/*
    int sides = 20; // TEMP
    // Verify valid die
    while (sides != 2 && sides != 3 && sides != 4 && sides != 6 && sides != 8 && sides != 10 && sides != 12 && sides != 20 && sides != 100) {
        printf("%d\n", "Invalid. Enter the number of sides: ");
        scanf("%d", &sides);
    }
*/

    // Get modifiers
    printf("%d\n", "Enter modifier. If there are none, enter 0: ");
   // int modifier;
    //scanf("%d", &modifier);

/*
    // Get number of dice
    printf("%d\n", "Enter number of dice: ");
    int numberOfDice;
    scanf("%d", &numberOfDice);

    // Roll dice
    sides++; // This ensures the rand() function utilises the correct numbers
    for (int i = 0; i < (numberOfDice+1);i++) {
        int roll = rand() % sides;
        while (roll == 0) {
            roll = rand() % sides;
        }
        int modifiedRoll = roll + modifier;
        printf("%s %d %s %d \n", "Die", i, "before modifiers:", roll);
        printf("%s %d %s %d \n", "Die", i, "after modifiers:", modifiedRoll);
    }


*/
    return 0;
}

// TODO: program compiles, but does not run properly. Returns a specific string of numbers and no more. Possibly an issue with time

// Looks to be an issue with input handling
