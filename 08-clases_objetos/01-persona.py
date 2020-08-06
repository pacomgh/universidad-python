#Clase es una plantilla de la que se pueden crear objetos
#en python las clases son objetos

class Persona:
    #que la pase y termine la ejecucion de la clase
    #pass
    #definimos el metodo init doble guion bajo, debe recibir self
    #self hace referencia al objeto que se ejecuta en ese momento, parecido this
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#print(Persona)
#modifica valores
Persona.nombre = "Juan"
Persona.edad = 23
#accede a los valores, nombreClase.Atributo
print(Persona.nombre)
print(Persona.edad)

#creacion de un objeto
persona = Persona("Karla", 30)
print("nombre: ",persona.nombre, " edad: ", persona.edad)
print(id(persona))  # imprime la direccion de memoria del objeto

persona2 = Persona("Eduardo", 28)
print("nombre:", persona2.nombre, "edad: ", persona2.edad)
print(id(persona2))#imprime la direccion de memoria del objeto
