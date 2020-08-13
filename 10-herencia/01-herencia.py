#object <- *extends* Persona <- *extends* Empleado

#clase padre, se definen todos los atributos genericos de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #para evitar que se imprima una direccion de memoria usamos str
    def __str__(self):
        #devuelve una cadena
        #convertimos edad(int) a una cadena con str()
        return "Nombre: "+self.nombre+", edad: "+str(self.edad)

#clase hija
#entre parentesis se pone la clase de cual va a heredar
#hereda las caracteristicas de la clase padre
class Empleado(Persona):
    #definimos nuevamente el metodo init para que contenga atributos propios
    #le pasamos los parametros que va a heredar(nombre, edad)
    #agregamos los parametros/atributos propios de la clase(sueldo)
    def __init__(self, nombre, edad, sueldo):
        #inicializamos los valores de la clase padre con super
        #super accede a la clase padre
        #pasamos los valores nombre, edad para poder inicializar el objeto de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    #definimos nuevamente el metodo str para imprimir los valores anteriores y los nuevos
    def __str__(self):
        return super().__str__() + ", sueldo: "+ str(self.sueldo)
        
persona = Persona("Juan", 28)
print(persona)#imprime una direccion de memoria

empleado = Empleado("Jose", 22, 3800)
print(empleado)

empleado.nombre = "Jose Madero"
empleado.sueldo = 10000.99
print(empleado)
        
        
    
    
