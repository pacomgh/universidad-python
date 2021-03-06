#esta clase crea una orden para las computadoras que se compran

class Orden:
    #falta agregar setters y getters
    contadorOrdenes = 0
    def __init__(self, computadoras):#computadoras es una lista de computadoras
        Orden.contadorOrdenes += 1
        self.__idOrden = Orden.contadorOrdenes
        self.__computadoras = computadoras
        
    def agregarComputadora(self, computadora):
        #agregamos a la lista de computadoras una nueva computadora
        self.__computadoras.append(computadora)
        
    def __str__(self):
        computadoraStr = ""
        for computadora in self.__computadoras:
            computadoraStr += computadora.__str__()
        
        return(
            f"Orden: {self.__idOrden}, "
            f"Computadoras: {computadoraStr}"
        )
