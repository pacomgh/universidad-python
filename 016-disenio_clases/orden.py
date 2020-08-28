class Orden:
    contadorOrdenes = 0
    
    def __init__(self, productos):
        Orden.contadorOrdenes += 1
        #cuando ya fue contado y se asigno nuevo valor
        self.__idOrden = Orden.contadorOrdenes
        self.__productos = productos
        
    def agregarProducto(self, producto):
        self.__productos.append(producto)
        
    def calcularTotal(self):
        total = 0
        for producto in self.__productos:
            total += producto.getPrecio()
        return total
                
        
    def __str__(self):
        #almacena todas las llamadas al metodo str de producto y obtener valores
        productos_str = ""
        for producto in self.__productos:
            #llamamos al metodo str para concatenar los valores de producto
            productos_str += producto.__str__() + " | "     
            
        return "Orden: "+str(self.__idOrden) + ", Productos: " + productos_str
