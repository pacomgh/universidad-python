#clase abstracta es aquella que no se puede instanciar
#las clases hijas son las que hacen la implementacion de los metodos
#no podemos crear objetos de una clase abstracta
#ABC permite clases y metodos abstractos
#decorador agrega funcionalidad a los metodos
from abc import ABC, abstractmethod
#entiende de abc(clase abstracta)
class ClaseAbstracta(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    #abc significa abstract base class
    @abstractmethod #decorador
    def area(self):
        pass
