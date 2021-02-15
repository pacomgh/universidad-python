from logger_base import logger
#clase que crea el modelo de persona
class Persona:
    ##como vamos a mandar los parametros por nombre, asignamos un valor inicial
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        
    def __str__(self):
        return(
            f'Id persona: {self.__id_persona}, '
            f'Nombre: {self.__nombre}, '
            f'Apellido: {self.__apellido}, '
            f'Email: {self.__email}'
        )
        
    #agregar getters y setters
    def setIdPersona(self, id_persona):
        self.__id_persona = id_persona

    def getIdPersona(self):
        return self.__id_persona
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido

    def getApellido(self):
        return self.__apellido
    
    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email
    
if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'correo@correo')
    logger.debug(persona1)
    #simulando un objeto a insertar de tipo peresona
    #indicamos nombre de parametro y valor, solo dejamos los parametros a utilizar
    persona2 = Persona(nombre='Karla', apellido='Gomez', email='kgomez@mail.com')    
    logger.debug(persona2)
    #simular el caso de eliminar un objeto de tipo persona, especificamos el nombre del argumento
    #debemos especificar los argumentos cuando no los mandamos todos como parametro
    persona3 = Persona(id_persona=3)
    logger.debug(persona3)
