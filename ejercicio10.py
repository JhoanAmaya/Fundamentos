
#Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.
from datetime import date

usuario = input("Ingresa tu nombre completo: ")
año = int(input("Ingresa el año de nacimiento: "))
if (año<=0):
    print("¡Error no se puede hallar año con signo negativo!")
else :
    mes = int(input("Ingresa el mes de nacimiento: "))
    if (mes<=0):
        print("¡Error no se puede hallar mes con signo negativo!")
    else :
        dia = int(input("Ingresa el dia de nacimiento: "))
        if (dia<=0):
            print("¡Error no se puede hallar dia con signo negativo!")

fecha_nacimiento_usuario = date(año, mes, dia) # La fecha de nacimiento que escribe el usuario.
fecha_actual = date.today() #fecha actual
usuario_mes = fecha_nacimiento_usuario.month #el mes del usuario.
fecha_actual_mes = fecha_actual.month #el mes de este año.
meses = 12 # 1 año

if (usuario_mes>fecha_actual_mes):
    result_mes = usuario_mes - fecha_actual_mes
    edad = fecha_actual.year - fecha_nacimiento_usuario.year
    resultado = (edad * meses) - result_mes
    print(usuario,"tiene",resultado,"meses entre su fecha de nacimiento y la fecha actual.")
else :
    result_mes = fecha_actual_mes - usuario_mes
    edad = fecha_actual.year - fecha_nacimiento_usuario.year
    resultado = (edad * meses) + result_mes
    print(usuario,"tiene",resultado,"meses entre su fecha de nacimiento y la fecha actual.")
