#return palabra reservada para regresar infromacion a la linea donde se llamo
#podemos pasar parametros por default, con un valor predefiido
#esos valores se usaran en caso de que no se mando ningun parametro
def suma(a=0,b=0):
    return a+b


print("El resultado es: ", suma(6, 2))
print("El resultado es: ", suma())
print("El resultado es: ", suma(2))
#print("El resultado es: ", suma(,2)), asi no funciona
