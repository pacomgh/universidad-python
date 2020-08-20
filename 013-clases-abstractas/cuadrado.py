from clase_abstracta import ClaseAbstracta
from color import Color


class Cuadrado(ClaseAbstracta, Color):
    def __init__(self, lado, color):
        ClaseAbstracta.__init__(self, lado, lado)
        Color.__init__(self, color)
    def area(self):
        return self.alto*self.ancho
    
