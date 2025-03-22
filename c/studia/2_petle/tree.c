#include <stdio.h>

int main() {
    const int wys = 5;

    for (int i = 0; i < wys; i++) {
        for (int spacje = 0; spacje < wys - i - 1; spacje++) {
            printf(" ");
        }
        for (int gwiazdki = 0; gwiazdki < 2 * i + 1; gwiazdki++) {
            printf("*");
        }
        printf("\n");
    }

    for (int spacje = 0; spacje < wys - 1; spacje++) {
        printf(" ");
    }
    printf("*\n");

    for (int spacje = 0; spacje < wys - 2; spacje++) {
        printf(" ");
    }
    printf("***\n");

    return 0;
}