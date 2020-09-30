class DispositivoEntrada:
    
    def __init__(self, tipoEntrada, marca):
        #para que sea protegido es solo un _
        #atributos protegidos
        self._tipoEntrada = tipoEntrada
        self._marca = marca
        
    def getTipoEntrada(self):
        return self._tipoEntrada

    def setTipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    def setMarca(self, marca):
        self._marca

    def getMarca(self):
        return self._marca
    
    

