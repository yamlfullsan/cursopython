print("Programa de evaluación")
nota_alumno=input("Introduce la nota: ")
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion(int(nota_alumno))) 
