#include <stdio.h>
#include <limits.h>

int main() {
    // Zmienna ze znakiem
    signed int si = INT_MAX;
    printf("signed int przed inkrementacją: %d\n", si);
    si = si + 1;  // Przekroczenie zakresu
    printf("signed int po przekroczeniu: %d\n", si);

    // Zmienna bez znaku
    unsigned int ui = UINT_MAX;
    printf("\nunsigned int przed inkrementacją: %u\n", ui);
    ui = ui + 1;  // Przekroczenie zakresu
    printf("unsigned int po przekroczeniu: %u\n", ui);

    // Dekrementacja
    signed int si2 = INT_MIN;
    printf("\n signed int przed dekrementacją: %d\n", si2);
    si2--;
    printf("signed int po przekroczeniu: %d\n", si2);

    unsigned int ui2 = 0;
    printf("\nunsigned int przed dekrementacją: %u\n", ui2);
    ui2--;
    printf("unsigned int po przekroczeniu: %u\n", ui2);

    return 0;
}