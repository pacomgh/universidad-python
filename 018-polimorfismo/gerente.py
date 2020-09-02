from empleado import Empleado
#hereda de la clase empleado, para que exista polimorfismo debe existir herencia
class Gerente(Empleado):
    #recibimos los parametros de la clase padre + el nuevo atributo
    def __init__(self, nombre, sueldo, departamento):
        #accedemos a la clase padre y pasarle los valores que tenia
        #inicializamos los atributos de la clase padre
        super().__init__(nombre, sueldo)
        self.departamento = departamento
        
    def __str__(self):
        #con el super reutilizamos el valor de retorno de este metodo en la clase
        #padre
        return super().__str__() + ", Departamento: "+self.departamento
        