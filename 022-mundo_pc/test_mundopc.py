from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

#creamos objetos que no dependen de otras clases
tecladoHP = Teclado ("hp", "usb")
ratonHP = Raton("hp", "usb")
monitorHP = Monitor("hp", "15pulgada")
computadraHP = Computadora("HP", monitorHP, tecladoHP, ratonHP)

tecladoAcer = Teclado("Acer", "usb")
ratonAcer = Teclado("Acer", "Bluetooth")
monitorAcer = Monitor ("Acer", "13pulgadas")
computadoraAcer = Computadora("Acer", monitorAcer, tecladoAcer, ratonAcer)

tecladoGamer = Teclado ("Gamer", "Bluetooth")
ratonGamer = Raton("Gamer", "USB")
monitorGamer = Monitor("Gamer", "47 pulgadas")
computadoraGamer = Computadora("Gamer", monitorGamer, tecladoGamer, ratonGamer)

computadoraArmada = Computadora("Armada", monitorHP, tecladoAcer, ratonGamer)

#creamos la lista de ordenes
computadoras1 = [computadraHP, computadoraAcer]
#creamos las ordenes
orden1 = Orden(computadoras1)
#se llama el metodo str de orden y este manda a llamar a los otros metodos str
#agregamos una nueva computadora a la lista
orden1.agregarComputadora(computadoraGamer)
print(orden1)

#orden 2
computadoras2 = [computadoraGamer, computadoraArmada, computadoraAcer]
orden2 = Orden(computadoras2)
orden2.agregarComputadora(computadraHP)
print(orden2)

