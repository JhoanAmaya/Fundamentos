
# Mostrar en pantalla la cantidad de segundos que tiene un lustro.

minuto = 60 #segundos
hora = 60 #minutos
dia = 24 #horas
año = 365 #dias

lustro = int(input("Ingresa el lustro: "))
resultado = (((minuto*hora)*dia)*año)
total = resultado*lustro
print("Un lustro tiene: ",total,"segundos")
