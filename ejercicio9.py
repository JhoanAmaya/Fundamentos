
#Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles).
print("Por favor calificar al estudiante de este corte:")
ES = int(input("Calificacion de Español: "))
MA = int(input("Calificacion de Matemáticas: "))
EC = int(input("Calificacion de Economía: "))
PR = int(input("Calificacion de Programación: "))
EN = int(input("Calificacion de Ingles: "))

#Hallar total de materias...
materias = 5

#Hallar el promedio...
promedio = (ES+MA+EC+PR+EN)/materias
if (promedio<3):
    print("Su promedio es: ",promedio,"¡Ups! Perdio el estudiante...que repita el semestre por favor jaja")
elif (promedio>=3 and promedio<=3.5):
    print("Su promedio es: ",promedio,"¡Ishh! Paso raspando...debe mejorar un poco el estudiante")
else :
    print("Su promedio es: ",promedio,"¡Congratulations! Paso el estudiante...sigue asi y alcanzaras tus metas y sueños.")
