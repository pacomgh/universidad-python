from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO(Data Acces Object) sirve para hacer CRUD: create, read, update y delete
    sobre la entidad persona
    '''
    __SELECCIONAR = 'SELECT  * from persona ORDER BY id_persona'
    
    @classmethod
    def seleccionar(cls):
        #obtenemos una conexion, accederemos al cursor
        #cls hace referencia a la clase en la que estamos trabajando
        cursor = Conexion.obtenerCursor()
        #para imprimir el query usamos mogrify
        #mogrify hace una validacion previa del query
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        #solicitamos el fetchall apra regresar todos los registros
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            #creamos y guardamos los campos de cada registro en un arreglo
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            #agregamos al arreglo cada objeto persona
            personas.append(persona)
        return personas
    

if __name__ == '__main__':
    personas = PersonaDao.seleccionar()
    for persona in personas:
        logger.debug(persona)
        logger.debug(persona.getIdPersona())
            
        