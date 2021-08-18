#include <stdio.h>

int main ()
{
    double area, n, raio;

    n = 3.14159;

    scanf ("%lf", &raio);

    area = n * pow(raio, 2);

    printf("A=%.4f\n", area);

    return 0;
}