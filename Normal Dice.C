#include <stdio.h>
#include <stdlib.h>

int main() {
    time_t t6;
    srand ((unsigned) time (&t6));

    // Get number of sides
    printf("%d\n", "Enter the number of sides: ");
    int sides;
    scanf("%d", &sides);

    // Verify valid die
    while (sides != 2 && sides != 3 && sides != 4 && sides != 6 && sides != 8 && sides != 10 && sides != 12 && sides != 20 && sides != 100) {
        printf("%d\n", ". Invalid. Enter the number of sides: ");
        scanf("%d", &sides);
    }


    // Get modifiers
    printf("%d\n", "Enter modifier. If there are none, enter 0: ");
    int modifier;
    scanf("%d", &modifier);


    // Get number of dice
    printf("%d\n", "Enter number of dice: ");
    int numberOfDice;
    scanf("%d", &numberOfDice);

    // Roll dice
    for (int i = 0; i < (numberOfDice)+1;i++) {
        int roll = rand() % (sides+1);
        while (roll == 0) {
            roll = rand() % (sides+1);
        }
        printf("%s\n", "Die", i, "before modifiers:", roll);
        printf("%s\n", "Die", i, "after modifiers:", (roll + modifier));
    }



    return 0;
}
