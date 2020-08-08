class Persona:
    #se puede usar otro nombre en lugar de self
    #* = parametro opcional, enviar tupla
    #** enviar diccionario, son opcionales
    def __init__(this, nombre, edad, *values, **d):
        this.nombre = nombre
        this.edad = edad
        this.values = values
        this.d = d
    #podemos cambiar el nombre por otro pero hace referencia al this
    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Valores tupla: ", self.values)
        print("Diccionario: ", self.d)
        
p1 = Persona("juan", 28)
#print(p1.nombre)
#print(p1.edad)
p1.desplegar()
print()
p2 = Persona("Karla", 30, 2, 4, 6)
p2.desplegar()
print()
p3 = Persona("Paloa", 33, 6,7, m="manzana", p="Pera")
p3.desplegar()