#include <stdio.h>
#include <stdlib.h>

int main() {
    time_t t6;
    srand ((unsigned) time (&t6));

    // Get number of sides
    printf("%c\n", "Enter the number of sides: ");
    int sides;
    scanf("%c", &sides);

    // Verify valid die
    while (sides != 2 && sides != 3 && sides != 4 && sides != 6 && sides != 8 && sides != 10 && sides != 12 && sides != 20 && sides != 100) {
    printf("%c\n", ". Invalid. Enter the number of sides: ");
    scanf("%d", &sides);
    }






    return 0;
}
