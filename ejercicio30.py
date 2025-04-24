total_letras = 0
for i in range(5):
    palabra = input(f" Ingresá la palabra {i+1}: ")
    total_letras += len(palabra)
print("Cantidad total de letras:", total_letras)