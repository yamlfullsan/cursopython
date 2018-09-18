#include <stdio.h>
#include <curses.h>

#define LimiSupe 200
#define LimiInfe 100

int main()
{
printf("hola");
float Numero=0; // Definicion de variable.

printf( "=== Problema 1 ===\n");
printf("Introduzca un numero: ");
scanf("%f", &Numero);

if (Numero>= LimiInfe){
    if (Numero<=LimiSupe){
        printf("Esta dentro del intervalo");
    }
    else 
    printf("Supera el limite maximo");
}
else 
printf("No alcanza el limite minimo");

return 0;
}