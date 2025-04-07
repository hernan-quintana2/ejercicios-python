frase=input("ingresa una frase: ")
iniciales=frase.split()
letras=""
for iniciales in iniciales:
    letras=letras + iniciales[0]
print(letras)