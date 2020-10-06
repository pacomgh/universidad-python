#esta clase contiene los elementos de las clases que ya hemos trabajado
from monitor import Monitor
from teclado import Teclado
from raton import Raton
class Computadora:
    contadorComputadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        #definimos valor a variables de clase
        Computadora.contadorComputadoras += 1
        self.__idComputadora = Computadora.contadorComputadoras
        self.__nombre = nombre
        #asignamos a variables de clase objetos de la clase respectiva
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
        
    def __str__(self):
        return(#se sustituye lo que esta entre {} por el valor del atributo
               #en monitor se llama el metodo str de esa clase
            f"""
            {self.__nombre}: {self.__idComputadora}
                Monitor: {self.__monitor}
                Teclado: {self.__teclado}
                Raton: {self.__raton}
            """
        )
    
#monitor1 = Monitor("HP", "15 pulgadas")
#teclado1 = Teclado("HP", "USB")
#raton1 = Raton("HP", "USB") 
#computadora1 = Computadora("HP", monitor1, teclado1, raton1)
#print(computadora1)
    
        
    