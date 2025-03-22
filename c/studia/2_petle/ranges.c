#include <stdio.h>
#include <limits.h>  // dla typów całkowitych
#include <float.h>   // dla typów zmiennoprzecinkowych

int main() {
    printf("Zakres zmiennych w aktualnej implementacji C:\n\n");

    // Typy całkowite
    printf("char: %d do %d (rozmiar: %lu bajtów)\n", CHAR_MIN, CHAR_MAX, sizeof(char));
    printf("unsigned char: 0 do %u (rozmiar: %lu bajtów)\n", UCHAR_MAX, sizeof(unsigned char));
    
    printf("short: %d do %d (rozmiar: %lu bajtów)\n", SHRT_MIN, SHRT_MAX, sizeof(short));
    printf("unsigned short: 0 do %u (rozmiar: %lu bajtów)\n", USHRT_MAX, sizeof(unsigned short));
    
    printf("int: %d do %d (rozmiar: %lu bajtów)\n", INT_MIN, INT_MAX, sizeof(int));
    printf("unsigned int: 0 do %u (rozmiar: %lu bajtów)\n", UINT_MAX, sizeof(unsigned int));
    
    printf("long: %ld do %ld (rozmiar: %lu bajtów)\n", LONG_MIN, LONG_MAX, sizeof(long));
    printf("unsigned long: 0 do %lu (rozmiar: %lu bajtów)\n", ULONG_MAX, sizeof(unsigned long));
    
    printf("long long: %lld do %lld (rozmiar: %lu bajtów)\n", LLONG_MIN, LLONG_MAX, sizeof(long long));
    printf("unsigned long long: 0 do %llu (rozmiar: %lu bajtów)\n", ULLONG_MAX, sizeof(unsigned long long));

    // Typy zmiennoprzecinkowe
    printf("\nfloat: od %.10e do %.10e (rozmiar: %lu bajtów)\n", FLT_MIN, FLT_MAX, sizeof(float));
    printf("double: od %.10e do %.10e (rozmiar: %lu bajtów)\n", DBL_MIN, DBL_MAX, sizeof(double));
    printf("long double: od %.10Le do %.10Le (rozmiar: %lu bajtów)\n", LDBL_MIN, LDBL_MAX, sizeof(long double));

    return 0;
}