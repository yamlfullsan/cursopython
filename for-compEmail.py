contador=0
dire=input("Escribe tu email: ")

for i in dire:
    if(i=="@" or i=="."):
        contador=contador+1

if contador==2:
    print("Correo correcto.")
else:
    print("Correo incorrecto.")

