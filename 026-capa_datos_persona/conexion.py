from logger_base import logger
import psycopg2 as db
import sys

#clase que crea solamente la conexion a la bd
#definimos la clase conexion con sus atributos
class Conexion:
    #se ponen en mayusculas porque son constantes
    __DATABASE = "test_db"
    __USERNAME = "postgres"
    __PASSWORD = "admin"
    __DB_PORT = "5432"
    __HOST = "127.0.0.1"
    __conexion = None
    __cursor = None
    
    @classmethod
    #cls es una referencia a nuestra clase
    def obtenerConexion(cls):#cls se usa para acceder a los estaticos de la clase
        #no se ha inicializado la variable
        if cls.__conexion is None:
            try:
                #inicializamos la conexion
                cls.__conexion = db.connect(host=cls.__HOST,
                                            user = cls.__USERNAME,
                                            password = cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database = cls.__DATABASE)
                #lo mandamos al debug ya que no es tan importante
                logger.debug(f"Conexion exitosa: {cls.__conexion}")
                return cls.__conexion
            except Exception as e:
                #usammos el logger y lo maneajamos como un error
                logger.error(f'Error al conectar a la BD: {e}')
                #si ocurre un error terminamos el programa
                sys.exit()
        else:
            #si el objeto esta inicializado ya, solo lo regresamos
            return cls.__conexion
    
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                #si el metodo funcionade manera correcta regresa la conexion
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f'Se abrio el cursor con éxito: {cls.__cursor}')
                #si se realizo con exito regresamos el cursor
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error al obtener el cursor: {e}')
                sys.exit()
        #si ya fue inicializada regresamos su valor        
        else:
            #regresamos el valor de cursor
            return cls.__cursor
        
    @classmethod
    def cerrar(cls):
        #preguntamos si no es none, que ya se inicializo
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.error(f'Error al cerrar cursor: {e}')
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as e:
                logger.error(f'Error al cerrar conexion: {e}')
        logger.debug('Se han cerrado los objetos de conexion y cursor')
            
            
            
if __name__ == '__main__':
    #llamamos el metodo conexion de nuestra clase para comprbar
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrar()
