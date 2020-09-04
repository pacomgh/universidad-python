from empleado import Empleado
from gerente import Gerente

#priermo definimos un metodo antes de utilizarlo
#definimos
#recibe una referencia de la clase padre
#el parametro puede ser referencia de cualquier objeto(clase padre/hija)
def imprimirDetalles(objeto):
    #por utilizar print se llama automaticamente al metodo str
    print(objeto)#llama al metodo str
    print(type(objeto), end="\n\n")
    #pregunta si una variabe es de la instacia que necesitamos
    #si es instancia de(variableUsada, tipo)
    if isinstance(objeto, Gerente):
        print(objeto.departamento)#si no es de tipo gerente lanzaria un error
empleado = Empleado("Juan", 1000)
imprimirDetalles(empleado)

empleado = Gerente("Karla", 2000.00, "Sistemas")
imprimirDetalles(empleado)
