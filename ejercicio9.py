alto=float(input("ingrese la altura de la pileta en metros (solo numero): "))
ancho=float(input("ingrese el ancho de la pileta en metros (solo numero): "))
largo=float(input("ingrese el largo de la pileta en metros (solo numero): "))
volumen=ancho*alto*largo
litros=volumen*1000
print("El volumen de la pileta es: ", volumen, "cm3")
print("La cantidad de litros que tiene la pileta es: ", litros, "litros")