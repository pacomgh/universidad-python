#Mantiene el orden, no se puede modificar
frutas = ("manzana", "pera", "uva", "guayaba")

print(frutas)
#largo de la tupla
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#rango
print(frutas[0:2])#exclute al indice 2
#modificar un valo
#rutas[0] = "Naranjita"
#print(frutas)
#para modificar una tupla debemos convertir a lista modificar la lista
#y convertirla a tupla nuevamente
frutasLista = list(frutas)
frutasLista[1] = "platanito"
frutas = tuple(frutasLista)
print(frutas)
#iterar una tupla
for fruta in frutas:
    #cambiamos el salto de linea del print por un espacio
    print(fruta, end=" ")
#no se pueden eliminar elementos de una tupla
#se puede eliminar la variable de la tupla
del frutas
print(frutas)