#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int health = 3;
    int enemy_health = 4;

    while (health > 0) {
        printf("Do you want to attack? (y/n)\n");

        char response = ' ';
        int response_received = scanf(" %c", &response);

        if (response == 'y' || response == 'Y') {
            health--;
            enemy_health--;
            printf("You attacked each other and both lost health.\n");
        } else if (response == 'n' || response == 'N') {
            printf("It stares at you menacingly.\n");
        }

        if (enemy_health == 0) {
            printf("You were victorious!\n");
            return 0;
        }

        fflush(stdin);
    }

    printf("Oh no, you died!\n");

    return 0;
}