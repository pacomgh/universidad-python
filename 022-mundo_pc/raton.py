from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    #variable estatica que cuenta nuestra cantidad de objetos de esta clase
    contadorRatones = 0
    def __init__(self, marca, tipoEntrada):
        #accedemos a la variable estatica mediante el nombre de la clase
        Raton.contadorRatones += 1
        #self.__idRaton = idRaton
        self.__idRaton = Raton.contadorRatones
        ##accedemos a los atributos protegidos, podemos acceder directamente a ellos
        #con el parametro de self._atributoProtegido
        self._marca = marca
        self._tipoEntrada = tipoEntrada
        
        
    def __str__(self):
        #cuando imrpimirmos varias lineas podemos usar ()
        return (#f es un formato de tipo cadena(da formato), manda llamar al metodo str
                f"id: {self.__idRaton}, "
                f"marca: {self._marca}, " 
                f"tipoEntrada: {self._tipoEntrada}"                
            )
        
#raton = Raton("hp", "usb")
#print(raton)
