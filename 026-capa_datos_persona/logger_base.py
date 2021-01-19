#logging nos permitira enviar informacion a multiples destinos, incluida la consola
#podemos priorizar los mensajes
import logging

logger = logging

##definimos el nivel desde el que deseamos enviar mensajes
#debug solo se usa en etapa de desarrollo
logger.basicConfig(level=logging.WARNING)

logging.warning('Mensaje a nivel warning')
logging.info('Mensaje a nivel info')
logging.debug('Mensaje a nivel debug')

logging.error('Ocurrio un error en la base de datos')
logging.debug('Se realizo la conexion con éxito')