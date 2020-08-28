class Producto:
    #se define en 0 para que cuando se cree un objeto se aumente el contador
    contadorProductos = 0#asociada a la clase
    
    def __init__(self, nombre, precio):
        Producto.contadorProductos += 1
        #cada que se crea un producto se aumenta en 1
        self.__idProducto = Producto.contadorProductos
        self.__nombre = nombre
        self.__precio = precio
        
    def getPrecio(self):
        return self.__precio
        
    def __str__(self):
        return "id producto: "+str(self.__idProducto) + ", nombre: "+self.__nombre+", precio: " + str(self.__precio)
        
