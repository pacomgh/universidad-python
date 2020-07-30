#creacion y uso de listas
nombres = ["juan", 'pedro', "jose",'paco']

print(nombres)
#conocer el largo de la lista
print(len(nombres))
#imprimir n elemento
print(nombres[2])
#mavegacion inversa
print(nombres[-1])
print(nombres[-3])
#imprimir rango
print(nombres[0:2])#vamos de 0 a 1, no incluye el dos
print(nombres[:3])#imprime desde la primera posicion hasta la indicada
#imprime los elementos hasta el final desde el indice proporcionado
print(nombres[1:])
#cambiar el elemeto de una lista
nombres[3]="Maria"
print(nombres)
#iterar lista
for nombre in nombres:
    print(nombre)
#ver si existe un elemento dentro de una lista
if "manuel" in nombres:
    print("manuel existe dentro de la lista")
else:
    print("el elemento buscado no existe en la lista")

#agregar elemento al final de la lista
nombres.append("lorenzo")
print(nombres)
#agregar el elemento en una parte especifica de la lista
nombres.insert(1, "octavio")
print(nombres)
#remover elemento de la lista
nombres.remove("octavio")
print(nombres)
#remover ultimo elemento de la lista por default
nombres.pop()
#remover el indice indicado de la lista
del nombres[0]
print(nombres)
#limpiar todos los elementos de nuestra lista
nombres.clear()
print(nombres)
#eliminar lista completa, elimina la variable tambien
del nombres
print(nombres)