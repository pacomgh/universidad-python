"""El encapsulamiento evita que se acceda directamente a los atributos de una
clase """

class Persona:
    def __init__(self, nombre, edad):
        # __ indica que un atributo es privado
        self.__nombre = nombre
        self.__edad = edad
    
    #obtenemos informacion del atriibuto
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad
    
    #mandamos informacion al atributo de nuestra clase
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setEdad(self, edad):
        self.__edad = edad
    
        
p1 = Persona("Juan", 18)
#print(p1.__nombre) marca error por el tipo de modificador de acceso
print(p1.getNombre())
print(p1.getEdad())
p1.setNombre("Pedro")
p1.setEdad(25)
print(p1.getNombre())
print(p1.getEdad())
