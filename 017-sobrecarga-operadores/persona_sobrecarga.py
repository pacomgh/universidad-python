class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    #metodo sobreescrito de la clase padre object
    def __add__(self, otro):
        #accedemos al nombre del objeto y lo concatenamos con el nombre del otro
        #objeto
        return self.__nombre + " " + otro.__nombre      
    
    def __sub__(self, otro):
        return "Operacion no soportada"  
        
p1 = Persona("juan")
p2 = Persona("Karla")
#la llamada al metodo add se hace automaticamente, solo se concatenan objetos 
#cuando sobreescribimos el metodo add
#sobrecarga agrega una nueva forma de trabajar al operador +
print(p1+p2)
print(p1-p2)