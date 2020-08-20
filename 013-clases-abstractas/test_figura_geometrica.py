from cuadrado import Cuadrado
from clase_abstracta import ClaseAbstracta
#no es posible crear objetos de una clase abstracta
#figuraGeometrica = ClaseAbstracta()
#sigue funcionado porque el cuadrado tiene el metodo area definido
cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.color)

#saber el orden en que se ejecutan nuestras clases  
#clase.mro(), mro = method resolution order
print(Cuadrado.mro())