numero=int(input("Introduce un numero: "))

mayor=100
menor=0

if numero<=mayor:
    if numero>=menor:
        print("Numero dentro del rango")
    else:
        print("Numero menor al rango")
else:
    print("Numero mayor al rango")
