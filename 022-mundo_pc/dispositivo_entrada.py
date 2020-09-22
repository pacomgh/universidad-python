class DispositivoEntrada:
    
    def __init__(self, tipoEntrada, marca):
        #para que sea protegido es solo un _
        #atributos protegidos
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    
    """ def setTipoEntrada(self, tipoEntrada):
        self.__tipoEntrada = tipoEntrada
    
    def getTipoEntrada(self):
        return self.__tipoEntrada
    
    def setMarca(self, marca):
        self.__marca
    
    def getMarca(self):
        return self.__marca
    
    def __str__(self):
         """