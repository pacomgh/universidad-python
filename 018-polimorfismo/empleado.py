#polimorfismo variable que puede apuntar a un objeto de tipo padre o tipo hijo
#dependiendo del tipo es el metodo que se ejecuta de la clase, depende a donde apunte
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
    def __str__(self):
        return "Nombre: " + self.nombre + ", sueldo: "+str(self.sueldo)