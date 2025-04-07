verbo = input("ingrese un verbo en infinitivo: ")
terminacion = verbo[-2:]
if terminacion == "ar" or terminacion == "er" or terminacion == "ir":
    print("la terminación del verbo es:", terminacion)
else:
    print("ERROR PALABRA NO VALIDA :c")