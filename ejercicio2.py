
# Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos y mostrar el resultado en pantalla.

pesos_colombianos = 3849.51
dolar = int(float(input("Ingresa el valor en dolar: ")))
if (dolar<=0):
    print("'Ups' Ingresa valores positivos")
else :
    resultado = dolar*pesos_colombianos
    print("El valor en pesos colombianos es: ",resultado)
