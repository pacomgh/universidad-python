#Crear un codigo en donde se pida el largo, ancho y la altura para calcular el area de
#una caja, los datos debe proporcionarlos el usuario

class Caja:
    
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        
    def calcVolumen(self):
        return self.largo * self.ancho * self.altura
    
largo = float(input("Ingresa el largo de la caja: "))
ancho = float(input("Ingresa el ancho de la caja: "))
altura = float(input("Ingresa la altura de la caja: "))

caja = Caja(largo, ancho, altura)
print("El volumen de la caja es: ",caja.calcVolumen()," mts cubicos")
