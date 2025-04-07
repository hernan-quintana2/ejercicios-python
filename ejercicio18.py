nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
dia = input("ingrese el día de nacimiento: ")
mes = input("ingrese el mes de nacimiento: ")
a = input("ingrese el año de nacimiento: ")
iniciales = nombre[0] + apellido[0]
clave = iniciales + "_" + a
print("Su clave es:", clave)