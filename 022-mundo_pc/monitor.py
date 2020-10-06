class Monitor:
    contadorMonitores =0
    
    def __init__(self, marca, tamanio):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca 
        self._tamanio = tamanio
        
    def setMarca(self, marca):
        self._marca = marca
    def getMarca(self):
        return self._marca
    def setTamanio(self, tamanio):
        self._tamanio = tamanio
    def getTamanio(self):
        return self._tamanio
    
    def __str__(self):
        return (
            f"id: {self._idMonitor}, "
            f"marca: {self._marca}, "
            f"Tamanio: {self._tamanio}"
        )
        
#monitor = Monitor("Lenovo", "13inch")
#monitor2 = Monitor("HP", "15inch")
#print(monitor)
#print(monitor2)
    