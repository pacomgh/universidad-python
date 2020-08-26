class MiClase:
    variableClase = "variable de clase"
    #variable de instania con init
    def __init__(self):
        #se crea hasta que se le asigna un valor
        #la variable se crea hasta que se crea un objeto y se llama al constructor init
        self.variableInstancia = "variable instancia"
    #definimos metodo static con el decorador
    #se asocia a la clase, y no recibe parametro, no esta disponible self porque
    #se asocia con objetos, los metodos estatico no pueden acceder a variables
    #de instancia
    @staticmethod
    def metodoEstatico():
        print("Soy un metodo estatico")
        #accedemos al atributo de clase con el nombre de la clase
        print(MiClase.variableClase)
        #Desde el metodo estatico no podemos acceder a variables de instancia
        #rint(MiClase.variableInstancia)
    #la diferencia es que si reibe un parametro que es el tipo de la clase
    #cls hace referencia a la clase, no puede recibir self, hace referencia
    #a instancias de la clase
    @classmethod
    def metodoClase(cls):
        print("Metodo de clase: "+str(cls))
        #accedemos a variableClase con el parametro de cls
        print(cls.variableClase)
        #Desde el metodo estatico no podemos acceder a variables de instancia
        #rint(cls.variableInstancia)
        
    #desde un metodo de instancia(se asocia a los objetos), si podemos acceder a
    #variables de instancia
    def metodoInstancia(self):
        self.metodoEstatico()
        self.metodoClase()
        print(self.variableClase)
        print(self.variableInstancia)
       

#podemos usar el nombre de la clase sin crear una instancia 
MiClase.metodoEstatico()
#accedemos a el a traves del nombre de la clase
MiClase.metodoClase()
print()
objeto1 = MiClase()
objeto1.metodoInstancia()