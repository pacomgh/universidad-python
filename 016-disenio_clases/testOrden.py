from producto import Producto
from orden import Orden

producto1 = Producto("Camisa", 100)
producto2 = Producto("Pantalon", 200)
producto3 = Producto("Calcetines", 50.00)

productos = [producto1, producto2]
print(productos)

orden1 = Orden(productos)
print(orden1)
print(orden1.calcularTotal())
#agrega un nuevo objeto
#productos.append(producto3)
orden2 = Orden(productos)
orden2.agregarProducto(producto3)
print(orden2)
print(orden2.calcularTotal())