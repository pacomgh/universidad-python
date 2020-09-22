class Teclado(DispositivoEntrada):
    
    contadorTeclados = 0
    def __init__(self, idTeclado):
        self.__idTeclado = idTeclado
        contadorTeclados += 1
        
    def __str__(self):
        return "id: "+str(self.__idTeclado)