from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO(Data Acces Object) sirve para hacer CRUD: create, read, update y delete
    sobre la entidad persona
    '''
    __SELECCIONAR = 'SELECT  * from persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
    
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
        Conexion.cerrar()
        return personas
    
    @classmethod
    #mandamos los parametros en el objeto eprsona
    def insertar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))       
            logger.debug(f'Persona a insrtar: {persona}')       
            #creamos tupla de valores
            valores = (persona.getNombre(), persona.getApellido(), persona.getEmail())
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()#mandamos a base de datos            
            return cursor.rowcount()#indica cuantos registros se insertaron
        except Exception as e:
            conexion.rollback()#si algo sale mal damos marcha atras
            logger.error(f'Excepcion, error al insertar persona: {e}')   
        finally:
            Conexion.cerrar()
    

if __name__ == '__main__':
    #personas = PersonaDao.seleccionar()
    #for persona in personas:
    #    logger.debug(persona)
    #    logger.debug(persona.getIdPersona())
    
    #inseramos nuevo registro
    persona=Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    personas_insertadas=PersonaDao.insertar(persona)
    
    logger.debug(f'Registros insertados: {personas_insertadas}')