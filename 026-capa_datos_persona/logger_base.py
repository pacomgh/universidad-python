#logging nos permitira enviar informacion a multiples destinos, incluida la consola
#podemos priorizar los mensajes
import logging
#variable logger a utilizar
logger = logging

##definimos el nivel desde el que deseamos enviar mensajes
#debug solo se usa en etapa de desarrollo
#handlers son los diferentes medios por los cuales enviamos informacion
logger.basicConfig(level=logging.DEBUG,#nivel debug hacia arriba
                   #modifica el formato de la informacion que se envia
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),#archivo que va a recibir la informacion
                       logging.StreamHandler(),#se envia la informacion a la consola
                   ])

#asignamos el nombre main a este archivo
if __name__ == '__main__':
    #solo se imprime esta informacion cuando se ejecuta este archivo
    logging.warning('Mensaje a nivel warning')
    logging.info('Mensaje a nivel info')
    logging.debug('Mensaje a nivel debug')

    logging.error('Ocurrio un error en la base de datos')
    logging.debug('Se realizo la conexion con éxito')
