productos_total=[]
total=0
for i in range (2):
    nombre=input("ingrese el nombre del producto: ")
    cantidad=int(input("ingrese la cantidad comprada del producto: "))
    precio_unitario=int(input("ingrese el precio por unidad del producto: "))
    producto=[nombre, cantidad, precio_unitario]
    productos_total.append(producto)
for producto in productos_total:
    nombre = producto[0]
    cantidad = producto[1]
    precio_unitario=producto[2]
    gasto= cantidad*precio_unitario
    print("el precio total de: ",nombre, "es: ",gasto)
    total=total+gasto
print("el precio total de todos los productos es " + str (total))