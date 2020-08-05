#para el diccionario tendremos un valor llave y una descripcion asociada a esa llave
#un diccionario esta compuesto por una llave y un valor(key, value)

diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programing",
    "DBMS": "Database Management System"
}

print(diccionario)
#finciones para tabajar con diccionarios
#largo
print(len(diccionario))
#acceder a un elemento de un diccionario
print(diccionario["IDE"])
#otra forma de acceder a los elementos y tener el mismo resultado, get
print(diccionario.get("IDE"))
#podemos hacer cambios en valores de llaves
diccionario["IDE"]="Integrated development enviroment"
print(diccionario)
#iteracion sobre un diccionario, solo regresa las llaves
for termino in diccionario:
    print(termino)
#acceder a los valores
for termino in diccionario:
    print(diccionario[termino])
#recuperar los valores directamente del diccionario si usar la llave
#se pierde la llave asociada al valor
for valor in diccionario.values():
    print(valor)
    
#comprobar si existe un elemento en el diccioario
#llave in nombreDiiccionario
print("IDE" in diccionario)
print("DAO" in diccionario)
#agregar nuevos elementos
#mandamos la nueva llave = nuevo valor
diccionario["PK"] = "Primary Key"
print(diccionario)
#remover elementos del diccionario
diccionario.pop("DBMS")
print(diccionario)
#limpiar el diccionario, eliminar todos sus elementos
diccionario.clear()
print(diccionario)
#eliminamos diccionario desde la variable
del diccionario
print(diccionario)
    
