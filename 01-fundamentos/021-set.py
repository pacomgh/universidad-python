#set es una coleccion sin orden y sin indices, no permite elementos repetidos
#los elementos no se pueden modificar pero si agregar o eliminar
planetas = { "Marte", "Jupiter", "Venus" }
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento esta contenido en el set, true/false
print( "Marte" in planetas)
#agregar
planetas.add("Tierra")
print(planetas)
#eliminar con remove, posible excepcion si no se encuentra el elemento
planetas.remove("Tierra")
print(planetas)
#eliminar con discard, no arroja excepcion
planetas.discard("Jupiters")
print(planetas)
#limpiar set completamente
planetas.clear()
print(planetas)
#eliminar la variable
del planetas
print(planetas)