
#Calcular el número de vueltas que da una llanta en 1 km, dado que el diámetro de la llanta es de 50 cm,
# mostrar el resultado en pantalla.

""" Hallar radio, luego, hallamos la longitud aplicando la formula 2*π*r para hallar el
recorrido de una vuelta con el diamentro de 50cm, lo cual la distancia de una vuelta queda en centimetros."""

diametro = 50 #centimetros
radio = diametro/2 #centimetros
longitud = (2*3.14*radio) #centimetros
centimetros = 100000 # 1 kilometro

distancia = int(float(input("Ingresa la distancia: ")))
resultado = centimetros*distancia
total = resultado/longitud
print("Una llanta de 50cm de diametro hace un recorrido de: ",int(total),"vueltas")
