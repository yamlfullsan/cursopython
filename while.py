#While --> ejecuta mientras condición sea verdadera.
import math
print("Programa para raiz cuadrada.")
numero=int(input("Introduce un numero: "))

intentos=0
while numero<0:
    print("No hay raiz cuadrada de negativos.")

    if intentos==2:
        print("Demasiados intentos.")
        break;
    
    numero=int(input("Introduce un numero: "))
    if numero<0:
        intentos=intentos+1 
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero)+ " es " +str(solucion))