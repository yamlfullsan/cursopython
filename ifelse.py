#Verificacion de acceso.
print("verificación de acceso")
edad_usuario=int(input("Introduce tu edad: "))

if edad_usuario<18:
    print("No puede pasar")
elif edad_usuario>100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")
print("Programa finalizado.")