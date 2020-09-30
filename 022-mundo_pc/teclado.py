from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contadorTeclados = 0
    def __init__(self,marca, tipoEntrada):
        Teclado.contadorTeclados +=1
        self.__idTeclado = Teclado.contadorTeclados
        self._marca = marca
        self._tipoEntrada = tipoEntrada
        
    def __str__(self):
        return (
            f"id: {self.__idTeclado}, "
            f"marca: {self._marca}, "
            f"tipoEntrada: {self._tipoEntrada}"
        )
        
teclado = Teclado("hp", "cable")
print(teclado)
