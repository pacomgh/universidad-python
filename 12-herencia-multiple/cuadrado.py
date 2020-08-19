#Es importante definir de que lado estara cada clase padre, del lado derecho
#se define en primer lugar, del izquierdo en segundo lugar
#Toma prioridad la clase de la izquierda, al final esta la clase object
from figura_geometrica import FiguraGeometrica
from color import Color
#primero se reciben los atributos de las clases de izq a der
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super llama el constructor de la clase de izq en prioridad mayor
        #Codigo explicito clase.__init__(), debemos pasar self + params
        FiguraGeometrica.__init__(self, lado, lado)
        #llamada con super, no es necesario pasar self y llama a la clase de la izq
        #se llama el init de la clase y se mandan los param correspondientes
        #super().__init__(lado, lado)
        #pasamos en el init de la clase externa el valor de parametro recibido
        #en el init de la clase de este archivo
        Color.__init__(self, color)
        #este metodo se define a este nivel porque el area depende del tipo
        #de figura, dentro de la clase hija
    def area(self):
        return self.alto*self.ancho
    