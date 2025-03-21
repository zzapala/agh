#include <stdio.h>

int main() {
    printf("Wersja standardu C: ");

    if (__STDC_VERSION__ == 199409L) {
        printf("C95 (199409L)\n");
    } else if (__STDC_VERSION__ == 199901L) {
        printf("C99 (199901L)\n");
    } else if (__STDC_VERSION__ == 201112L) {
        printf("C11 (201112L)\n");
    } else if (__STDC_VERSION__ == 201710L) {
        printf("C17 (201710L)\n");
    } else if (__STDC_VERSION__ == 202000L) {
        printf("C2x (202000L)\n");
    } else if (__STDC_VERSION__ == 202311L) {
        printf("C23 (202311L)\n");
    } else {
        printf("Nieznana wersja C (__STDC_VERSION__ = %ld)\n", __STDC_VERSION__);
    }

    return 0;
}