
#Dado de los valores ingresados por el usuario (base, altura) calcular y mostrar en pantalla el área de un triángulo.

base = int(float(input("Ingresa la base de un triangulo: ")))
if (base<=0):
    print("'Ups'Ingresa un numero positivo en la base...")

else :
    altura = int(float(input("Ingresa la altura de un triangulo: ")))
    if (altura<=0):
        print("'Ups'Ingresa un numero positivo en la altura...")
area = ((base*altura)/2)
print("El area del triangulo es: ",area)
