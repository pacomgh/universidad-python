#extiende de la clase exception para que sea una clase valida
class NumerosIdenticosException(Exception): 
    def __init__(self, mensaje):
        #message esta definido dentro de la clase padre
        self.message = mensaje