from cuadrado import Cuadrado

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.color)

#saber el orden en que se ejecutan nuestras clases  
#clase.mro(), mro = method resolution order
print(Cuadrado.mro())