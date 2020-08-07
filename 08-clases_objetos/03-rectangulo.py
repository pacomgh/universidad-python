#Crear una clase en donde se pida la base y la altura para calcular el area de
#un rectangulo, los datos debe proporcionarlos el usuario

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    #def menu():
    #    base = int(input("Ingresa la base del rectangulo"))
    #    altura = int(input("Ingresa la altura del rectangulo"))
    
    #loque hizo el profe
    """pasamos el self para poder acceder a los atributos de la clase"""
    def calcArea(self):
        return self.base*self.altura
     
    #lo que yo hice   
    #def calcArea(base=0, altura=0):
        #base = int(input("Ingresa la base del rectangulo"))
        #altura = int(input("Ingresa la altura del rectangulo"))
    #    area = base*altura
    #    return "El area del rectangulo es: " + area

base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))
rect = Rectangulo(base, altura)   
print(rect.calcArea())
#rect = Rectangulo()
#rect.menu()
#rect.calcArea()
