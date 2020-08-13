#sin guion bajo -> publico
# _  -> parcialmente privado o protegido
# __ -> privado
#no podemos acceder a un metodo/atributo privado desde fuera de la clase

class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno):
        self.nombre = nombre
        self._apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        
    def metodoPublico(self):
        self.__metodoPrivado()
        
    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellidoPaterno)
        print(self.__apellidoMaterno)
    
    def getApellidoMaterno(self):
        return self.__apellidoMaterno
    def setApellidoMaterno(self, apellidoMaterno):
        self.__apellidoMaterno = apellidoMaterno
        
p1 = Persona("Juan", "Perez", "Lopez")
#p1.__metodoPrivado() no se puede acceder
#podemos acceder al metodo privado desde un metodo publico
p1.metodoPublico()
print(p1.nombre)
print(p1._apellidoPaterno)#si podemos acceder a este atributo
#con los metodos set y get podemos modificar y acceder a los atributos que privados
p1.setApellidoMaterno("Gonzales")
print(p1.getApellidoMaterno())


        
